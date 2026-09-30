from functools import reduce
numbers = [10, 20, 30]
result = reduce(
    lambda accumulated, current: accumulated + current,
    numbers
)
print(result)