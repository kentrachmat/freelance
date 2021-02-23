// The Variables for Game 1
const boxElements = document.querySelectorAll(".box");
const ScoreC = document.querySelector(".score");
const totalSpan = ScoreC.querySelector(".total");

var x = document.getElementById("myAudio1");
var y = document.getElementById("myAudio2");

let total = 0;
let attempt = 0;
let limit = 10;

// Allow the drag and drop
boxElements.forEach(elem => {
    elem.addEventListener("dragstart", dragStart);
    elem.addEventListener("dragend", dragEnd);
    elem.addEventListener("dragenter", dragEnter);
    elem.addEventListener("dragover", dragOver);
    elem.addEventListener("dragleave", dragLeave);
    elem.addEventListener("drop", drop);
});

// The Drag and Drop Functions
function dragStart(event) {
    event.target.classList.add("drag-start");
    event.dataTransfer.setData("text", event.target.id);
}

function dragEnd(event) {
    event.target.classList.remove("drag-start");
}

function dragEnter(event) {
    if (!event.target.classList.contains("drag-start")) {
        event.target.classList.add("drag-enter");
    }
}

function dragOver(event) {
    event.preventDefault();
}

function dragLeave(event) {
    event.target.classList.remove("drag-enter");
}

function drop(event) {
    event.preventDefault();
    event.target.classList.remove("drag-enter");
    const draggableElementId = event.dataTransfer.getData("text");
    const droppableElementId = event.target.id;
    if (draggableElementId !== droppableElementId) {
        const draggableElement = document.getElementById(draggableElementId);
        const droppableElementBgColor = event.target.style.backgroundColor;
        const droppableElementTextContent = event.target.querySelector("span").textContent;

        event.target.style.backgroundColor = draggableElement.style.backgroundColor;
        event.target.querySelector("span").textContent = draggableElement.querySelector("span").textContent;
        event.target.id = draggableElementId;
        draggableElement.style.backgroundColor = droppableElementBgColor;
        draggableElement.querySelector("span").textContent = droppableElementTextContent;
        draggableElement.id = droppableElementId;
    }
}

// Makes us able to know the position of an element, to tell if the we obtnained the right sequence in the math game
function getPosition(el) {

    var xPos = 0;
    var yPos = 0;

    while (el) {
        if (el.tagName == "BODY") {
            // deal with browser quirks with body/window/document and page scroll
            var xScroll = el.scrollLeft || document.documentElement.scrollLeft;
            var yScroll = el.scrollTop || document.documentElement.scrollTop;

            xPos += (el.offsetLeft - xScroll + el.clientLeft);
            yPos += (el.offsetTop - yScroll + el.clientTop);
        } else {
            // for all other non-BODY elements
            xPos += (el.offsetLeft - el.scrollLeft + el.clientLeft);
            yPos += (el.offsetTop - el.scrollTop + el.clientTop);
        }

        el = el.offsetParent;
    }
    return xPos;
};

// Checks if the sequence is right or not using the previous function
function check1() {

    var p1 = getPosition(document.getElementById("box-1"));
    var p2 = getPosition(document.getElementById("box-2"));
    var p3 = getPosition(document.getElementById("box-3"));
    var p4 = getPosition(document.getElementById("box-4"));
    var p5 = getPosition(document.getElementById("box-5"));
    var p6 = getPosition(document.getElementById("box-6"));
    if (p1 < p2 && p2 < p3 && p3 < p4 && p4 < p5 && p5 < p6) {
        y.play();
        Swal.fire({
            icon: 'success',
            title: 'Horray you\'ve made it !',
            customClass: 'swal-wide'
        })
    } else {
        x.play();
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Something is wrong!',
            customClass: 'swal-wide'
        })
    }
};

// The Variables for Game 2
const option1 = document.getElementById("option1");
const option2 = document.getElementById("option2");
const option3 = document.getElementById("option3");
var answer = 0;

// Generate a random basic equation with random numbers
function random_equation() {
    var val1 = Math.floor(Math.random() * 6);
    var val2 = Math.floor(Math.random() * 6);
    var dummyAnswer1 = Math.floor(Math.random() * 12 + 1);
    var dummyAnswer2 = Math.floor(Math.random() * 12 + 7);
    var random = [];
    answer = eval(val1 + val2);

    document.getElementById("value1").innerHTML = val1;
    document.getElementById("value2").innerHTML = val2;

    var randomAnswers = [answer, dummyAnswer1, dummyAnswer2];

    for (var randomAnswers = [answer, dummyAnswer1, dummyAnswer2], i = randomAnswers.length; i--;) {
        random.push(randomAnswers.splice(Math.floor(Math.random() * (i + 1)), 1)[0]);
    };

    option1.innerHTML = random[0];
    option2.innerHTML = random[1];
    option3.innerHTML = random[2];

};

// Generate the pop up with sweet alerts 2
function swali() {
    Swal.fire({
        title: "Congratulation, the game is finished !",
        text: "Your score is : " + (100 - total) + " %, Great job !",
        icon: 'success',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        customClass: 'swal-wide',
        confirmButtonText: 'Restart'
    }).then((result) => {
        if (result.isConfirmed) {

            window.location = "math.html";

        }
    })
}

// Add the functionality for each options
option1.addEventListener("click", function () {
    attempt++;
    if (attempt == limit) {
        swali();
    }
    if (option1.innerHTML == answer) {
        y.play();
        totalSpan.textContent = 100 - total + " %";
        random_equation();

    } else {
        total = total + 10;
        totalSpan.textContent = 100 - total + " %";
        x.play();
    }
});
option2.addEventListener("click", function () {
    attempt++;
    if (attempt == limit) {
        swali();
    }
    if (option2.innerHTML == answer) {
        y.play();
        totalSpan.textContent = 100 - total + " %";
        random_equation();

    } else {
        total = total + 10;
        totalSpan.textContent = 100 - total + " %";
        x.play();
    }
});
option3.addEventListener("click", function () {
    attempt++;
    if (attempt == limit) {
        swali();
    }
    if (option3.innerHTML == answer) {
        y.play();
        totalSpan.textContent = 100 - total + " %";
        random_equation();

    } else {
        total = total + 10;
        totalSpan.textContent = 100 - total + " %";
        x.play();
    }
});

// Function is called for it to work as soon as you open the website
random_equation()
