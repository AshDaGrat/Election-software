
const bold = document.querySelector('.bold')
const italic = document.querySelector('.italic')
const editable = document.querySelector('.editable')

editable.innerHTML = `
<div class="leftside">
<label class="labelexpanded">
    <input type="radio" id="Ayaan Jamil" name="options" value="Ayaan Jamil">
    <div class="radio-btns">
        <img src="../assets/yea.png">
        <p>Ayaan Jamil</p>
    </div>
</input>
</label>
<label class="labelexpanded">
    <input type="radio" id="Jyaan Aamil" name="options" value="Jyaan Aamil">
    <div class="radio-btns">
        <img src="../assets/fourfeet.png">
        <p>Jyaan Aamil</p>
    </div>
</input>
</label>


<button type="button" class='radio-btns' onclick="getSelectedOption();">button</button>
</div>
`;

