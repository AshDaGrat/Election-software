function getInputValue() {
    let inputVal = document.getElementById("inputId").value;
    eel.login(inputVal)(function(e){			
        console.log(e)		
        if(e == 3){
            window.location.href = "forms/disc.html";
            eel.votingDict('USN', inputVal);
        }
        if(e == 2){
            alert("Invalid USN/Employee Number");
        }
        if(e == 1){
            alert("Already Voted");
        }
    })
}

function getSelectedOption() {

    var options = document.getElementsByName('options');
    var value = ""
    for (var i = 0; i < options.length; i++) {
        if (options[i].checked) {
            value = options[i].value;
        }
    }

    if (window.location.href == 'http://localhost:8000/forms/wannavote.html'){
        eel.wannaVote(value)(function(e){
            if(e == 0){
                if (confirm('Are you sure you want to forfeit?')) {
                eel.forfeit()
                window.location.href = 'thanks-forfeit.html'}
            }
            if(e == 1){
                eel.test("cool");
                window.location.href = 'splb.html';
            }
            if(e == 2){
                alert("Please choose an option");
            }
        })
    }

    else if (value == "" && window.location.href!='http://localhost:8000/forms/disc.html'){
        alert("Please choose an option.");
        }
    else if (window.location.href == 'http://localhost:8000/forms/disc.html'){
        window.location.href = 'wannavote.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/wannavote.html'){
        window.location.href = 'splb.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/splb.html'){
        eel.votingDict('splb', value);
        window.location.href = 'splg.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/splb.html'){
        eel.votingDict('splb', value);
        window.location.href = 'splg.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/splg.html'){
        eel.votingDict('splg', value);
        window.location.href = 'asplb.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/asplb.html'){
        eel.votingDict('asplb', value);
        window.location.href = 'asplg.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/asplg.html'){
        eel.votingDict('asplg', value);
        window.location.href = 'csb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/csb.html'){
        eel.votingDict('csb', value);
        window.location.href = 'csg.html'
        }
    else if (window.location.href == 'http://localhost:8000/forms/csg.html'){
        eel.votingDict('csg', value);
        window.location.href = 'acsb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/acsb.html'){
        eel.votingDict('acsb', value);
        window.location.href = 'acsg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/acsg.html'){
        eel.votingDict('acsg', value);
        window.location.href = 'scb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/scb.html'){
        eel.votingDict('scb', value);
        window.location.href = 'scg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/scg.html'){
        eel.votingDict('scg', value);
        window.location.href = 'ascb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/ascb.html'){
        eel.votingDict('ascb', value);
        window.location.href = 'ascg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/ascg.html'){
        eel.votingDict('ascg', value);
        eel.submitVote();
        window.location.href = 'thanks.html'
        }
    }

function goBack(){
    eel.test(window.location.href);
    if (window.location.href == 'http://localhost:8000/forms/disc.html'){
        window.location.href = '../index.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/wannavote.html'){
        window.location.href = 'disc.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/splb.html'){
        window.location.href = 'wannavote.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/splg.html'){
        window.location.href = 'splb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/asplb.html'){
        window.location.href = 'splg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/asplg.html'){
        window.location.href = 'asplb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/csb.html'){
        window.location.href = 'asplg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/csg.html'){
        window.location.href = 'csb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/acsb.html'){
        window.location.href = 'csg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/acsg.html'){
        window.location.href = 'acsb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/scb.html'){
        window.location.href = 'acsg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/scg.html'){
        window.location.href = 'scb.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/ascb.html'){
        window.location.href = 'scg.html';
        }
    else if (window.location.href == 'http://localhost:8000/forms/ascg.html'){
        window.location.href = 'ascb.html';
        }
    }

function goBackToLoginPage(){
    window.location.href = '../index.html'}