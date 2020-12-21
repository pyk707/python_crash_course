def greet_user(username):
    """간단한 환영 인사를 표시합니다"""
    print(f"Hello, {username.title()}!")

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title}.")


if __name__=="__main__":
    name = input("니 이름이 뭐니? ")
    greet_user(name)
    print()
    
    ani_type = input("동물 타입? ")
    ani_name = input("동물 이름? ")
    describe_pet(ani_type, ani_name)
    print()