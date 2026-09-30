names = ["Анна", "Иван"]
ages = [20, 25]

result = zip(names, ages)

print(type(result))
print(list(result))
names = ["Анна", "Иван"]
ages = [20, 25]

for name, age in zip(names, ages):
    print(name, age)
    
names = ["Анна", "Иван"]
ages = [20, 25]
cities = ["Москва", "Казань"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)
    
names = ["Анна", "Иван", "Мария"]
ages = [20, 25]

result = list(zip(names, ages))

print(result)

names = ["Анна", "Иван", "Мария"]
ages = [20, 25]

#result = zip(names, ages, strict=True)

print(list(result))

keys = ["name", "age", "city"]
values = ["Анна", 25, "Москва"]

pairs = zip(keys, values)
user = dict(zip(keys, values))
print(list(pairs))
print(user)

