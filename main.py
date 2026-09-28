source = "print(5 + 7)"

print(type(source))

code = compile(source, "<example>", "exec")

print(type(code))