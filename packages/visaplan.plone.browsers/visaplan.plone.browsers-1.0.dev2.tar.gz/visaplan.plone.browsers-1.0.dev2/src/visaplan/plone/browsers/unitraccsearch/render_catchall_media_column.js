 function (data, type, row, meta) {
    var val=row.getCode, res='';
    if (val) {
    	res += '<div class="info-data"><p class="info">'+val+'</p></div>';
    }
    res += '<h3><a href="' + row.href + '/view">' + row.Title + '</a></h3>';
    val = row.Description;
    if (val) {
        res += '<p>'+val+'</p>';
    }
    return res
}
