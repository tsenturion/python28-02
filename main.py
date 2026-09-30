def generate_even_numbers(limit):
    number = 0

    while number < limit:
        if number % 2 == 0:
            yield number

        number += 1
        
for number in generate_even_numbers(10):
    print(number)
    
numbers = (
    number
    for number in range(10)
    if number % 2 == 0
)

def generate_numbers():
    yield 1
    yield 2
    yield 3
    
for number in generate_numbers():
    print(number)
    
    
    
def generate_numbers(limit):
    number = 0

    while number < limit:
        if number == 3:
            return

        yield number
        number += 1
        
print(list(generate_numbers(10)))

pairs = [
    (x, y)
    for x in range(3)
    for y in range(2)
]

print(pairs)
pairs = []

for x in range(3):
    for y in range(2):
        pairs.append((x, y))