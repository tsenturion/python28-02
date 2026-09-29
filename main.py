file_exists = True
file_is_empty = False

if not file_exists:
    print("Файл не найден")
elif file_is_empty:
    print("Файл существует, но не содержит данных")
else:
    print("Файл найден и содержит данные")