function login(user,pass) {
    $.ajax
    ({
        url: "http://127.0.0.1:5000/login",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'username': user,
            'password': pass
        }),
        type: "POST",
        dataType: "json",
        error: function (e) {
        },
        success: function (resp) {
            console.log(resp.status)
            if (resp.status === 'error'){
                alert("Invalid username or pass");
            }
            else {
                window.location.replace('/dashboard');
            }
        }
    });
}

function validate() {
    const user = $('input#user1').val();
    $.ajax
    ({
        url: "http://localhost:8080/validate",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'username': user
        }),
        type: "POST",
        dataType: "json",
        error: function (e) {
        },
        success: function (resp) {
            if (resp.status === 'exist'){
                console.log("Username is currently in use");
            }
            else {
                console.log("Username is available");
            }
        }
    });
}

$(document).on('keypress', '#pass1', function(e) {
    if (e.keyCode === 13) {
        $('button#mylogin').click();
    }
});

$(document).on('click', '#mylogin', function(){
    var username = $('input#user1').val();
    var password = $('input#pass1').val();
    login(username,password);
});

$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});