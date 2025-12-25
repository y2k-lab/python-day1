#ジャンケンゲーム
game_images = ["rock","paper","scissors"]

user_choice = int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
    computer_choice = randam.randint 
print(f"Computer chose{computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif computer_choice == 0 and user_choice == 2:
    print("You lose")

elif computer_choice > user_choice:
    print("You lose")

elif user_choice > computer_choice:
    print("You win")

else:
    print("You typed an invalid number.You lose!")