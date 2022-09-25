function hideShowPassword(){
    if($("#create-account").is(':checked')){
        $("#login-password1").prop('required', true);
        $("#login-password2").prop('required', true);  // checked
    }                
    else{
        $("#login-password1").prop('required', false);  // unchecked
        $("#login-password2").prop('required', false);
    } 
}

function validateForm(){
    username = $('#username').val();
    //username = document.getElementById('username').value;
    console.log(ValidateEmail(username))
    console.log(isNumeric(username))
    if (ValidateEmail(username) == true || isNumeric(username) == true){
        return (true)
    }else{
        alert('Please enter valid Username')
        return (false)
    }
}

function ValidateEmail(mail) {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (mail.match(validRegex))
    {
        return (true)
    }
        return (false)
    }

function isNumeric(num){
    return !isNaN(num)
    }

function LoginClicked(){
    username = $('#username').val();
    if (ValidateEmail(username) == true || isNumeric(username) == true){
        password = $('#login-password').val();
        $.ajax({
            method: "POST",
            url: "/login/",
            data: {'username':username,'password':password},
            success: function (response) {
            if (response.message == "required"){
                $("#username").prop('disabled', true);
                $('#pswdiv').css("display", "block");
                $("#login-password").prop('required', true);
            }
            else if(response.message == "ok"){
                location.replace("/")
            }
            else{
                $('.loginbtn').removeClass('mt-1');
                $('#alert-error').css("display", "block");
                $('#error-message').text(" "+response.message)
                setTimeout(
                    $('#alert-error').css("display", "none")
                ,5000);
                $('.loginbtn').addClass('mt-1');
            }
        }
        })
    }else{
        alert('Please enter valid Username')
    }
}