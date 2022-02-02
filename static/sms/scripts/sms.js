var check=$('#selectall').click(function(){
    $("#user*").prop('checked',$(this).prop('checked'))
    
})
var lst=[]
$("#smsbtn").click(function(){
    if($("#user").prop('checked')){
        lst.push($( "#user:" ).each(function() {
            return $( this ).val();
          }))
    }else{
    alert($("textarea").val())
    }
    alert(lst)
})

