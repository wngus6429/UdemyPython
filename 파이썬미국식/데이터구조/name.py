animal = "cat"

def f():
    """Test Func Doc"""
    print(f.__name__) # f
    print(f.__doc__) # Test Func Doc

f()
print("Global:", __name__) # __main__