#合計金額、割合、人数を入力して一人当たりの金額を計算をするプログラム

print("Welcom to the tip calculator!")

bill = float(input("What was the total bill?💲"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill?"))


print(f"bill={bill}, tip={tip}, people={people}")  # ← 最小改造



tip_as_percent = tip / 100

total_tip_amout = bill * tip_as_percent

total_bill = bill + total_tip_amout

bill_per_person = total_bill / people

final_amount = round(bill_per_person,2)

print(f"Each person shold pay:💲{final_amount}")





#=======================================================================================================



#観点1:正常値を入力したら？　

# 入力/💲150　　チップ割合10%、　人数5人
# 期待/33.0💲




#観点2:合計金額にスペースだけ入れたら？

#入力/" "(スペースひとつ)
#期待/ ValueError が発生する





#観点３:人数を0にしたら?

#入力/💲150　　チップ割合10%、　人数0人
#期待/エラー




#観点4:チップ割合を0にしたら?

#入力/💲150　　チップ割合0%、　人数５人
#期待/💲30
