#TODO-1: Ask the user for input
#TODO-2: Save data into dictionary{name:price]}
#TODO-3: Whether if new bids need to be added
#TODO-4: Compare bids in dictionary


#1 usage
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?")

    #最小改造
    #名前が未入力(空文字)の場合処理を進めない
    #仕様を変えず、再入力のみさせる
    if name == "":
        print("名前を入力してください")
    continue

    price =int(input("What is your bid?:$"))
    #入札金額はint()を使用
    #数字以外や小数点入力時はValueErrorになる仕様を利用する
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' .\n").lower()

    #　yes/no　以外の入力は「yes扱い」としてオークションを継続する使用
    if should_continue == "no":
       continue_bidding = False
       find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)




#####################################################################################################



#観点1:　nameに空白を入れたら？

# 入力/　What is your name?" "
# 期待/  The winner is   with a bid of $70. 名前が空白で表示される




#観点2: nameに数字を入れたら？

#入力/　What is your name?20
#期待/ The winner is 20 with a bid of $70. そのまま表示される




#観点3: 入札金額に小数点のある数字を入れたら？

#入力/ What is your bid?:$20.5
#期待/　バリューエラーと表示される




#観点4:　入札金額に数字以外をを入れたら？

#入力/　What is your bid?:$yusuke
#期待/　バリューエラーと表示される




#観点5: 他に入札者がいるどうかの問いに"yes" "no"以外で答えると？

#入力/ Are there any other bidders? Type 'yes' or 'no' .　yusuke
#期待/　What is your name?と表示されそのままオークションが続く




