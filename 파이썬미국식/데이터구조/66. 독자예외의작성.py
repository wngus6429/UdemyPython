class UpperCaseError(Exception):
    pass

def check_uppercase():
    words = ['HELLO', 'WORLD', 'PYTHON', 'java']
    for word in words:
        if not word.isupper():
            raise UpperCaseError(word)

try:
    check_uppercase()
except UpperCaseError as e:
    print("Caught an UpperCaseError: {}".format(e))