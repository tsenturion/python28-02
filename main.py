outer = 1

while outer <= 3:
    inner = 1

    while inner <= 3:
        print("outer =", outer, "inner =", inner)

        if inner == 2:
            break

        inner += 1

    outer += 1