def create_user(name, age, city):
    print(name)
    print(age)
    print(city)
    
create_user(
    name="Анна",
    age=25,
    city="Москва"
)

create_user(
    city="Москва",
    name="Анна",
    age=25
)

create_user("Анна", 25, city="Москва")
#create_user(name="Анна", 25, "Москва")

def greet(name):
    print(name)


greet("Анна", name="Мария")