import random

while True:
    player_input = input("\n\n\n\n\n\nInput [R]ock, [P]aper or [S]cissors to play the game. \nInput 0 to exit. \n>>> ")

    # 0=Rock, 1=Paper, 2=Scissors
    computer_input = str(random.randint(0, 2))

    def rock():
        if computer_input == "0":
            print("The computer used Rock. It's a draw!")
        elif computer_input == "1":
            print("The computer used Paper. You lose!")
        elif computer_input == "2":
            print("The computer used Scissors. You win!")

    def paper():
        if computer_input == "0":
            print("The computer used Rock. You win!")
        elif computer_input == "1":
            print("The computer used Paper. It's a draw!")
        elif computer_input == "2":
            print("The computer used Scissors. You lose!")

    def scissors():
        if computer_input == "0":
            print("The computer used Rock. You lose!!")
        elif computer_input == "1":
            print("The computer used Paper. You win!")
        elif computer_input == "2":
            print("The computer used Scissors. It's a draw!") 

    def game():
        if player_input.upper() == "R":
            rock()
            
        elif player_input.upper() == "P":
            paper()
            
        elif player_input.upper() == "S":
            scissors()
        
        elif player_input == "0":
            exit()
            
        else:
            input("Invalid input. Press any key to continue")

    game()
    continue