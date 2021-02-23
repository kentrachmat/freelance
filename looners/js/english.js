// Function to write by itselfs
window.addEventListener("load",write);

var index = 0;
var speed = 200;
var text = 'English is great !'; 


function write() {
  if (index < text.length) {
    document.getElementById("board").innerHTML += text.charAt(index);
    index++;
    setTimeout(write, speed);
  }
}

