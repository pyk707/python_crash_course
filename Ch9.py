##클래스
# 파이썬에서는 클래스 이름의 첫 글자를 대문자로

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('vally', 15)

print(f"my dog's name is {my_dog.name}")
print(my_dog.sit())
print(my_dog.roll_over())