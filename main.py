def calculate_total(price, quantity):
    total = price * quantity
    return total

def calculate_total(price, quantity):
    print(price * quantity)

def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(500, 3)
tax = result * 0.2

print(result)
print(tax)

def check_number(number):
    if number < 0:
        return "Отрицательное"

    return "Неотрицательное"

print(check_number(-5))
print(check_number(10))

def show_message():
    print("Готово")

result = show_message()

print(result)