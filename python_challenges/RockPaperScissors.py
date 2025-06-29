import random

ROCK = 1
PAPER = 2
SCISSORS = 3

Moves = {
    "r": ROCK,
    "p": PAPER,
    "s": SCISSORS,
    "rock": ROCK,
    "paper": PAPER,
    "scissors": SCISSORS
}

MoveNames = {
    ROCK: "Rock",
    PAPER: "Paper",
    SCISSORS: "Scissors"
}

def getplayermove():
    while True:
        playerinput = input("Enter your move (r for Rock, p for Paper, s for Scissors): ").lower().strip()
        if playerinput in Moves:
            return Moves[playerinput]
        else:
            print("Invalid input! Please type 'r', 'p', 's', 'rock', 'paper', or 'scissors'.")

def getcomputermove():
    return random.randint(1, 3) 

def determinewinner(playerm, cpum):
    if playerm == cpum:
        return "It's a DRAW!"
    elif (playerm == ROCK and cpum == SCISSORS) or (playerm == PAPER and cpum == ROCK) or (playerm == SCISSORS and cpum == PAPER):
        return "PLAYER WINS!"
    else:
        return "COMPUTER WINS!"

print("welcome")

playerchoice = getplayermove()
cpuchoice = getcomputermove()

print(f"Player chose: {MoveNames[playerchoice]}")
print(f"Computer chose: {MoveNames[cpuchoice]}")

result = determinewinner(playerchoice, cpuchoice)
print(result)

print("game over")