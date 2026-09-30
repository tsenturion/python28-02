numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))