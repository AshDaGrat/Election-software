function getSelectedOption() {
    var options = document.getElementsByName('options');
    var value = ""
    for (var i = 0; i < options.length; i++) {
        if (options[i].checked) {
            value = options[i].value;	
        }	
    }
    eel.test(value)
}
