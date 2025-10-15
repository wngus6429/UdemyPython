l = [1,2,3]
i = 5

try:
    l[i]
except:
    print("dont worry")

try:
    () 
except IndexError as ex:
    print("dont worry {}".format(ex)) # dont worry list index out of range
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other {}".format(ex))
finally:
    print("finally")

print("last")