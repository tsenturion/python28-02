numbers = [1, 2, 3]

result = map(lambda number: number * 2, numbers)
result = list(
    map(lambda number: number * 2, numbers)
)
print(list(result))
print(list(result))

result = map(
    lambda value: value.strip().lower().replace(" ", "_"),
    values
)

def normalize_name(value):
    value = value.strip()
    value = value.lower()
    return value.replace(" ", "_")