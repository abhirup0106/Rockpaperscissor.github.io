let playerScore = 0;
let computerScore = 0;
let roundsPlayed = 0;
const maxRounds = 5;

function playGame(playerChoice) {
    // Prevent playing more rounds than allowed
    if (roundsPlayed >= maxRounds) {
        displayGameOver();
        return;
    }

    // Computer randomly chooses rock, paper, or scissors
    const choices = ['rock', 'paper', 'scissors'];
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];
    
    // Determine the winner of the current round
    const result = determineWinner(playerChoice, computerChoice);

    // Update scores based on the round result
    updateScores(result);

    // Update the DOM with the current game status
    updateDOM(playerChoice, computerChoice, result);

    // Update rounds played
    roundsPlayed++;
    document.getElementById('roundCount').innerText = roundsPlayed;

    // Check if the game has ended
    if (roundsPlayed >= maxRounds) {
        displayGameOver();
    }
}

// Determine the winner of the current round
function determineWinner(player, computer) {
    if (player === computer) {
        return 'It\'s a draw!';
    } else if (
        (player === 'rock' && computer === 'scissors') ||
        (player === 'paper' && computer === 'rock') ||
        (player === 'scissors' && computer === 'paper')
    ) {
        return 'You won!';
    } else {
        return 'Computer won!';
    }
}

// Update scores based on the round result
function updateScores(result) {
    if (result === 'You won!') {
        playerScore++;
    } else if (result === 'Computer won!') {
        computerScore++;
    }
    
    // Update score display
    document.getElementById('playerScore').innerText = playerScore;
    document.getElementById('computerScore').innerText = computerScore;
}

// Update the DOM to display the current round result
function updateDOM(playerChoice, computerChoice, result) {
    document.getElementById('result').innerHTML = 
        `You chose <strong>${playerChoice}</strong>.<br>` +
        `Computer chose <strong>${computerChoice}</strong>.<br>` +
        `<strong>${result}</strong>`;
}

// Display game over message and results
// Display game over message and results
function displayGameOver() {
  let finalResult = '';

  if (playerScore > computerScore) {
      finalResult = "<strong>You are the overall winner!</strong>";
  } else if (computerScore > playerScore) {
      finalResult = "<strong>Computer is the overall winner!</strong>";
  } else {
      finalResult = "<strong>It's a draw overall!</strong>";
  }

  document.getElementById('result').innerHTML += "<br><strong>Game Over!</strong><br>" + finalResult;
  document.getElementById('restartButton').style.display = 'block'; // Show the restart button
}

// Restart the game
function restartGame() {
    playerScore = 0;
    computerScore = 0;
    roundsPlayed = 0;

    // Reset the display
    document.getElementById('playerScore').innerText = playerScore;
    document.getElementById('computerScore').innerText = computerScore;
    document.getElementById('result').innerText = '';
    document.getElementById('roundCount').innerText = roundsPlayed;
    document.getElementById('restartButton').style.display = 'none'; // Hide the restart button
}
