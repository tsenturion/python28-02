numbers = [10, 20, 30, 40]
target = 30
for number in numbers:
    if number == target:
        print("Значение найдено")
        break
if target in numbers:
    print("Значение найдено")