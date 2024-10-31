const choosingBox = document.querySelector("#choosing-box");
const scissorsButton = document.querySelector("#scissors-button");
const rockButton = document.querySelector("#rock-button");
const paperButton = document.querySelector("#paper-button");
const modal = document.querySelector(".modal");
const modalContent = document.querySelector(".modal-content");

modal.addEventListener("click", (event) => {
  modal.style.display = "none";
});

let count1 = 0;
let count2 = 0;

const playGame = (player1, player2) => {
  if (player1 === "scissors") {
    if (player2 === "rock") {
      count2 += 1;
      return 2;
    } else if (player2 === "paper") {
      count1 += 1;
      return 1;
    }
  } else if (player1 === "rock") {
    if (player2 === "paper") {
      count2 += 1;
      return 2;
    } else if (player2 === "scissors") {
      count1 += 1;
      return 1;
    }
  } else {
    if (player2 === "scissors") {
      count2 += 1;
      return 2;
    } else if (player2 === "rock") {
      count1 += 1;
      return 1;
    }
  }
  return 0;
};

const buttonClickHandler = function (event) {
  // console.log(event.target);
  // console.log(event.target.id);
  // let choice;
  // if (event.target.id === "rock-button") {
  //   choice = "rock";
  // } else if (event.target.id === "scissors-button") {
  //   choice = "scissors";
  // } else if (event.target.id === "paper-button") {
  //   choice = "paper";
  // }

  let choice;
  if (event.target.id.includes("rock")) {
    choice = "rock";
  } else if (event.target.id.includes("scissors")) {
    choice = "scissors";
  } else if (event.target.id.includes("paper")) {
    choice = "paper";
  }

  const buttons = [scissorsButton, rockButton, paperButton];
  buttons.forEach((button) => {
    button.disabled = true;
  });

  const choices = ["rock", "scissors", "paper"];
  const randomIndex = Math.floor(Math.random() * 3);
  const result = playGame(choice, choices[randomIndex]);

  const player1Img = document.querySelector("#player1-img");
  const player2Img = document.querySelector("#player2-img");
  player1Img.src = `./img/${choice}.png`;
  // console.log("image source:", player1Img.src);
  let i = randomIndex + 1;
  const rotateImg = () => {
    i = (i + 1) % 3;
    player2Img.src = `./img/${choices[i]}.png`;
  };

  const timerId = setInterval(rotateImg, 100);
  setTimeout(() => {
    clearInterval(timerId);
    const countA = document.querySelector(".countA");
    const countB = document.querySelector(".countB");
    countA.innerText = count1;
    countB.innerText = count2;
    player2Img.src = `./img/${choices[randomIndex]}.png`;
    modalContent.innerText = result ? `Player ${result}이 이겼쓰!` : `비겼쓰!`;
    modal.style.display = "flex";

    buttons.forEach((button) => {
      button.disabled = false;
    });
  }, 1000);
};

choosingBox.addEventListener("click", buttonClickHandler);
// scissorsButton.addEventListener("click", () => {
//   buttonClickHandler("scissors");
// });
// rockButton.addEventListener("click", () => {
//   buttonClickHandler("rock");
// });
// paperButton.addEventListener("click", () => {
//   buttonClickHandler("paper");
// });
