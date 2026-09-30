from mytools import calculator
import mytools.calculator

from mytools.calculator import add

from mytools.text_utils import normalize

print(add(10, 20))
print(normalize("  PYTHON  "))

print(add(10, 20))

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))

result = mytools.calculator.add(10, 20)

print(result)