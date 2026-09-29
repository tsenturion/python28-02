def show_values(*args):
    print(type(args))
    print(args)
    
show_values(10, 20, 30)

def show_values(*args):
    for value in args:
        print(value)

show_values(10, 20, 30)
show_values(10)
show_values(10, 20, 30, 40, 50)
show_values()

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

result = calculate_sum(10, 20, 30)

print(result)

def show_message(title, *messages):
    print("Заголовок:", title)

    for message in messages:
        print(message)
        
show_message(
    "Отчёт",
    "Сервис запущен",
    "Соединение установлено",
    "Проверка завершена"
)

def calculate(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
#calculate(numbers)
result = calculate(*numbers)
calculate(10, 20, 30)
print(result)