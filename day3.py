#選択式ゲーム

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    "You're at a crossroads, where do you want to go?\n"
    'Type "Left" or "Right".\n').lower()

if choice1 == "left":
    print("You've come to a lake.")
    print("There is an island in the middle of the lake.")
    print('Type "wait" to wait for a boat.')
    print('Type "swim" to swim across.')

    choice2 = input("What do you choose? ").lower()

    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed.\n"
            "There is a house with 3 doors: one red, one yellow and one blue.\n"
            "Which colour do you choose?\n").lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")


#========================================================================================================


#観点1:正常値を入力したら？　

# 入力/　 choice1:left →  choice2:wait → choice3:yellow
# 期待/  宝箱を見つけた。あなたの勝利です!と表示される




#観点2:　方向入力にスペースのみを入力したら？

#入力/　" "（スペース1文字）
#期待/ 条件に一致しないため Game Over と表示される





#観点３:色の扉で　"red" "yellow" "blue"以外が入力されたら？

#入力/ green
#期待/ 「存在しないドアを選択しました」と表示されてGame Overになる




#観点4: 大文字入力でも正しく判定されるか

#入力/ choice1: LEFT hoice2: WAIT choice3: YELLOW
#期待/ すべて小文字に変換され、勝利メッセージが表示される