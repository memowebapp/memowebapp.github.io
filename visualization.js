const verbs_table_map = new Map(Object.entries(verbs_table));

function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

function openedClass() {
    return isMobileDevice() ? "opened-tab-mobile" : "opened-tab";
}

function closedClass() {
    return isMobileDevice() ? "closed-tab-mobile" : "closed-tab";
}

function getVerbString(verb, form){
    let isMemorized = document.cookie.includes(verb + "_" + form + "=");
    let str = isMemorized ? verb : '-';
    if(isMemorized && verb in synonyms) {
        str += " (" + synonyms[verb] + ")";
    }
    return str;
}

function getVerbsStr(verbs, form) {
    let str = "";
    let separator = "";
    for (let verb of verbs) {
        str += separator + getVerbString(verb, form);
        separator = ", ";
    }
    return str;
}

function refreshTable() {
    let table = isMobileDevice() ? '<table width="96%" style="border: solid white 1px; border-spacing: 0; padding: 0;">' : '<table width="70%">';
    table += '<tr align="center" bgcolor="white"><th width="10%"> # </th><th width="40%"> Infinitive </th> <th width="25%"> Past Simple </th> <th width="25%">Past Participle</th></tr>';
    let color = 'white';
    let count = 0;
    for (let [verb, m] of verbs_table_map) {
        count += 1;
        let second = getVerbsStr(m['second'], 'second');
        let third = getVerbsStr(m['third'], 'third');
        color == 'white' ?  color = '#C5C6C7' : color = 'white'
        table += '<tr align="center" bgcolor="' + color + '"> <td width="10%">' + count + '</td> <td width="40%">' + verb + '</td> <td width="25%">' + second + '</td> <td width="25%">' + third + '</td></tr>';
    }
    table += '</table>';

    document.getElementById("verbs_table").innerHTML = table;
}

function openTab(tab_to_show, tab_to_hide) {       
    document.getElementById(tab_to_show+"_button").setAttribute("class", openedClass());
    document.getElementById(tab_to_show).style.display = "block";
    document.getElementById(tab_to_hide+"_button").setAttribute("class", closedClass());
    document.getElementById(tab_to_hide).style.display = "none";
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

        document.getElementById("about_button").setAttribute("class", closedClass());
        document.getElementById("application_button").setAttribute("class", openedClass());
    }
    else {
        document.getElementById("about_button").setAttribute("class", openedClass());
        document.getElementById("application_button").setAttribute("class", closedClass());
    }

    if(isMobileDevice()){
        document.getElementById("main_table").setAttribute("class", "main-table-mobile");
        document.getElementById("task").setAttribute("class", "task-p-mobile");
        document.getElementById("help").setAttribute("class", "action-button-mobile");
        document.getElementById("next").setAttribute("class", "action-button-mobile");
        document.getElementById("header_p").setAttribute("class", "header-p-mobile");
        document.getElementById("verbs_table").setAttribute("class", "verbs-table-mobile");
        document.getElementById("tab_td").setAttribute("class", "tab-td-mobile");
        document.getElementById("progress_note").setAttribute("class", "progress-note-mobile");
    }

    next(); 
};