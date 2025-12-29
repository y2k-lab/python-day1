# Day8: Caesar Cipher 完全版

# アルファベット一覧
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

# 暗号化/復号の関数
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""  # 結果を入れる変数

    # 文章を1文字ずつ処理
    for letter in original_text:

        # 文字がアルファベットかチェック
        if letter in alphabet:

            # decode の場合は shift を逆に
            if encode_or_decode == "decode":
                shift = -shift_amount
            else:
                shift = shift_amount

            # 文字の位置をずらす
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)  # 26文字を超えたら戻す
            output_text += alphabet[shifted_position]

        else:
            # アルファベット以外はそのまま追加（空白、記号など）
            output_text += letter

    # 結果を表示
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# プログラムを続けるかのスイッチ
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # 関数を呼ぶ
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # 続けるか確認
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        should_continue = False
        print("Goodbye!")

#########################################################################################################


#観点1: 正常値1

# 入力/ encode  yoitenki  7
# 期待/ fvpalurp



#観点2: 正常値2

#入力/ decode  fvpalurp  7
#期待/ yoitenki



#観点3: 異常値3

#入力/　メッセージが空白の場合
#期待/　Here is the decoded result:と表示される。




#観点4: 異常値2

#入力/ shift numberが空白の場合
#期待/　バリューエラーが表示される




#観点5: 異常値3

#入力/ メッセージに数字が入った場合→ encode yo1tenki shift number7
#期待/　入力した数字がそのまま出力される→fv1alurp（数字1がそのまま含まれる）




#観点6: 異常値4

#入力/ shift numberにアルファベットが入った場合
#期待/　バリューエラーと表示される
