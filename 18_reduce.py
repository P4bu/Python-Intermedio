import functools

numbers = [1,2,3,4,5]

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

