def square(number):
    return number ** 2

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))