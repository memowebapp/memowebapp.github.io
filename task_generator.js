const second_sentences_map = new Map(Object.entries(second_sentences));
const third_sentences_map = new Map(Object.entries(third_sentences));
const verbs_list  = new Array(Object.entries(all_verbs_list));

function getRandomIndex(len) {
    return Math.floor(Math.random() * len);
}

function getNextVerb() {
    for (let [verb, first, form, _] of all_verbs_list) {
        if(!document.cookie.includes(verb))
        {
            return [verb, first, form];
        }
    }
    //console.log(document.cookie);
    return ["", "", ""];
}

function scheduleNextVerefication(verb, correctAnswers) {
    var date = new Date();
    var time = date.getTime();
    var expireTime = time + 1000 * 60 * Math.pow(5, correctAnswers);
    date.setTime(expireTime);
    document.cookie = verb + "=; SameSite=None; Secure; expires=" + date.toGMTString() + ";";
}

let expectedValue = ""

function fixActions(){
    document.getElementById('answer').disabled = true;
    document.getElementById("help").disabled = true;
    document.getElementById("next").disabled = false;
}

function incrementCorrectAnswers(verb) {
    let correctAnswers = localStorage.getItem(verb);
    if (!correctAnswers) correctAnswers = 1;
    correctAnswers += 1;
    localStorage.setItem(verb, correctAnswers);
    return correctAnswers;
}

function resetCorrectAnswers(verb) {
    let correctAnswers = localStorage.getItem(verb);
    if (!correctAnswers) correctAnswers = 1;
    localStorage.setItem(verb, correctAnswers);
    return correctAnswers;
}

function verify() {
    let actualValue = document.getElementById('answer').value
    if(expectedValue == actualValue.toLowerCase()) {
        correctAnswers = incrementCorrectAnswers(expectedValue);
        scheduleNextVerefication(expectedValue, correctAnswers);
        fixActions();
    }
}

function help() {
    document.getElementById('answer').value = expectedValue;
    correctAnswers = resetCorrectAnswers(expectedValue);
    scheduleNextVerefication(expectedValue, correctAnswers);
    fixActions();
}

function next() {
    let [verb, firstForm, form] = getNextVerb();
    expectedValue = verb
    if(form == "second") {
        document.getElementById("task").innerHTML = getNextTask(verb, firstForm, second_sentences_map);
    }
    else {
        document.getElementById("task").innerHTML = getNextTask(verb, firstForm, third_sentences_map);
    }
    document.getElementById("next").disabled = true; 
    document.getElementById("help").disabled = false;
    refreshTable();
}

function getNextTask(verb, firstForm, sentences_map) {
    if(verb) {
        sentences = sentences_map.get(verb);
        const index = getRandomIndex(sentences.length);
        let sentence = sentences[index];
        let task = ' <input type="text" id="answer" onkeyup="verify();"> (' + firstForm + ') ';

        var regEx = new RegExp(verb, "ig");
        sentence = sentence.replace(regEx, task);

        return sentence;
    }
    else {
        return "Congratulation!!! there are no irregular verbs left to learn!";
    }
}

window.onload = function() { next(); };
  

