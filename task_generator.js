const second_sentences_map = new Map(Object.entries(second_sentences));
const third_sentences_map = new Map(Object.entries(third_sentences));

function getRandomIndex(len) {
    return Math.floor(Math.random() * len);
}

function getNextVerb() {
    for (let [verb, first, form, _] of all_verbs_list) {
        if(!document.cookie.includes(verb + "_" + form + "="))
        {
            return [verb, first, form];
        }
    }
    return ["", "", ""];
}

function scheduleNextVerefication(verb, form, correctAnswers) {
    var date = new Date();
    var time = date.getTime();
    var expireTime = time + 1000 * 60 * Math.pow(3, correctAnswers);
    date.setTime(expireTime);
    document.cookie = verb + "_" + form + "=" + "; SameSite=None; Secure; expires=" + date.toGMTString() + ";";
}

let expectedValue = []

function fixActions(){
    document.getElementById('answer').disabled = true;
    document.getElementById("help").disabled = true;
    document.getElementById("next").disabled = false;
    document.getElementById("next").focus();
}

function incrementCorrectAnswers(verb, form) {
    let key = verb + "_" + form;
    let correctAnswers = localStorage.getItem(key);
    if (!correctAnswers) correctAnswers = 8;
    correctAnswers += 1;
    localStorage.setItem(verb, correctAnswers);
    return correctAnswers;
}

function resetCorrectAnswers(verb, form) {
    let key = verb + "_" + form;
    let correctAnswers = localStorage.getItem(key);
    if (!correctAnswers) correctAnswers = 1;
    localStorage.setItem(verb, correctAnswers);
    return correctAnswers;
}

function isAnswerCorrect(expected, actual){
    return (expected == actual) || (actual in synonyms && synonyms[actual] == expected);
}

function verify() {
    let actualValue = document.getElementById('answer').value
    let [verb, form] = expectedValue
    if(isAnswerCorrect(verb, actualValue.toLowerCase())){
        correctAnswers = incrementCorrectAnswers(verb, form);
        scheduleNextVerefication(verb, form, correctAnswers);
        fixActions();
    }
}

function help() {
    let [verb, form] = expectedValue
    document.getElementById('answer').value = verb;
    correctAnswers = resetCorrectAnswers(verb, form);
    scheduleNextVerefication(verb, form, correctAnswers);
    fixActions();
}

function next() {
    let [verb, firstForm, form] = getNextVerb();
    expectedValue = [verb, form]
    if(form == "second") {
        document.getElementById("task").innerHTML = getNextTask(verb, firstForm, second_sentences_map);
    }
    else {
        document.getElementById("task").innerHTML = getNextTask(verb, firstForm, third_sentences_map);
    }
    document.getElementById("next").disabled = true; 
    document.getElementById("help").disabled = false;
    document.getElementById("answer").focus();
    updateProgress();
    refreshTable();
}

function getNextTask(verb, firstForm, sentences_map) {
    if(verb) {
        sentences = sentences_map.get(verb);
        const index = getRandomIndex(sentences.length);
        let sentence = sentences[index];
        let inputLen = verb.length + 2
        let task = ' <input type="text" id="answer" onkeyup="verify();" style="font-size: 0.7em; margin-bottom: 0.5em; margin-top: 0.5em; width:' + inputLen + 'em;"> (' + firstForm + ') ';

        var regEx = new RegExp(verb, "ig");
        sentence = sentence.replace(regEx, task);

        return sentence;
    }
    else {
        return "Congratulation!!! there are no irregular verbs left to learn!";
    }
}

function updateProgress() {
    let memorised = (document.cookie.match(/=/g) || []).length;
    let total = all_verbs_list.length;
    let percents = (memorised/total)*100;

    document.getElementById("progress").max = total
    document.getElementById("progress").value = percents
    document.getElementById("progress_note").innerHTML = "Learned " + memorised.toString() + " irregular verbs out of " + total.toString()
}

window.onload = function() { 
    if((document.cookie.match(/=/g) || []).length > 0) {
        document.getElementById("application").style.display = "block";
        document.getElementById("about").style.display = "none";

        [document.getElementById("about_button").style.backgroundColor, document.getElementById("application_button").style.backgroundColor] = 
            [document.getElementById("application_button").style.backgroundColor, document.getElementById("about_button").style.backgroundColor];

        [document.getElementById("about_button").style.borderTop, document.getElementById("application_button").style.borderTop] = 
            [document.getElementById("application_button").style.borderTop, document.getElementById("about_button").style.borderTop];

        [document.getElementById("about_button").style.borderBottom, document.getElementById("application_button").style.borderBottom] = 
            [document.getElementById("application_button").style.borderBottom, document.getElementById("about_button").style.borderBottom];

        [document.getElementById("about_button").style.borderLeft, document.getElementById("application_button").style.borderRight] = 
            [document.getElementById("application_button").style.borderRight, document.getElementById("about_button").style.borderLeft];
    }

    next(); 
};
  

