function (data, type, row, meta) {
    var price=row.getPrice,
        durat=row.getDuration,
        val3='',
        info='',
        year=row['getDateForList/year'],
        uid=row.UID,
        url='course_overview?cuid='+uid,
        res='<h3><a href="' + url + '">' + row.Title + '</a></h3>';

    if (price) {
        if (info) {
            info += ' / ' + price;
        } else {
            info = price;
        }
    }
    if (durat) {
        if (info) {
            info += ' / ' + durat;
        } else {
            info = durat;
        }
    }
    if (year) {
        if (info) {
            info += ' / ' + year;
        } else {
            info = year;
        }
    }
    if (info) {
        res += '<div class="info-data"><p class="info">'+info+'</p></div>';
    }
    val3 = row.Description;
    if (val3) {
        res += '<p class="text-plain">'+val3+'</p>';
    }
    if (uid !== 'c83e5e6a9680b002112c3fd95049c602' &&
        uid !== '29078be2d47834e757f02568b5393947') {
        res += '<form method="GET" action="@@booking/add_article">' +
               '<button class="btn btn-primary" type="submit">' +
               '<i class="glyphicon glyphicon-shopping-cart icon-white"></i>' +
               _('book this course') +
               '</button>' +
               '<input type="hidden" name="uid" value="'+uid+'">' +
               '</form>';
    }
    return res;
}
