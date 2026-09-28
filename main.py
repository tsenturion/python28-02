import dis

def calculate():
    x = 10
    y = 20
    return x + y

dis.dis(calculate)