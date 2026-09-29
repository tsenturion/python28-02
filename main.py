def greet():
    print("Здравствуйте")

print(type(greet))

greet()

print(greet)
print(greet())

def greet(name):
    print("Здравствуйте,", name)

say_hello = greet

say_hello("Анна")

def get_number():
    return 100

value = get_number
result = get_number()
print(value())

def greet(name):
    return "Здравствуйте, " + name

def execute(function, value):
    return function(value)

result = execute(greet, "Анна")

print(result)
operation = greet

def start():
    print("Запуск")

def stop():
    print("Остановка")

actions = [start, stop]

print(actions[0])
actions[0]()
actions[1]()

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operation = add

print(operation(10, 5))
operation = multiply
print(operation(10, 5))

def create_operation():
    def operation():
        print("Операция выполнена")

    return operation
result = create_operation()
result()