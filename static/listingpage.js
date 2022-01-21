function mark(id){
    fetch("mark/"+id).then(function(data){
        data.json().then(function (json) {
          $("#markatnd").addClass('d-none');
         window.location.reload();
});
    });
  }

  $(window).on('load', function(){
    setTimeout(removeLoader, 500); //wait for page load PLUS two seconds.
  });
  function removeLoader(){
      $( "#spin" ).fadeOut(500, function() {
        // fadeOut complete. Remove the loading div
        $( "#spin" ).remove(); //makes page more lightweight 
    });  
  }

// async function spin(time){
//   setTimeout(() => {
//     $("#spin").removeClass('d-none');
//   }, time);
 
// }
