numbers = [1, 2, 3]
result = list(map(lambda number: number * 10, numbers))
result = list(
    filter(lambda number: number % 2 == 0, numbers)
)
names = ["Анна", "Иван"]
ages = [20, 25]
result = list(zip(names, ages))

from functools import reduce

result = reduce(lambda a, b: a + b, numbers)

result = []

for number in numbers:
    result.append(number ** 2)

print(result)

result = list(
    map(lambda number: number ** 2, numbers)
)

numbers = [1, 2, 3, 4, 5]
result = []

for number in numbers:
    if number > 2:
        result.append(number)
        
    numbers = [1, 2, 3, 4, 5]

result = list(
    filter(lambda number: number > 2, numbers)
)


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)

squares = map(
    lambda number: number ** 2,
    even_numbers
)

print(list(squares))