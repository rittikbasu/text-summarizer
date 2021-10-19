function reset() {
  document.getElementById("select").selectedIndex = 0;
  document.getElementById('num').value = '';
  document.getElementById("url").value = '';
}
window.onload = reset;

function toggle() {
  var url = document.getElementById("url");
  var text = document.getElementById("text");
  var x = document.getElementById("select").value;
    if (x=='URL') {
        text.style.display = "none";
        url.style.display = "block";
        url.disabled = false;
        text.disabled = true;
    }
    if (x=='Text Box') {
        url.style.display = "none";
        text.style.display = "block";
        text.disabled = false;
        url.disabled = true;
    }
}

