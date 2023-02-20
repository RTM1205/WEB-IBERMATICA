
(function ($) {
    "use strict";


    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })
    })


    /*==================================================================
    [ Send ]*/
    var URL_POST = "http://xcpm1dldb011.onpremise.es.bs:8000"


    $('.validate-form').on('submit',function(){
        var data = JSON.stringify( $(mform).serializeArray() );
    console.log(URL_POST);
        //$.post( URL_POST, data );
        $.ajax({
        url: URL_POST,
        method: 'POST',
        data: data,
        cache: false,
        success: function(result){
            //if the submit was successful, you redirect
            window.location.href = "thanks.html";
        },
        error: function(){
             //console.log("ERROR")
             window.location.href = "error.html";
        }
    });
    });



})(jQuery);
