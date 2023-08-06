(function($){

var CourseXml = function(){
    this._class  = CourseXml;
    this.xml=$('<'+'root'+'>');
    this._last=null;

}

CourseXml.fn = CourseXml.prototype;

CourseXml.fn.add = function(struct_){

    element_=$('<'+'element'+'>');

    $(element_).attr('id',struct_['uid_object']);

    for(var name_ in struct_) {
        property_=$('<'+name_+'>');
        $(property_).html(struct_[name_]);
        $(element_).append(property_);
    }

    property_=$('<'+'children'+'>');
    $(element_).append(property_);

    property_=$('<'+'properties'+'>');
    $(element_).append(property_);

    if (struct_['uid_parent']=='') {
        $(this.xml).append(element_);
    } else {
        container_=$('#'+struct_['uid_parent']+' > children',this.xml);
        container_.append(element_);
    }

    this._last=element_;
};

CourseXml.fn.set_property = function(id,key,value){

    if ($('#'+id,this.xml).length==0) {
        alert('Element not found.');
        return null;
    }

    if ($('#'+id+' > properties > '+key,this.xml).length==0) {
        element_=$('#'+id+' > properties',this.xml);
        property_=$('<'+key+'>');
        $(property_).html(value);
        $(element_).append(property_);
    } else {
        $('#'+id+' > properties > '+key,this.xml).html(value)
    }

};

$.course_xml = function(options, callback){
  return(new CourseXml());
};

$.test_course_xml = function(options, callback){
    var xml_=new CourseXml();
    xml_.add({uid_object:'uid_object',
              uid_parent:'uid_parent',
              uid_next:'uid_next',
              uid_prev:'uid_prev'
              });
    xml_.add({uid_object:'uid_object1',
              uid_parent:'uid_parent1',
              uid_next:'uid_next1',
              uid_prev:'uid_prev1'
              });

    xml_.set_property('uid_object','portal_type','Document');
    xml_.set_property('uid_object1','portal_type','UnitraccLesson');

};

})(jQuery);