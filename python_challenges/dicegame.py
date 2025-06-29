import random

print("Dice roll game ")
print('''How the game works
      1. Enter the number of players who are going to play the game
      2. Roll the dice 
      3. If you roll a six the game is over''')

players = int(input("Enter number of players: "))
i = 0

while i!=6:
    for j in range(players):
        print(f"player {j+1} turn")
        inp=input("Press Enter key to roll the dice: ")
        i = random.randint(1,6)
        
        if i == 6:
            print(f"player {j+1} rolled 6, Game Over")
            break
        else:
            print(f"player {j+1} rolled {i} Game Continues")