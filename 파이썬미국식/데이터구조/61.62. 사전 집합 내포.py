w = ['mon', 'tue', 'wed']
f = ['coffe', 'milk', 'water']

d = {}
for x, y in zip (w, f):
    d[x] = y
# {'mon': 'coffe', 'tue': 'milk', 'wed': 'water'}
print(d)

# 위와 똑같이
d = { x:y for x, y in zip(w,f)}
# {'mon': 'coffe', 'tue': 'milk', 'wed': 'water'}
print(d)


#######################################

s = set()

for i in range(10):
    s.add(i)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)

# 위와 똑같이
s = {i for i in range(10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)

#######################################

c = set()

for i in range(10):
    if i % 2 == 0:
        c.add(i)
# {0, 2, 4, 6, 8}
print(c)

# 위와 똑같이
c = {i for i in range(10) if i % 2 == 0}
# {0, 2, 4, 6, 8}
print(c)