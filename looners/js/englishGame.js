// The Lists of words
const Objects = ["Pencil", "Sad", "Cat", "House"];

// The Variables
var x = document.getElementById("myAudio1");
var y = document.getElementById("myAudio2");

let correct = 0;
let total = 0;
let draggableElements;
let droppableElements;
let randomDraggableLogo = Randomly();
let totalDraggableItems = randomDraggableLogo.length;
let totalMatchingPairs = totalDraggableItems;
let randomWord = randomDraggableLogo.split('').sort(function () {
    return 0.5 - Math.random()
}).join('');

const boxElements = document.querySelectorAll(".box");
const ScoreC = document.querySelector(".score");
const totalSpan = ScoreC.querySelector(".total");
const hintbutton = document.getElementById("hintbutton");
const draggableItems = document.querySelector(".draggable-items");
const matchingPairs = document.querySelector(".matching-pairs");
const context = new window.AudioContext();

boxElements.forEach(elem => {
    elem.addEventListener("dragstart", dragStart1);
    elem.addEventListener("dragend", dragEnd1);
    elem.addEventListener("dragenter", dragEnter1);
    elem.addEventListener("dragover", dragOver1);
    elem.addEventListener("dragleave", dragLeave1);
    elem.addEventListener("drop", drop1);
});

// The Drag and Drop Functions
function dragStart1(event) {
    event.target.classList.add("drag-start");
    event.dataTransfer.setData("text", event.target.id);
}

function dragEnd1(event) {
    event.target.classList.remove("drag-start");
}

function dragEnter1(event) {
    if (!event.target.classList.contains("drag-start")) {
        event.target.classList.add("drag-enter");
    }
}

function dragOver1(event) {
    event.preventDefault();
}

function dragLeave1(event) {
    event.target.classList.remove("drag-enter");
}

function drop1(event) {
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
            title: 'Congratulations you\'ve made it !',
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

StartGame();

// Function to start the game and fill the missing element in HTML
function StartGame() {

    const bootstrap = Math.floor(12 / randomDraggableLogo.length);

    hintbutton.addEventListener("click", function () {
        Swal.fire({
            icon: 'info',
            title: 'The word is : ' + randomDraggableLogo,
            customClass: 'swal-wide',
        })
    });

    matchingPairs.insertAdjacentHTML("beforeend", `
      <div class="row">
    `);

    for (let i = 0; i < randomDraggableLogo.length; i++) {
        matchingPairs.insertAdjacentHTML("beforeend", `
      <div class="matching-pair col-sm-${bootstrap}">
        <span class="droppable" data-type="${randomDraggableLogo[i]}" data-logo="${randomDraggableLogo[i]}"></span>
      </div>
    `);
    }

    matchingPairs.insertAdjacentHTML("beforeend", `
      </div>
    `);

    matchingPairs.insertAdjacentHTML("beforeend", `
      <div class="row">
    `);

    for (let i = 0; i < randomWord.length; i++) {
        draggableItems.insertAdjacentHTML("beforeend", `
      <p class="draggable englishtext" draggable="true" id="${randomWord[i]}" data-type="${randomWord[i]}">${randomWord[i]}</p>
    `);
    }

    matchingPairs.insertAdjacentHTML("beforeend", `
      </div>
    `);

    draggableElements = document.querySelectorAll(".draggable");
    droppableElements = document.querySelectorAll(".droppable");

    draggableElements.forEach(elem => {
        elem.addEventListener("dragstart", dragStart);
    });

    droppableElements.forEach(elem => {
        elem.addEventListener("dragenter", dragEnter);
        elem.addEventListener("dragover", dragOver);
        elem.addEventListener("dragleave", dragLeave);
        elem.addEventListener("drop", drop);
    });
}

// The Drag and Drop Functions
function dragStart(event) {
    event.dataTransfer.setData("text", event.target.getAttribute('id'));
    event.dataTransfer.setData("type", event.target.getAttribute('data-type'));
}

function dragEnter(event) {
    if (event.target.classList && event.target.classList.contains("droppable") && !event.target.classList.contains("dropped")) {
        event.target.classList.add("droppable-hover");
    }
}

function dragOver(event) {
    if (event.target.classList && event.target.classList.contains("droppable") && !event.target.classList.contains("dropped")) {
        event.preventDefault();
    }
}

function dragLeave(event) {
    if (event.target.classList && event.target.classList.contains("droppable") && !event.target.classList.contains("dropped")) {
        event.target.classList.remove("droppable-hover");
    }
}

function drop(event) {
    event.preventDefault();
    event.target.classList.remove("droppable-hover");

    const draggableLogo = event.dataTransfer.getData("text");
    const droppableElementLogo = event.target.getAttribute("data-logo");
    const x = event.target.getAttribute("data-type");
    const y = event.dataTransfer.getData("type");
    const isCorrectMatching = x == y;

    if (isCorrectMatching) {
        const draggableElement = document.getElementById(draggableLogo);
        event.target.classList.add("dropped");
        event.target.style.backgroundColor = window.getComputedStyle(draggableElement).color;
        draggableElement.classList.add("dragged");
        draggableElement.setAttribute("draggable", "false");
        event.target.insertAdjacentHTML("afterbegin", `<span style="font-family: '3dumbregular',
        Arial,
        sans-serif;
    color: white;
    font-size: 100px;">${draggableLogo}</span>`);
        correct++;

        PlayMusic('https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/success.mp3');

    } else {
        total = total + 10;

        PlayMusic('https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/error.mp3');
    }
    ScoreC.style.opacity = 0;
    setTimeout(() => {
        //correctSpan.textContent = correct;
        totalSpan.textContent = 100 - total + " %";
        ScoreC.style.opacity = 1;
    }, 200);
    if (correct === Math.min(totalMatchingPairs, totalDraggableItems)) {

        var textSwal = "Your score is " + (100 - total) + " %, ";

        if (100 - total > 60)
            textSwal += "Great Job !!"
        else if (100 - total > 40)
            textSwal += "Not Bad, Keep Practice !!"
        else if (100 - total < 0)
            textSwal += "Keep Learning and Stay Curious !!"

        PlayMusic('https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/success.mp3');

        Swal.fire({
            title: 'Congratulation you have finished your English game !',
            text: textSwal,
            icon: 'success',
            showCancelButton: true,
            customClass: 'swal-wide',
            confirmButtonColor: '#3085d6',
            cancelButtonColor: 'purple',
            confirmButtonText: 'Continue ?',
            cancelButtonText: 'Have your partner look at what you wrote !'
        }).then((result) => {
            if (result.isConfirmed) {
                playAgainBtnClick();
            }
        })
    }
}

// Function to play the game again
function playAgainBtnClick() {
    correct = 0;
    total = 0;
    randomDraggableLogo = Randomly();
    totalDraggableItems = randomDraggableLogo.length;
    totalMatchingPairs = totalDraggableItems;
    randomWord = randomDraggableLogo.split('').sort(function () {
        return 0.5 - Math.random()
    }).join('');
    draggableItems.style.opacity = 0;
    matchingPairs.style.opacity = 0;
    setTimeout(() => {
        ScoreC.style.opacity = 0;
    }, 100);
    setTimeout(() => {
        //playAgainBtn.style.display = "none";
        while (draggableItems.firstChild) draggableItems.removeChild(draggableItems.firstChild);
        while (matchingPairs.firstChild) matchingPairs.removeChild(matchingPairs.firstChild);
        StartGame();
        //correctSpan.textContent = correct;
        totalSpan.textContent = total;
        draggableItems.style.opacity = 1;
        matchingPairs.style.opacity = 1;
        ScoreC.style.opacity = 1;
    }, 500);
}

// Generate a random word from the list
function Randomly() {
    return Objects[Math.floor(Math.random() * Objects.length)];
}

// Function to decode audio data 
function PlayMusic(filepath) {
    fetch(filepath)
        .then(response => response.arrayBuffer())
        .then(arrayBuffer => context.decodeAudioData(arrayBuffer))
        .then(audioBuffer => {
            const soundSource = context.createBufferSource();
            soundSource.buffer = audioBuffer;
            soundSource.connect(context.destination);
            soundSource.start();
        });
}
