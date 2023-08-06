// Label fuer Radio-Buttons *ohne* Aktivierung:
$(document).ready(function () {
    $('label.for-next-input').click(function () {
        $(this).next().find('input').first().focus();
        return False;
        });
    });
