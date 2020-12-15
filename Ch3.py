""" #Ch3

bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle[0].title())
print()

motocycles = ['honda','yamaha','suzuki']
print(motocycles)
print()

motocycles.append('ducati')
print(motocycles)
print()

motocycles.insert(0, 'ducati')
print(motocycles)
print()

#del, pop, remove
del motocycles[0]
print(motocycles)
print()

motorcycles = ['honda', 'yamaha', 'suzuki'] # ①
print(motorcycles)
print()

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print()

motorcycles.remove('yamaha')
print(motorcycles)
print() """

#sort, sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print()

cars.sort()
print(cars)
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))