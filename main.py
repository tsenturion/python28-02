numbers = [1, 2, 3]

result = filter(lambda number: number > 1, numbers)

print(type(result))
print(list(result))
numbers = [1, 2, 3, 4]

result = filter(lambda number: number % 2 == 0, numbers)

for number in result:
    print(number)