$(document).ready(function () {
    $.each($('.datatb-ajax'),
        function (i, v) {
            // i - Index
            // v - das Tabellenobjekt (Herleitung des Namens?)
            var options = Unitracc.datatables_config(i, v);
            options.data = %(data)s;
            options.columns = %(columns)s;
            options.deferRender = true;
            options.deferLoading = %(result_length)s;
            Unitracc.log(options);
            $(v).dataTable(options);
        }
    );
});
// vim: ts=8 sts=4 sw=4 si et hls
