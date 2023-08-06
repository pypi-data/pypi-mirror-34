function (data, type, row, meta) {
    if (type === 'display') {
        return "<img src='"+data+"' alt=''>";
    } else {
        return '';
    }
}
