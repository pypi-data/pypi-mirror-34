// -*- coding: utf-8 -*- vim: et ts=4 sts=4
// Achtung: Synchron halten und perspektivisch zusammenführen
// mit ./course_view.js!
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

    // diese Tooltips gibt es bisher nur in der Präsentationsansicht:
    handle_tooltips();
    $('.course-page-content a').each(function (index) {
        attach_ = true;
        if ($(this).hasClass('content-only')) {
            attach_ = false;
        }

        if ($(this).html().indexOf('<'+'img') != -1) {
            attach_ = false;
        }

        if (attach_ == true) {
            $(this).addClass('course-page-link-confirm');
        }

    });

    var tmp_selector = '.transformed-booklink';
    $('.course-page-link-confirm').live("click", function (event) {
        value_ = confirm('Really?');
        if (value_ == true) {
            return true;
        } else {
            return false;
        }
    });
}

function handle_page_switch(dict_) {
    togglevalue = $("#toggle").css('display');
    $.post($('base').attr('href')+'/js-presentation-page',
            dict_,
            function (data) {
                $('.js-course-content').html(data);
                $("#toggle").css('display', togglevalue);
                //_V_.autoSetup();
                handle_page_links(); // Auswertungs-Buttons fuer Frageboegen
                zz_spin(false);
            }
    ).done(function () {
        if (typeof qs_init !== 'undefined' && $.isFunction(qs_init)) {
            qs_init();
        }
    }
    ).error(function () {
        zz_spin(false);
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
        LOG('DONT: window.location.href = location.href;')
        // window.location.href = location.href;
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

            if ($(event.target).prop("nodeName") == 'IMG') {
                target = $(event.target).parent();
            } else {
                target = $(event.target);
            }
            uid = $(target).attr('rel').split('-')[1];

            togglevalue = $("#toggle").css('display');
            url = $(target).attr('href');
            manage_history(url);
            dict_ = {};
            dict_['uid'] = uid;
            dict_['next'] = $(target).attr('next');
            dict_['previous'] = $(target).attr('prev');
            zz_spin(true);
            $.post($('base').attr('href')+'/js-presentation-page',
                    dict_,
                    function (data) {
                        $('.js-course-content').html(data);
                        $("#toggle").css('display', togglevalue);
                        //_V_.autoSetup();
                        zz_spin(false);
                        handle_page_links();
                        handle_navigation(dict_);
                    }
            ).done(function () {
                if (typeof qs_init !== 'undefined' && $.isFunction(qs_init)) {
                    qs_init();
                }
            }).error(function () {
                zz_spin(false);
            });
            LOG('... .course-nav-link--live:click')
        });

    $('.course-ppt-page').live("click", function (event) {
        event.preventDefault();
        zz_spin(true);
        if ($(event.target).prop("nodeName") == 'IMG') {
            target = $(event.target).parent();
        } else {
            target = $(event.target);
        }
        uid = $(target).attr('rel').split('-')[1];
        url = $(target).attr('href');
        manage_history(url);
        dict_ = {};
        dict_['uid'] = uid;
        dict_['next'] = $(target).attr('next');
        dict_['previous'] = $(target).attr('prev');
        handle_navigation(dict_);
        handle_page_switch(dict_);
    });

    $('.presentation-galleries').live("click", function (event) {
        event.preventDefault();
        if ($(event.target).hasClass('active')) {
            $(event.target).removeClass('active');
            target = $(event.target).parent();
            dict_ = {};
            dict_['uid'] = $(target).attr('rel').split("-")[1];
            dict_['next'] = $(target).attr('next');
            dict_['previous'] = $(target).attr('prev');
            handle_navigation(dict_);
            handle_page_switch(dict_);
        } else {
            $.post($('base').attr('href')+'/js-presentation-galleries',
                    'uid='+$(event.target).attr('rel'),
                    function (data) {
                        $(event.target).addClass('active');
                        $("#kss-presentation-content").html(data);
                        $("form.enableFormTabbing, div.enableFormTabbing")
                            .each(ploneFormTabbing.initializeForm);
                        $("dl.enableFormTabbing").each(ploneFormTabbing.initializeDL);
                        //_V_.autoSetup();
                    }
            );
        }
    });

    $('#kss-slides .background-arrow-left').live("click", function (e) {
        e.preventDefault();
        $.post($('base').attr('href')+'/js-presentation-slides',
                $(e.target).attr('href').split("?")[1],
                function (data) {
                    $("#kss-slides").html(data);
                }
        );
    });


    $('#kss-slides .pager a, #kss-slides .background-arrow-left, #kss-slides .background-arrow-right'
       ).live("click", function (e) {
        e.preventDefault();
        $.post($('base').attr('href')+'/js-presentation-slides',
                $(e.target).attr('href').split("?")[1],
                function (data) {
                    $("#kss-slides").html(data);
                }
        );
    });

    $('#kss-gallery .background-arrow-right, #kss-gallery .background-arrow-left, #kss-gallery .background-arrow-right'
       ).live("click", function (e) {
        e.preventDefault();
        $.post($('base').attr('href')+'/js-presentation-gallery',
                $(e.target).attr('href').split("?")[1],
                function (data) {
                    $("#kss-gallery").html(data);
                }
        );
    });

    $('#kss-gallery .pager a'
       ).live("click", function (e) {
        e.preventDefault();
        $.post($('base').attr('href')+'/js-presentation-gallery',
                $(e.target).attr('href').split("?")[1],
                function (data) {
                    $("#kss-gallery").html(data);
                }
        );
    });

    handle_tooltips();
    $('#kss-spinner').css('display', 'none');
}); // ... $(document).ready

function zz_spin(show) {
    return true;
    if (show) {
        $('#ajax-spinner').css('display', 'block');
    } else {
        $('#ajax-spinner').css('display', 'none');
    }
    return true;
}

function handle_tooltips() {
    $('[data-tooltipid]').each(function () {
        var ttid = $(this).data('tooltipid');
        $(this).qtip({
            content: {
                text: $('#'+ttid).html(),
            },
            position: {
                my: 'top left',
                at: 'bottom left',
                target: $(this)
            }
        }).removeAttr('href').removeAttr('onclick');
    });
}


function table_of_content() {
    if ($('#toggle').css('display') == 'none') {
        $('#toggle').show('slide',
                           {'direction': 'right'},
                           1000);

    } else {
        $('#toggle').hide('slide',
                           {'direction': 'right'},
                           1000);
    }
}

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
               var resp = $.parseJSON(response);
               if (resp) {
                   var uid = resp['uid'];
                   var url = document.URL.split("?")[0];
                   $('#learningprogress').data('tooltipsy').hide();
                   url = url+"?uid="+uid;
                   manage_history(url);
                   handle_page_switch({'uid': uid});
               }
           });
}
