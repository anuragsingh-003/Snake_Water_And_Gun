# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

import random
print('Snake - Water - Gun')
print("Game Begins!!")
 
 
# Input no. of rounds
n = int(input('Enter number of rounds: '))
 
 
# List containing Snake(s), Water(w), Gun(g)
options = ['Snake', 'Water', 'Gun']
 
# Round numbers
rounds = 0
 
# Count of computer wins
comp_win = 0
 
# Count of player wins
user_win = 0
 
 
# There will be n rounds of game
while rounds <= n:
 
    # Display round
    print("Rounds")
    print(rounds)
 
    # Exception handling
    try:
        player = input("Choose your option: ")
    except EOFError as e:
        print(e)
 
    # Control of bad inputs
    if player != 'Snake' and player != 'Water' and player != 'Gun':
        print("Invalid input, try again\n")
        continue
 
    # random.choice() will randomly choose
    # item from list- options
    computer = random.choice(options)
    print("Computer Choice: "+computer)
    print("Player Choice: "+player)
 
    # Conditions based on the game rule
    if computer == 'Snake':
        if player == 'Water':
            comp_win += 1
        elif player == 'Gun':
            user_win += 1
 
    elif computer == 'Water':
        if player == 'Gun':
            comp_win += 1
        elif player == 'Snake':
            user_win += 1
 
    elif computer == 'Gun':
        if player == 'Snake':
            comp_win += 1
        elif player == 'Water':
            user_win += 1
 
    # Announce winner of every round
    if user_win > comp_win:
        print(f"You Won round {rounds}\n")
    elif comp_win > user_win:
        print(f"Computer Won round {rounds}\n")
    else:
        print("Draw!!\n")
 
    rounds += 1
 
 
# Final winner based on the number of wons
if user_win > comp_win:
    print("Congratulations!! You Won")
elif comp_win > user_win:
    print("You lose!!")
else:
    print("Match Draw!!")