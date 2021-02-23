// The lists of objects
const Objects = [

    {
        iconName: "cat",
        Name: "Cat",
        color: "#fd5c63",
        type: "living"
        },
    {
        iconName: "dog",
        Name: "Dog",
        color: "yellow",
        type: "living"
        },
    {
        iconName: "dove",
        Name: "Dove",
        color: "brown",
        type: "living"
        },
    {
        iconName: "tshirt",
        Name: "tshirt",
        color: "red",
        type: "nonliving"
        },
    {
        iconName: "hotdog",
        Name: "Hotdog",
        color: "pink",
        type: "nonliving"
        },
    {
        iconName: "hamburger",
        Name: "Hamburger",
        color: "blue",
        type: "nonliving"
        }
    ];

// The Variables
let correct = 0;
let total = 0;
let draggableElements;
let droppableElements;
let randomSound;

const varToString = varObj => Object.keys(varObj)[0]
const totalDraggableItems = 6;
const totalMatchingPairs = totalDraggableItems;

const ScoreC = document.querySelector(".score");
//const correctSpan = ScoreC.querySelector(".correct");
const totalSpan = ScoreC.querySelector(".total");
const draggableItems = document.querySelector(".draggable-items");
const matchingPairs = document.querySelector(".matching-pairs");
const context = new window.AudioContext();

const catPic = document.getElementById("catPic");
const cowPic = document.getElementById("cowPic");
const dogPic = document.getElementById("dogPic");
const chickenPic = document.getElementById("chickenPic");
const frogPic = document.getElementById("frogPic");

var dict = {
    catsound: "catPic",
    cowsound: "cowPic",
    dogsound: "dogPic",
    chickensound: "chickenPic",
    frogsound: "frogPic"
};

StartGame();

// Function to fill the element and start the game
function StartGame() {
    const randomDraggableLogo = Randomly(totalDraggableItems, Objects);
    const randomDroppableLogo = totalMatchingPairs < totalDraggableItems ? Randomly(totalMatchingPairs, randomDraggableLogo) : randomDraggableLogo;
    const SortedRandomObjects = [...randomDroppableLogo].sort((a, b) => a.Name.toLowerCase().localeCompare(b.Name.toLowerCase()));

    for (let i = 0; i < randomDraggableLogo.length; i++) {
        draggableItems.insertAdjacentHTML("beforeend", `
      <i class="fas fa-${randomDraggableLogo[i].iconName} draggable" draggable="true" style="color: ${randomDraggableLogo[i].color};" id="${randomDraggableLogo[i].iconName}" data-type="${randomDraggableLogo[i].type}"></i>
    `);
    }

    matchingPairs.insertAdjacentHTML("beforeend", `<div class="row"><div class="titleboxes col-sm-12">Drag a Non-Living things</div></div>`);

    for (let i = 0; i < SortedRandomObjects.length; i++) {
        if (SortedRandomObjects[i].type == "nonliving") {
            matchingPairs.insertAdjacentHTML("beforeend", `
      <div class="matching-pair col-sm-4">
        <span class="droppable" data-type="${SortedRandomObjects[i].type}" data-logo="${SortedRandomObjects[i].iconName}"></span>
      </div>
    `);
        }
    }

    matchingPairs.insertAdjacentHTML("beforeend", `<div class="row"><div class="titleboxes col-sm-12">Drag a Living things</div></div>`);

    for (let i = 0; i < SortedRandomObjects.length; i++) {
        if (SortedRandomObjects[i].type == "living") {
            matchingPairs.insertAdjacentHTML("beforeend", `
      <div class="matching-pair col-sm-4">
        <span class="droppable" data-type="${SortedRandomObjects[i].type}" data-logo="${SortedRandomObjects[i].iconName}"></span>
      </div>
    `);
        }
    }

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
        event.target.insertAdjacentHTML("afterbegin", `<i class="fas fa-${draggableLogo}" style="font-size:100px; color:white;"></i><span style="color:white; font-size: 20px;">${draggableLogo}</span>`);
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
            title: 'Congratulation you have finished your science game !',
            text: textSwal,
            icon: 'success',
            showCancelButton: true,
            customClass: 'swal-wide',
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Continue ?'
        }).then((result) => {
            if (result.isConfirmed) {
                playAgainBtnClick();
            }
        })
    }
}

//playAgainBtn.addEventListener("click", playAgainBtnClick);

// Function to play again
function playAgainBtnClick() {
    correct = 0;
    total = 0;
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

// Generate random list function
function Randomly(n, originalArray) {
    let res = [];
    let clonedArray = [...originalArray];
    if (n > clonedArray.length) n = clonedArray.length;
    for (let i = 1; i <= n; i++) {
        const randomIndex = Math.floor(Math.random() * clonedArray.length);
        res.push(clonedArray[randomIndex]);
        clonedArray.splice(randomIndex, 1);
    }
    return res;
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

function check1() {
    var $ele = $('.sound');
    randomSound = $ele.eq(Math.floor(Math.random() * ($ele.length - 1))).attr('id')

    document.getElementById(randomSound).play();
};

function checkSound(so) {
    var counterSound = $('.sound').length;
    if (counterSound == 1) {
        Swal.fire({
            title: "Wow you have a great hearing !",
            icon: 'success',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            customClass: 'swal-wide',
            confirmButtonText: 'Restart'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location = "science.html";
            } else {
                $("#check1").remove();
            }
        })
    }

    if (dict[randomSound] == so) {
        PlayMusic('https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/success.mp3');
        document.getElementById(so).src = "images/check.png";
        document.getElementById(randomSound).classList.remove("sound")
        counterSound--;
    } else {
        PlayMusic('https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/error.mp3');
    }

}
