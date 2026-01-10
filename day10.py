#辞書と関数を使った電卓プログラム

def add(n1, n2):
    return n1 + n2


# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values.
# Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# TODO: Use the dictionary operations to perform the calculations.
# Multiply 4 * 8 using the dictionary

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operations_symbol = input("Pick an operation: ")

        if operations_symbol not in operations:
            print("+, -, *, / のいずれかを入力してください")
            continue

        num2 = float(input("What is the next number?: "))

        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()


####################################################################################################


#観点1:　正常値

# 入力/　What is the first number?: 5   Pick an operation: *  What is the next number?: 7
# 期待/  5.0 + 7.0 = 12.0




#観点2: 異常値　スペースを入れると？

#入力/　What is the first number?:" "
#期待/ バリューエラーと表示される




#観点3: 異常値　符号を入れると？

#入力/ What is the first number?:　+
#期待/　バリューエラーと表示される




#観点4:　異常値 数字を入れると？

#入力/　Pick an operation: 4
#期待/　キーエラーと表示される



#観点5:　異常値 スペースを入れると？

#入力/　Pick an operation:" "
#期待/　キーエラーと表示される

