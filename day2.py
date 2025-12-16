#一人当たりの金額を算出するプログラム

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?💲"))
tip = int(input("What percentage tip would you like to give 10 12 15 "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip/100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person =  total_bill / people

final_amount = round(bill_per_person,2)

print(f"Each person should pay:💲{final_amount}")

#=====================================================================================



#観点1:
# 入力/bill=150💲,tip=10,people=2
# 期待/1人あたり182.5💲
# 正常系






 
#観点2:
# 入力/bill=100💲, tip=0, people=2
# 期待/1人あたり50.00💲
# 割合計算が0でも壊れないか







#観点3:
# 入力/bill=100💲, tip=10, people=1
# 期待/110.00💲
# 割り算が正しく処理される






#観点4:
# 入力/bill=100, tip=12, people=3
# 期待/小数点2桁まで表示（例：37.33）
# round が効いているか






#観点5:
# 入力/bill=99.99, tip=15, people=2
# 期待/小数点2桁で表示される（例：57.49）
# floutが効いているか
