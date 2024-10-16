try:
    print(0/0)
    assert 1 != 1, 'uno no es igual uno'
except AssertionError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)    

print('hola')
