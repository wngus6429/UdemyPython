# animal = 'cat'
# def f():
#     print(animal)
#     animal = 'dog'
#     print('after', animal)
#                 #   ^^^^^^
#     # UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value
# f()

#위와 같이 하면 에러남
#아래와 같이 하면 괜찮음

animal = 'cat'
def f():
    # print(animal)
    animal = 'dog'
    print('after', animal)

f()

##################################

animal = 'cat'
def f():
    animal = 'dog'
    print('local:', locals()) # local: {'animal': 'dog'}

f()
print('global', animal) # global cat

##################################

animal = 'cat'
def f():
    # animal = 'dog'
    print('local:', locals()) # local: {}

f()
print('global', animal) # global cat

# globals 뒤에 s 주의
print('globals 주의:', globals()) 
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': 
# <_frozen_importlib_external.SourceFileLoader object at 0x000001999ECEBFE0>, 
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' 
# (built-in)>, '__file__': 'c:\\Users\\wngus\\OneDrive\\Documents\\Github\\
# UdemyPython\\파이썬미국식\\데이터구조\\64.65.66 스코프, 예외, 예외작성.py',
# '__cached__': None, 'animal': 'cat', 'f': <function f at 0x000001999ECA8A40>} 