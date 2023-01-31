function getInputValue() {
    let inputVal = document.getElementById("inputId").value;
    eel.login(inputVal)(function(bool){					
        if(bool){
            window.location.href = "test.html";
        }
        else{
            window.location.href = "test.html"
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