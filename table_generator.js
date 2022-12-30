const verbs_table_map = new Map(Object.entries(verbs_table));

function isMemoized(arr, form) {
    for (let verb of arr) {
        if(!document.cookie.includes(verb + "=" + form)) {
            return false;
        }
    }
    return true;
}

function refreshTable() {
    let table = '<table  class="center" width="70%">'
    let color = 'white'
    for (let [verb, m] of verbs_table_map) {
        let second = isMemoized(m['second'], 'second') ? 'V' : '-';
        let third = isMemoized(m['third'], 'third') ? 'V' : '-';
        color == 'white' ?  color = '#D3D3D3' : color = 'white'
        table += '<tr align="center" bgcolor="' + color + '"> <td width="50%">' + verb + '</td> <td width="25%">' + second + '</td> <td width="25%">' + third + '</td></tr>';
    }
    table += '</table>';

    document.getElementById("table").innerHTML = table;
}