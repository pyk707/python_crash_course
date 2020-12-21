prompt = "나이를 입력하세요"
prompt += "\n(종료하고 싶으면 아무 문자나 입력하세요.): "


ticket_active = True
while ticket_active:
    age = input(prompt)
    
    if age.isalpha():
        print("프로그램을 종료합니다.")
        ticket_active = False
    else:
        if age.isdigit():
            age2 = int(age)
            if 0 < age2 < 3:
                print("무료입니다. ")
            elif 3 <= age2 <= 12:
                print("$10")
            elif age2 > 12:
                print("$15")
                