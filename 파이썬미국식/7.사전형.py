datadict = { "juhyun": "good", "whatscore":100}

print(datadict.items())
print('아이템', list(datadict.items())) 
print(datadict.keys())
print('키', list(datadict.keys()))
print(datadict.values())
print(datadict)
print("juhyun" in datadict)

tu = (1, 2, 3, 4, 5)
print(tu[1:])