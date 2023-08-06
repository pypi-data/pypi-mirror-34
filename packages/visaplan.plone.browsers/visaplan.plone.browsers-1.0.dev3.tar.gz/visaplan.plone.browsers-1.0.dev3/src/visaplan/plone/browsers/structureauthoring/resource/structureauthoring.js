var cp=null;
var clickCounter=1001;
var listToOpen=new Array();
var current_after_save=null;
var is_text_iframe_loaded=null;
var se_editing = false,  // Wird gerade etwas bearbeitet?
    se_debug = false;

function save_or_cancel_hint() {
    if (se_editing) {
        tell('save_or_cancel_hint --> Protest!');
        alert('Please save or cancel first!');
        return true;
    } else {
        tell('save_or_cancel_hint: OK');
    }
}

/**
 * Rückfrage vor dem Verlassen des Editors
 * (der Abbrechen-Button funktioniert derzeit nicht korrekt)
 */
function abort_confirm() {
    if (se_editing) {
        tell('abort_confirm ...');
        if (confirm('Möchten Sie Ihre Änderungen verwerfen?')) {
            nuke_editors();
            se_editing = false;
            return true;
        } else {
            return false;
        }
    } else {
        return true;
    }
}

function handleParentClick(element) {
    tell('Aufruf: handleParentClick');

    if (! abort_confirm()) return false;
    handleOverLay(true);
    uid=$(element).attr('id').split('---')[1];
    $('#uid').attr('value', uid);

    $('.parent-click').removeClass('current');

    $(element).addClass('current');
    if (!$('#span---'+uid).hasClass('open')) {
        openTree(uid);
    } else {
        $('#span---'+uid).html('');
        $('#span---'+uid).removeClass('open');

        var regex = /click-..../;
        currentClass=String(regex.exec($('#span---'+uid).attr('class')));
        $('#span---'+uid).removeClass(currentClass);
    }

    $.post('kss-structure-content',
           $("#filter-post").serialize(),
           function (data) {
               $('#kss-structure-content').html(data);
               _V_.autoSetup();
               handleOverLay(false);
           }
    );
}

function openTree(uid) {
    tell('Aufruf: openTree');
    if (! abort_confirm()) return false;
    $.post('kss-presentation-level',
           'uid='+uid,
           function (data) {
               $('#span---'+uid).html(data);
               handleOverLay(false);
               $('#span---'+uid).addClass('open');

               var regex = /click-..../;
               currentClass=String(regex.exec($('#span---'+uid).attr('class')));
               if (!currentClass) {
                   $('#span---'+uid).addClass('click-'+clickCounter);
                   clickCounter=clickCounter+1;
               }
               if (listToOpen.length!=0) {
                   openTree(listToOpen[0]);
                   listToOpen.shift();
               }

               if (current_after_save!=null && $('#'+current_after_save).length) {
                   $('#'+current_after_save).addClass('current');
                   current_after_save=null;
               }
           }
    );
}

handlerParentClick = function () {
    handleParentClick(this);
}

function addParentClickHandler() {
    tell('Aufruf: addParentClickHandler');
    $('.parent-click').live('click', handlerParentClick);
}

function remove_action_menu() {
    tell('Aufruf: remove_action_menu');
    $('#kss-right-click-menu').remove();
}


function handleRightClickMenu(e) {
    tell('Aufruf: handleRightClickMenu');

    div_=$('<div></div>');
    $(div_).attr('id','kss-right-click-menu');

    $('body').append(div_);

    uid=$(e.target).attr('id').split('---')[1];

    $('#kss-right-click-menu').css('top', e.pageY);
    $('#kss-right-click-menu').css('left', e.pageX);
    $('#kss-right-click-menu').show();

    $.post('kss-right-click-menu',
           'uid='+uid,
           function (data) {
               $('#kss-right-click-menu').html(data);
               if (!cp) {
                   $('#right-click-paste-before').hide();
                   $('#right-click-paste-after').hide();
                   $('#right-click-paste-in-folder').hide();
               }
           }
    );
}

function handleAddReturn(data) {
    tell('Aufruf: handleAddReturn');
    $('#kss-structure-content').html(data);
    remove_action_menu();
    $("form.enableFormTabbing, div.enableFormTabbing").each(ploneFormTabbing.initializeForm);
    _V_.autoSetup();
}

function handleRightClickAdd(e, methodId) {
    tell('Aufruf: handleRightClickAdd');
    if (console && console.log) {
        console.log('handleRightClickAdd('+methodId+')');
    }
    handleOverLay(true);
    uid=$(e.target).attr('rel').split('---')[1];
    $.post('resolveUid/'+uid+'/@@structureauthoring/'+methodId,
           'uid='+uid,
           function (data) {
               handleAddReturn(data);
               handleOverLay(false);
           }
    );
}

function handleRightClickAgendaView(e) {
    tell('Aufruf: handleRightClickAgendaView');
    uid=$(e.target).attr('rel').split('---')[1];
    title=$('#parent---'+uid).html()

    dict_={'msgid': 'js_select_agenda_view',
           'uid': uid}

    $.post('@@structureauthoring/titleMappingByUid',
           dict_,
           function (data) {
               complexe=$.parseJSON(data);
               Check = confirm(complexe.message);
               if (Check == false) {
                   return false;
               }

               $.post('resolveUid/'+complexe.uid+'/@@structureauthoring/setAgendaView',
                      '',
                      function (data) {
                          complexe=$.parseJSON(data);
                          uid=complexe.uid;
                          message.show(complexe.message);

                          $('#uid').attr('value', uid);
                          remove_action_menu();
                          rebuildTree();
                      }
               );
           }
    );
}

function handleRightClickSetDefaultPage(e) {
    tell('Aufruf: handleRightClickSetDefaultPage');
    uid=$(e.target).attr('rel').split('---')[1];

    $.post('resolveUid/'+uid+'/@@kss-select-default-page',
           '',
           function (data) {
               handleAddReturn(data);
               rebuildTree();
           }
    );
}

function handleRightClickDelete(e) {
    tell('Aufruf: handleRightClickDelete');
    if (! abort_confirm()) return false;
    uid=$(e.target).attr('rel').split('---')[1];
    title=$('#parent---'+uid).html()

    dict_={'msgid': 'Do you really want to delete "${title}"?',
           'uid': uid}

    $.post('@@structureauthoring/titleMappingByUid',
           dict_,
           function (data) {
               complexe=$.parseJSON(data);
               Check = confirm(complexe.message);
               if (Check == false) {
                   return false;
               }

               $.post('resolveUid/'+complexe.uid+'/@@structureauthoring/delete',
                      '',
                      function (data) {
                          complexe=$.parseJSON(data);
                          uid=complexe.uid;
                          message.show(complexe.message);

                          $('#uid').attr('value', uid);
                          remove_action_menu();
                          rebuildTree();
                      }
               );
           }
    );
}

function handleRightClickCut(e) {
    tell('Aufruf: handleRightClickCut');
    uid=$(e.target).attr('rel').split('---')[1];

    $('.italic').removeClass('italic');
    $('#parent---'+uid).addClass('italic');

    $.post('@@structureauthoring/cut',
           'uid='+uid,
           function (data) {
               complexe=$.parseJSON(data);
               cp=complexe.cp;
               message.show(complexe.message);
               remove_action_menu();
           }
    );
}

function sortClickFunction(a, b) {
    tell('Aufruf: sortClickFunction');
    var regex = /click-..../;
    currentClass=String(regex.exec($('#span---'+uid).attr('class')));

   var compA = String(regex.exec($(a).attr('class')));
   var compB = String(regex.exec($(b).attr('class')));
   return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
}

function handleRightClickCopy(e) {
    tell('Aufruf: handleRightClickCopy');
    uid=$(e.target).attr('rel').split('---')[1];

    $('.italic').removeClass('italic');
    $('#parent---'+uid).addClass('italic');

    $.post('@@structureauthoring/copy',
           'uid='+uid,
           function (data) {
               complexe=$.parseJSON(data);
               cp=complexe.cp;
               message.show(complexe.message);
               remove_action_menu();
           }
    );
}

/**
 * CKEditor-Instanzen nach Gebrauch zerstoeren
 */
function nuke_editors() {
    tell('Aufruf: nuke_editors');
    if (CKEDITOR.instances) {
        for (var name in CKEDITOR.instances) {
            CKEDITOR.instances[name].destroy();
        }
    }
}

/**
 * txt - Text, oder auch ein Objekt - was console.log so alles ausgibt
 */
function tell(txt) {
    if (! se_debug) {
        return;
    }
    if (window.console && console.log) {
        var now = new Date(),
            time = [now.getHours(), now.getMinutes(), now.getSeconds()],
            i;
        for (i = 1; i < time.length; i++) {
            if (time[i] < 10) {
                time[i] = '0'+time[i];
            }
        }
        console.log(time.join(':')+' '+txt);
    }
}

function copy_value_from_editor(name) {
    tell('Aufruf: copy_value_from_editor');
    var selector = '#'+name;
    if ($(selector).length) {  // Anzahl gefundener Objekte != 0
        if (CKEDITOR.instances && CKEDITOR.instances[name]) {
            $(selector).attr('value', CKEDITOR.instances[name].getData());
        }
    }
}


function saveForm(e) {
    tell('Aufruf: saveForm');
    copy_value_from_editor('text');
    copy_value_from_editor('notes');
    current_after_save=$('.current').attr('id');

    $.post('@@structureauthoring/save',
           $("#edit-form").serialize(),
           function (data) {    // Success-Funktion
               $('#uid').attr('value', data);
               remove_action_menu();
               rebuildTree();

               $.post('kss-structure-content',
                      'uid='+data,
                      function (data) {
                          $('#kss-structure-content').html(data);
                          _V_.autoSetup();
                          handleOverLay(false);
                          $('body').addClass('structureInlineInActive');

                      }
               );
           }
    );

    nuke_editors();
    se_editing = false;
}

function cancel_form(event) {
    tell('Aufruf: cancel_form');

    $.post('@@structureauthoring/cancel',
           $("#edit-form").serialize(),
           function (data) {    // Success-Funktion
               remove_action_menu();
               rebuildTree();
               $.post('kss-structure-content',
                      'uid='+data,
                      function (data) {
                          $('#kss-structure-content').html(data);
                          _V_.autoSetup();
                          handleOverLay(false);
                      }
               );
           }
    );
    // nuke_editors();  // TH: warum nicht?
    se_editing = false;
}

function setDefaultPage(e) {
    tell('Aufruf: setDefaultPage');

    $.post('@@structureauthoring/setDefaultPage',
           $("#edit-form").serialize(),
           function (data) {
               complexe=$.parseJSON(data);
               message.show(complexe.message);
               handleAddReturn(complexe.html);
               rebuildTree();
           }
    );
}


function handleRightClickPaste(e, methodId) {
    tell('Aufruf: handleRightClickPaste');
    uid=$(e.target).attr('rel').split('---')[1];

    dict_={'cp': cp,
          'uid': uid}

    $.post('@@structureauthoring/'+methodId,
           dict_,
           function (data) {
               complexe=$.parseJSON(data);
               message.show(complexe.message);
               remove_action_menu();
               rebuildTree();
               cp=null;
           }
    );
}

function load_editor(event, uid) {
    tell('Aufruf: load_editor');
    if (! abort_confirm()) return false;
    dict_={'uid': uid}
    nuke_editors();
    se_editing = true;
    $.post('@@structureauthoring/edit',
           dict_,
           function (data) {
               complexe=$.parseJSON(data);
               remove_action_menu();
               $('#kss-structure-content').html(complexe.html);
               $("form.enableFormTabbing, div.enableFormTabbing").each(ploneFormTabbing.initializeForm);
               setTimeout("launchCKInstances()", 100);
           }
    );
}

function rebuildTree() {
    tell('Aufruf: rebuildTree');
    var list_=$('.open');
    list_.sort(sortClickFunction)
    $.each(list_, function (index, value) {
        var uid=$(value).attr('id').split('---')[1];
        listToOpen.push(uid)
        }
    );
    openTree(listToOpen[0]);
    listToOpen.shift()
}

$(document).ready(function () {
        window.focus();
        addParentClickHandler();

        $(document).bind("contextmenu", function (e) {
            return false;
        });

        $('.parent-click').live('mousedown', function (e) {
            if (e.button == 2) {
                handleRightClickMenu(e);
                return false;
            }
            return true;
        });

        /* Ein Klick neben das aufgepoppte Menü
         * schließt es mit einer kleinen Verzögerung
         */
        $(document).bind('mousedown', function (e) {
            if (e.button == 0) {
                setTimeout(function () {
                    $('#kss-right-click-menu').hide()
                }, 300);
            }
        });

        $('#right-click-add-slide').live("click", function (e) {
            tell('Element #right-click-add-slide::click')
            handleRightClickAdd(e, 'addSlide');
        });

        $('#right-click-add-slide-before').live("click", function (e) {
            tell('Element #right-click-add-slide-before::click')
            handleRightClickAdd(e, 'addSlideBefore');
        });

        $('#right-click-add-slide-after').live("click", function (e) {
            tell('Element #right-click-add-slide-after::click')
            handleRightClickAdd(e, 'addSlideAfter');
        });

        $('#right-click-add-page').live("click", function (e) {
            tell('Element #right-click-add-page::click')
            handleRightClickAdd(e, 'addPage');
        });

        $('#right-click-add-page-before').live("click", function (e) {
            tell('Element #right-click-add-page-before::click')
            handleRightClickAdd(e, 'addPageBefore');
        });

        $('#right-click-add-page-after').live("click", function (e) {
            tell('Element #right-click-add-page-after::click')
            handleRightClickAdd(e, 'addPageAfter');
        });

        $('#right-click-add-presentation-folder').live("click", function (e) {
            tell('Element #right-click-add-presentation-folder::click')
            handleRightClickAdd(e, 'addPresentationFolder');
        });

        $('#right-click-add-presentation-folder-before').live("click", function (e) {
            tell('Element #right-click-add-presentation-folder-before::click')
            handleRightClickAdd(e, 'addPresentationFolderBefore');
        });

        $('#right-click-add-presentation-folder-after').live("click", function (e) {
            tell('Element #right-click-add-presentation-folder-after::click')
            handleRightClickAdd(e, 'addPresentationFolderAfter');
        });

        $('#right-click-add-structure-folder-before').live("click", function (e) {
            tell('Element #right-click-add-structure-folder-before::click')
            handleRightClickAdd(e, 'addStructureFolderBefore');
        });

        $('#right-click-add-structure-folder').live("click", function (e) {
            tell('Element #right-click-add-structure-folder::click')
            handleRightClickAdd(e, 'addStructureFolder');
        });

        $('#right-click-add-structure-folder-after').live("click", function (e) {
            tell('Element #right-click-add-structure-folder-after::click')
            handleRightClickAdd(e, 'addStructureFolderAfter');
        });

        $('#right-click-paste-before').live("click", function (e) {
            tell('Element #right-click-paste-before::click')
            handleRightClickPaste(e, 'pasteBefore');
        });

        $('#right-click-paste-after').live("click", function (e) {
            tell('Element #right-click-paste-after::click')
            handleRightClickPaste(e, 'pasteAfter');
        });

        $('#right-click-paste-in-folder').live("click", function (e) {
            tell('Element #right-click-paste-in-folder::click')
            handleRightClickPaste(e, 'pasteInFolder');
        });

        $('#right-click-cut').live("click", function (e) {
            tell('Element #right-click-cut::click')
            handleRightClickCut(e);
        });

        $('#right-click-copy').live("click", function (e) {
            tell('Element #right-click-copy::click')
            handleRightClickCopy(e);
        });

        $('#right-click-delete').live("click", function (e) {
            tell('Element #right-click-delete::click')
            handleRightClickDelete(e);
        });

        $('#save-edit').live("click", function (e) {
            tell('Element #save-edit::click')
            saveForm(e);
        });

        $('#save-cancel').live("click", function (event) {
            tell('Element #save-cancel::click')
            cancel_form(event);
        });

        $('#save-default-page').live("click", function (e) {
            tell('Element #save-default-page::click')
            setDefaultPage(e);
        });


        $('#right-click-set-agenda-view').live("click", function (e) {
            tell('Element #right-click-set-agenda-view::click')
            handleRightClickAgendaView(e);
        });

        $('#right-click-set-default-page').live("click", function (e) {
            tell('Element #right-click-set-default-page::click')
            handleRightClickSetDefaultPage(e);
        });

        $('#right-click-edit-structure-folder').live("click", function (e) {
            tell('Element #right-click-edit-structure-folder::click')
            handleRightClickAdd(e, 'editFolder');
        });

        $('#right-click-edit-structure-page').live("click", function (event) {
            tell('Element #right-click-edit-structure-page::click')
            load_editor(event, $(event.target).attr('rel').split('---')[1]);
        });
    }
);
