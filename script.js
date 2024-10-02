const moves = ['Rock', 'Paper', 'Scissors'];

// Player and computer scores
let playerScore = 0;
let computerScore = 0;

// DOM elements
const pScore = document.getElementById('p-score');
const cScore = document.getElementById('c-score');
const pMoveImg = document.getElementById('p-move');
const cMoveImg = document.getElementById('c-move');

// Images for moves
const moveImages = {
  'Rock': 'images/Rock.png',
  'Paper': 'images/Paper.png', // Ensure 'Paper.png' matches the actual file name
  'Scissors': 'images/Scissor.png' // Ensure 'Scissors.png' matches the actual file name
};

// Event listener for player move selection
document.querySelectorAll('.options').forEach(option => {
  option.addEventListener('click', function() {
    const playerMove = this.value;
    const computerMove = getComputerMove();
    
    // Display moves
    pMoveImg.src = moveImages[playerMove];
    cMoveImg.src = moveImages[computerMove];

    // Determine winner
    const result = getRoundWinner(playerMove, computerMove);
    updateScore(result);
    checkWinner();
  });
});

// Function to get computer's random move
function getComputerMove() {
  const randomIndex = Math.floor(Math.random() * moves.length);
  return moves[randomIndex];
}

// Function to determine the winner of the round
function getRoundWinner(playerMove, computerMove) {
  if (playerMove === computerMove) {
    return 'draw';
  }
  
  if (
    (playerMove === 'Rock' && computerMove === 'Scissors') ||
    (playerMove === 'Paper' && computerMove === 'Rock') ||
    (playerMove === 'Scissors' && computerMove === 'Paper')
  ) {
    return 'player';
  } else {
    return 'computer';
  }
}

// Function to update scores based on result
function updateScore(result) {
  if (result === 'player') {
    playerScore++;
    pScore.textContent = playerScore;
  } else if (result === 'computer') {
    computerScore++;
    cScore.textContent = computerScore;
  }
}

// Function to check if someone won the game
function checkWinner() {
  if (playerScore === 5) {
    alert('Congratulations! You won the game.');
    resetGame();
  } else if (computerScore === 5) {
    alert('Computer wins! Better luck next time.');
    resetGame();
  }
}

// Function to reset the game
function resetGame() {
  playerScore = 0;
  computerScore = 0;
  pScore.textContent = 0;
  cScore.textContent = 0;
  pMoveImg.src = '';
  cMoveImg.src = '';
}
