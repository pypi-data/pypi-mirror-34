var lesson_counter=0;
var lesson_info={};

function handle_post(template_id, identifier, form_) {
    $.post(template_id,
           form_,
           function (data){
               $(identifier).html(data);
               handle_sortable();
           }
    ).error(function (result) {
	result.error();
    });
}

function handle_course_browse_button(form_) {
    handle_post('js-coursemanagement-browse','.coursemanagement-detail',form_);
}

function handle_sortable() {
    $( ".connectedSortable" ).sortable({
        connectWith: ".connectedSortable"
    }).disableSelection();
}

function create_lesson() {
    $('.coursemanagement-detail').hide();
    $('.coursemanagement-item-edit').show();
    dict_={}
    dict_['uid']=lesson_counter+1;
    //1=create,2=edit
    dict_['status']='1';

    $.post('js-coursemanagement-lesson-edit',
        dict_,
            function (data){
                $('.coursemanagement-item-edit').html(data);
            }
    ).error(function () {});

}

function edit_lesson(uid) {
    $('.coursemanagement-detail').hide();
    $('.coursemanagement-item-edit').show();
    dict_={}
    //1=create,2=edit
    dict_['status']='2';

    for(var name_ in lesson_info[uid]) {
        dict_[name_]=lesson_info[uid][name_];
    }

    $.post('js-coursemanagement-lesson-edit',
        dict_,
            function (data){
                $('.coursemanagement-item-edit').html(data);
                handle_menu_container(false);
            }
    ).error(function () {handle_menu_container(false);});

}

function set_lesson() {
    dict_={}
    $($('.course-edit-form').serializeArray()).each(function (index) {
        dict_[$(this).attr('name')]=$(this).attr('value');
    });
    lesson_info[$(".course-edit-form input[name='uid']").attr('value')]=dict_;

    lesson_counter=lesson_counter+1;
    $.post('js-coursemanagement-lesson',
        lesson_info[$(".course-edit-form input[name='uid']").attr('value')],
            function (data){
                $(data).insertBefore('.course-end');
                $('.coursemanagement-detail').show();
                $('.coursemanagement-item-edit').hide();
                handle_sortable();
            }
    ).error(function () {});
}

function save_lesson() {
    title_=$(".course-edit-form input[name='title']").attr('value');
    uid=$(".course-edit-form input[name='uid']").attr('value');

    $("#lesson-title-"+uid).html(title_);

    dict_={}
    $($('.course-edit-form').serializeArray()).each(function (index) {
        dict_[$(this).attr('name')]=$(this).attr('value');
    });
    lesson_info[$(".course-edit-form input[name='uid']").attr('value')]=dict_;
    $('.coursemanagement-detail').show();
    $('.coursemanagement-item-edit').hide();
}

function save_course() {
    var xml_=$.course_xml();
    var inputs_=$('.coursemanagement-edit .one input');
    $('.coursemanagement-edit .one input').each(function (index) {
        if ($(this).attr('rel')=='UnitraccLesson') {
            parent_uid_value='';
            next_uid_value=$(inputs_[index+1]).attr('value');
            if (index==0) {
                prev_uid_value='';
            } else {
                prev_uid_value=$(inputs_[index-1]).attr('value');
            }
        } else {
            parent_uid_value=$(this).parents('li').parents('li').children('input').attr('value');
            prev_uid_value=$(inputs_[index-1]).attr('value');
            if (index+1!=inputs_.length) {
                next_uid_value=$(inputs_[index+1]).attr('value');
            } else {
                next_uid_value='';
            }
        }

        object_uid_value=$(this).attr('value');
        var dict_={uid_object:object_uid_value,
                   uid_parent:parent_uid_value,
                   uid_prev:prev_uid_value,
                   uid_next:next_uid_value}
        if ($(this).attr('checked') == 'checked') {
            xml_.add(dict_);

            xml_.set_property(object_uid_value,'portal_type',$(this).attr('rel'));
        }


    });

    for(var index in lesson_info) {
        for(var name_ in lesson_info[index]) {
            xml_.set_property(index,name_,lesson_info[index][name_]);
        }
    }

    dict_={}
    dict_['xml']=$(xml_.xml).html();
    dict_['html_left']=$('.coursemanagement-edit .one').html();
    dict_['html_right']=$('.coursemanagement-edit .two').html();

    $.post($('base').attr('href')+'/@@unitracccourse/set',
        dict_,
            function (data) {
                alert('Changes saved.');
            }
    ).error(function () {alert('Not saved! An error occured.')});

}

function load_course() {
    $.post($('base').attr('href')+'/@@unitracccourse/load',
        '',
        function (data){
            complexe=$.parseJSON(data);

            if (complexe.html_right){
                $('.coursemanagement-edit .two').html(complexe.html_right);
            }

            $.post($('base').attr('href')+'/unitracccourse_html_left',
                '',
                    function (data){
                        $('.coursemanagement-edit .one').html(data);

                        elements_=$('.lesson-checkbox');
                        counter_=$(elements_[$('.lesson-checkbox').length-1]).attr('value');
                        lesson_counter=parseInt(counter_);
                        handle_sortable();
                        $('.coursemanagement-edit .one .lesson-checkbox').each(function (index) {
                            dict_={}
                            uid=$(this).attr('value');
                            $($('#'+uid+' > properties',complexe.xml).children()).each(function (index) {
                                dict_[this.localName]=$(this).html();
                            });
                            lesson_info[parseInt(uid)]=dict_;
                        });

                    }
            ).error(function () {alert('An error occured.')});
        }
    ).error(function () {});

}

function handle_menu_container(show, element) {
    if (show==true) {
        $('body').append('<div id="course-edit-menu"></div>');

        $('#course-edit-menu').css('top',element.pageY);
        $('#course-edit-menu').css('left',element.pageX);
    } else {
        $('#course-edit-menu').remove();
    }
}

function load_lesson_actions(event) {
    input_=$('> input',$(event.target).parent());


    uid=$(input_).attr('value');


    dict_={}
    dict_['uid']=uid

    if ($('#course-edit-menu').html()) {
        handle_menu_container(false, event);
        $('#course-edit-menu').hide();
    }else{
        handle_menu_container(true, event);
        $.post('js-lesson-edit-menu',
            dict_,
                function (data){
                    $('#course-edit-menu').html(data);
                    $('#course-edit-menu').show();
                }
        ).error(function () {});
    }
}


$(document).ready(
    function () {
        $('.coursemanagement-browse-button').live("click", function (event) {
            $('.coursemanagement-item-edit').hide();
            $('.coursemanagement-detail').show();
            handle_course_browse_button('');
        });

        $( "body" ).delegate( "td", "click", function (event) {
            create_lesson();
        });
        $('.coursemanagement-create-lesson').live("click", function (event) {
            create_lesson();
        });
        $('.button-lesson-create').live("click", function (event) {
            set_lesson();
        });

        $('.coursemanagement-load-button').live("click", function (event) {
            load_course();
        });

        $('.actionicon-lesson').live("click", function (event) {
            load_lesson_actions(event);
        });

        $('.lesson-edit-click').live("click", function (event) {
            event.preventDefault();
            uid=$(event.target).attr('id').split('-')[1];
            edit_lesson(uid);
        });

        $('.button-lesson-edit').live("click", function (event) {
            save_lesson();
        });

        $('.lesson-remove-click').live("click", function (event) {
            event.preventDefault();
            uid=$(event.target).attr('id').split('-')[1];
            $('#lesson-'+uid).remove();
            handle_menu_container(false);
        });

        $( "body" ).delegate( ".coursemanagement-save-button", "click", function () {
            save_course();
        });

        $('.folderish-browser').live("click", function (event) {
            event.preventDefault();
            dict_={}
            dict_['uid']=$(event.target).attr('id').split('-')[1];
            handle_course_browse_button(dict_);
        });

        $('.content-open').live("click", function (event) {
            event.preventDefault();
            uid=$(event.target).attr('id').split('-')[1];

            if ($(event.target).hasClass('tree-open')) {
                $(event.target).removeClass('tree-open')

                //close tree
                $('#div-'+uid).html('');

            } else {
                $(event.target).addClass('tree-open');

                //open tree
                dict_={}
                dict_['uid']=uid;
                handle_post('js-coursemanagement-level','#div-'+uid,dict_);

            }
        });

        $('.content-checkbox').live("click", function (event) {
            parent=$(event.target).parent();
            uid=$(parent).attr('id').split('-')[1];
            if ($(event.target).attr('checked') == 'checked') {
                $('#div-'+uid+' input').attr('checked',true);
                $(event.target).attr('checked',true);
            } else {
                $('#div-'+uid+' input').attr('checked',false);
                $(event.target).attr('checked',false);
            }
        });
});
