animal = 'cat'
# def f():
#     print(animal)
#     animal = 'dog'
#     print('after', animal)
#                 #   ^^^^^^
#     # UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value
# f()

# #위와 같이 하면 에러남
# #아래와 같이 하면 괜찮음

# animal = 'cat'
# def f():
#     # print(animal)
#     animal = 'dog'
#     print('after', animal)

# f()