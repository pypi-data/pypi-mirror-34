// -*- coding: utf-8 -*- vim: et ts=4 sts=4
// Achtung: Synchron halten und perspektivisch zusammenführen
// mit ./course_ppt_view.js!
function LOG(txt) {
    if (console && console.log) {
        console.log(txt);
    }
    return;
    var logdiv = $('div#log');
    if (logdiv) {
        $('<p>').append(txt).appendTo(logdiv);
    }
}

function handle_page_links() {

    // TODO: kommentieren!
    if ($('.no-page-link-confirm').length) {
        return false;
    }

    $('.course-page-content a').each(function (index) {
        attach_ = true;
        if ($(this).hasClass('content-only') || $(this).hasClass('no-page-confirm')) {
            attach_ = false;
        }

        if ($(this).html().indexOf('<'+'img') != -1) {
            attach_ = false;
        }

        if (attach_ == true) {
            $(this).addClass('course-page-link-confirm');
        }

    });

    // TODO: kommentieren!
    $('.course-page-content .question-hints a').each(function (index) {
        $(this).removeClass('course-page-link-confirm');
    });

    $('.course-page-link-confirm').click(function (event) {
        $(this).removeClass('course-page-link-confirm')
        value_ = confirm('Do you really want to leave this site?');
        if (value_ == true) {
            return true;
        } else {
            event.preventDefault();
            return false;
        }
        return false;
    });
}

function handle_page_switch(dict_) {
    handleOverLay(true);
    $.post($('base').attr('href')+'/js-course-content',
            dict_,
            function (data) {
                $('.area-content>.row').html(data);
                _V_.autoSetup();
                handleOverLay(false);
                handle_page_links();
            }
    ).done(function () {
        if (typeof qs_init !== 'undefined' && $.isFunction(qs_init)) {
            qs_init();
        }
    }
    ).error(function () {
        handleOverLay(false);
    });
}

function handle_navigation(dict_) {
    $.post($('base').attr('href')+'/js-course-navigation',
            dict_,
            function (data) {
                $('#course-navigation').html(data);
            }
    );
}

var loaded = false;
window.onpopstate = function (event) {
    // Workaround für Chrome, da Chrome das onpopstate-Event sofort triggert
    // (trotz neuer HTML-5-history-Unterstützung)
    if (loaded) {
        LOG('course_view.js: window.location.href = location.href;')
        window.location.href = location.href;
    }
};

$(document).ready(
    function () {
        $('.nav-tabs a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
        });

        $('.course-nav-link').live("click", function (event) {
            event.preventDefault();
            LOG('.course-nav-link--live:click ...')
            LOG(event)
            LOG('nodeName = '+$(event.target).prop("nodeName"))

            if ($(event.target).prop("nodeName")=='I') {
                target = $(event.target).parent();
            } else {
                target = $(event.target);
            }
            uid = target.attr('rel').split('-')[1];
            url = target.attr('href');
            manage_history(url);
            dict_ = {}
            dict_['uid'] = uid;
            dict_['next'] = $(target).attr('next');
            dict_['previous'] = $(target).attr('prev');
            handle_navigation(dict_);
            handleOverLay(true);
            $.post($('base').attr('href')+'/js-course-content',
                    dict_,
                    function (data) {
                        $('.area-content>.row').html(data);
                        _V_.autoSetup();
                        handleOverLay(false);
                        handle_page_links();
                    }
            ).done(function () {
                if (typeof qs_init !== 'undefined' && $.isFunction(qs_init)) {
                    qs_init();
                }
            }).error(function () {
                handleOverLay(false);
            });
            LOG('... .course-nav-link--live:click')
        });
}); // ... $(document).ready

function manage_history(uri) {
    var value = "";
    if (uri.split("=").length > 1) {
        value = uri.split("=")[1];
    }

    if (window.history.pushState) {
        title = document.title;
        stateObj = {'uid': value};
        window.history.pushState(stateObj, title, uri);
        loaded = true;
    }
}

function go_to_page() {
    var url = $('#form_go_to').attr('action'),
        data = {'page': $('#goto').val(),
                'uid':  $('#cuid').val(),
                'ajax': true,
                };
    $.post(url, data,
           function (response) {
               uid = $.parseJSON(response)['uid'];
               url = document.URL.split("?")[0];
               url = url+"?uid="+uid;
               $('#learningprogress').data('tooltipsy').hide();
               manage_history(url);
               dict_ = {'uid': uid};
               handle_navigation(dict_);
               handle_page_switch(dict_);
           });
}
