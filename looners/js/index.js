document.querySelector('body').addEventListener('mousemove', eyeball);

function eyeball() {
    var eye = document.querySelectorAll('.eye');
    eye.forEach(function (eye) {
        let x = (eye.getBoundingClientRect()
            .left) + (eye.clientWidth / 2);
        let y = (eye.getBoundingClientRect()
            .top) + (eye.clientHeight / 2);
        let radian = Math.atan2(event.pageX -
            x, event.pageY - y);
        let rot = (radian * (180 / Math.PI) * -1) + 0;
        eye.style.transform = "rotate(" + rot + "deg)";
    })
}

var circle = document.getElementById("circle");
var button = document.getElementById("button");
var btn = document.getElementById("btn");

var rotateValue = circle.style.transform;
var rotateSum;

button.onclick = function () {
    rotateSum = rotateValue + "rotate(-90deg)";
    circle.style.transform = rotateSum;
    rotateValue = rotateSum;
}
btn.onclick = function () {
    rotateSum = rotateValue + "rotate(+90deg)";
    circle.style.transform = rotateSum;
    rotateValue = rotateSum;
}
