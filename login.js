const button = document.querySelector("button");

button.addEventListener("click",function(){

    const username=document.querySelector("input[type='text']").value;

    const password=document.querySelector("input[type='password']").value;

    const error=document.getElementById("error");

    error.innerHTML="";

    if(username===""){

        error.innerHTML="Username Required";

        return;

    }

    if(password===""){

        error.innerHTML="Password Required";

        return;

    }

    alert("Login Successful");

});