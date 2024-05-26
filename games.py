import random

while True:
    #******************** WELCOME TO ROCK PAPER SCISSOR GAME ********************
    user_score = 0
    comp_score = 0
    ties = 0
    name = input("Enter your name: ")
    print('''winning rules
        1. paper vs rock --> paper
        2. rock vs scissor --> rock
        3. scissors vs paper --> scissors''') 

    print('''CHOICES
        1. Rock
        2. Paper
        3. Scissors''')
    
    choice = int(input("Enter your choice 1-3: "))
    print("User choice: ", choice)

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
    
    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissors"

    print("The user's choice is", user_choice)
    
    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice = "rock"  
    elif computer == 2:
        comp_choice = "paper" 
    else:
        comp_choice = "scissors"  

    print("Computer choice is", comp_choice) 

    if ((user_choice == "paper" and comp_choice == "rock") or
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "scissors" and comp_choice == "paper")):
        print(f"{user_choice} wins")
        result = user_choice
    elif user_choice == comp_choice:
        print("It's a tie")
        result = "tie"
    else:
        print(f"{comp_choice} wins")
        result = comp_choice 

    if result == "tie":
        ties += 1
    elif result == user_choice:
        user_score += 1
    else:
        comp_score += 1

    print("Scores are:")
    print(name,"'s score is" ,user_score)
    print("Computer's score is",comp_score)
    print("Ties are", ties)

    repeat = input("Do you want to play again? (yes/no): ").lower()
    if repeat == "no":
        break

print("Game Over")
print("Thanks for playing")
