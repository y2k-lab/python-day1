import random

letters = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcom to the PyPassword Generator!")

#最小改造
try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
except ValueError:
 print("数字を入力してください")

nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many number would you like?\n"))

password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)


password = "".join(password_list)
print("Your password is:" + password)



######################################################################################################




#観点1:letter,number,symbolにそれぞれ０を入力したら？　

# 入力/letterに0 numberに0 symbolに0
# 期待/Yor password is:とだけ表示される




#観点2:スペースだけ入れたら？

#入力/letterに" "(半角スペースひとつ)
#期待/数字を入力してくださいと表示され、処理が終了する




#観点3:symbolに数字以外を入力

#入力/？
#期待/バリューエラーが表示される




#観点4:正常値

#入力/letter 5 symbol 3 numbar 1
#期待/u2&jzq&+h 英字5個　記号3個　数字1個


