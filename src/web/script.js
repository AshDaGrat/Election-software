function getInputValue() {
    let inputVal = document.getElementById("inputId").value;
    eel.login(inputVal)(function(e){					
        if(e == 3){
            window.location.href = "forms/1.html";
        }
        if(e == 2){
            alert("Invalid USN/Employee Number");
        }
        if(e == 1){
            alert("Already Voted");
        }
    })
}

/*
document.querySelector("button").onclick = function () {
    // Call python's random_python function
    eel.random_python()(function(number){					
        // Update the div with a random number returned by python
        document.querySelector(".random_number").innerHTML = number;
    })
    }
*/