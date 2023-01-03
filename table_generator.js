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