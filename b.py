def b_method():
    print("b_method 실행됨.")
    print(__name__)
    if __name__ == "__main__":
        print("b.py의 __main__")