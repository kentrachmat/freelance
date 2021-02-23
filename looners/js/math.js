// Function to write by itselfs
window.addEventListener("load",typeWriter);

var i = 0;
var texts = 'Math is Amazing !'; 
var speed = 200;

function typeWriter() {
  if (i < texts.length) {
    document.getElementById("board").innerHTML += texts.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}



