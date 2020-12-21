def question_toping():
    toping = input("무슨 토핑을 먹을래요?")
    if toping == "quit":
        return -1
    return toping

def say_toping(toping):
    return print(toping + "을 피자에 추가하겠습니다.")

if __name__ == "__main__":
    while True:
        toping = question_toping()
        if toping == -1:
            break
        say_toping(toping)