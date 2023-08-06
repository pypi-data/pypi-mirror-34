function (data, type, row, meta) {
    var info=row.getCode,
        year=row['getDateForList/year'],
        author=row.Rights,
        descr=row.Description,
        res='';
    if (year) {
        if (info) {
            info += ' / ' + year;
        } else {
            info = year;
        }
    }
    if (author) {
        if (info) {
            info += ' / ' + author;
        } else {
            info = author;
        }
    }
    if (info) {
    	res = '<div class="info-data"><p class="info">'+info+'</p></div>';
    }
    res += '<h3><a href="' + url + '">' + row.Title + '</a></h3>';
    if (descr) {
        res += '<p class="text-plain">'+descr+'</p>';
    }
    return res;
}
