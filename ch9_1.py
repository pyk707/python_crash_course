class Restaurant:

    def __init__(self, restaurant_name, cusine_type):
        self.name = restaurant_name
        self.type = cusine_type

    def describe_restaurant(self):
        print(f"My restaurant is {self.name}")
        print(f"We have a lot of {self.type}")

    def open_restaurant(self):
        print(f"{self.name} is open")

hk = Restaurant("hk", "American food")
yk = Restaurant("yk", "Korean food")
jk = Restaurant("jk", "Chiness food")

print(hk.describe_restaurant())
print(yk.describe_restaurant())
print(jk.describe_restaurant())

