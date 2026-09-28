import os

print(os.environ.get("PATH"))

for name, value in os.environ.items():
    print(name, "=", value)