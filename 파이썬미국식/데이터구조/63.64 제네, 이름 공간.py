def g():
    for i in range(10):
        yield i

g = g()

print(type(g)) # <class 'generator'>
print(next(g)) #0
print(next(g)) #1
print(next(g))# 2
print(next(g))# 3

# tuple 안쓰면 제네레이터고 쓰면 튜플이고 ㅋㅋ

f = (i for i in range(10))
print(type(f)) # <class 'generator'>
print(next(f)) #0
print(next(f)) #1
print(next(f)) #2
print(next(f)) #3

# 튜플로 하고 싶으면 앞에 tuple 적으면됨
f = tuple(i for i in range(10))
print(type(f)) # <class 'tuple'>
print(f) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 이건 튜플이네
h = (i for i in range(10) if i % 2 == 0)
for x in h:
    print(x)
# 0
# 2
# 4
# 6
# 8

# 괄호 **()`**만 있고 앞에 아무것도 없으면 → 제네레이터
# 괄호가 tuple(), list(), set() 등 생성자 함수의 인자라면 → 그 자료형

(i for i in range(10))   # 제네레이터
list(i for i in range(10))  # 리스트
set(i for i in range(10))   # 집합
tuple(i for i in range(10)) # 튜플