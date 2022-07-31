var ethereum = 1;

function removeMonke(ele) {
    ele.parentNode.removeChild(ele);
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('number').value = value;
}


function incrementValue() {
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('number').value = value;
}

function removeElement(ele) {
    ele.parentNode.removeChild(ele);
}

function btnClick() {
    ethereum = ethereum + 1;

    document.getElementById("number").innerHTML = ethereum;
}