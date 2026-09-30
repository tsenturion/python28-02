def generate_numbers():
    counter = 0
    
    while counter < 5:
        yield counter
        counter += 1
        
        
generator = generate_numbers()
print(next(generator))
print(generator.gi_frame.f_locals)
print(generator.gi_frame.f_lasti)


print(next(generator))
print(generator.gi_frame.f_locals)
print(generator.gi_frame.f_lasti)

def generate_names():
    yield "Анна"
    yield "Иван"
    yield "Мария"
    
for index, name in enumerate(generate_names()):
    print(index, name)