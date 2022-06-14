    var email;
    var pass;
    
    $("#btn_acceder").click(function(){
        email = $("#email").val();
        pass = $("#password").val();
        //console.log(email + ' '+ pass);
        validar_acceso_v2(email, pass);
    });


    //funcion normal
    function validar_acceso_v1(_email, _pass){
        if (_email == 'ernestoleonidas@gmail.com' && _pass == '123') {
            console.log('SI');
        } else {
            console.log('NO');
        }
    }

    //funcion de flecha
    validar_acceso_v2 = (_email, _pass) => {
        if (_email == 'ernestoleonidas@gmail.com' && _pass == '123') {
            console.log('SI');
            $(location).attr('href','dashboard.html');
        } else {
            console.log('NO');
        }
    }

    $("#btn_limpiar").click(function(){
        $("#email").val('');
        $("#password").val('');
    });