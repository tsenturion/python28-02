source = "x = 10\nprint(x * 2)"

code = compile(source, "<example>", "exec")

exec(code)