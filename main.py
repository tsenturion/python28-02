def show_settings(**kwargs):
    print(type(kwargs))
    print(kwargs)

show_settings(
    host="localhost",
    port=5432,
    debug=True
)

def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
        
show_settings(
    host="localhost",
    port=5432,
    debug=True
)

def show_settings(**data):
    print(data)
    
def show_data(*args, **kwargs):
    print("Позиционные:", args)
    print("Именованные:", kwargs)
    
show_data(
    10,
    20,
    30,
    name="Анна",
    active=True
)

def create_user(*args):
    print(args)
    
def create_user(name, age, city):
    print(name, age, city)
    
def show_user(name, age):
    print(name)
    print(age)
    
user = {
    "name": "Анна",
    "age": 25
}

show_user(**user)