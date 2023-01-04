const verbs_table_map = new Map(Object.entries(verbs_table));

function isMemoized(arr, form) {
    for (let verb of arr) {
        if(!document.cookie.includes(verb + "_" + form + "=")) {
            return false;
        }
    }
    return true;
}

function refreshTable() {
    let table = '<table  class="center" width="70%">';
    table += '<tr align="center" bgcolor="white"><th width="10%"> # </th><th width="40%"> Infinitive </th> <th width="25%"> Past Simple </th> <th width="25%">Past Participle</th></tr>';
    let color = 'white';
    let count = 0;
    for (let [verb, m] of verbs_table_map) {
        count += 1;
        let second = isMemoized(m['second'], 'second') ? '&#10004;' : '-';
        let third = isMemoized(m['third'], 'third') ? '&#10004;' : '-';
        color == 'white' ?  color = '#C5C6C7' : color = 'white'
        table += '<tr align="center" bgcolor="' + color + '"> <td width="10%">' + count + '</td> <td width="40%">' + verb + '</td> <td width="25%">' + second + '</td> <td width="25%">' + third + '</td></tr>';
    }
    table += '</table>';

    document.getElementById("table").innerHTML = table;
}

function openTab(tab_to_show, tab_to_hide) {
    [document.getElementById("about_button").style.backgroundColor, document.getElementById("application_button").style.backgroundColor] = 
        [document.getElementById("application_button").style.backgroundColor, document.getElementById("about_button").style.backgroundColor];

    [document.getElementById("about_button").style.borderTop, document.getElementById("application_button").style.borderTop] = 
        [document.getElementById("application_button").style.borderTop, document.getElementById("about_button").style.borderTop];

    [document.getElementById("about_button").style.borderBottom, document.getElementById("application_button").style.borderBottom] = 
        [document.getElementById("application_button").style.borderBottom, document.getElementById("about_button").style.borderBottom];

    [document.getElementById("about_button").style.borderLeft, document.getElementById("application_button").style.borderRight] = 
        [document.getElementById("application_button").style.borderRight, document.getElementById("about_button").style.borderLeft];

    document.getElementById(tab_to_show).style.display = "block";
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