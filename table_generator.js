const verbs_table_map = new Map(Object.entries(verbs_table));

function isMemoized(arr) {
    for (let verb of arr) {
        if(!document.cookie.includes(verb)) {
            return false;
        }
    }
    return true;
}

function refreshTable() {
    let table = '<table  class="center" width="70%">'
    for (let [verb, m] of verbs_table_map) {
        let second = isMemoized(m['second']) ? 'V' : '-';
        let third = isMemoized(m['third']) ? 'V' : '-';
        table += '<tr align="center"> <td width="50%">' + verb + '</td> <td width="25%">' + second + '</td> <td width="25%">' + third + '</td></tr>';
    }
    table += '</table>';

    document.getElementById("table").innerHTML = table;
}