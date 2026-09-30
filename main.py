def execute(function, value):
    return function(value)

result = execute(lambda number: number * 2, 10)

print(result)