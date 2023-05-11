#튜플은 수치를 바꿀 수 없다.
t = (1,2,3,4,1,2)
print(t)
print(type(t))
#t[0] = 100 #튜플은 이렇게 넣는거 불가능
print(t[0])
print(t[0:2])
print(t.index(1))
print(t.index(1,1))
print(t.count(1))
#print(help(tuple))

g = ([1,2,3], [4,5,6])
print(g)
print(g[0])
print(g[0][0])
g[0][0] = 100 #리스트 안에거는 바꾸기 가능하니까.
print(g)
print("#######################################")

#튜플 언패킹
num_tuple = (10,20)
print(num_tuple)
x,y = num_tuple
print(x, y)
x,y = 10, 20 #튜플은 소괄호 안 해도 됨
print(x, y)
min, max = 0, 100
print(min,max)
print("#######################################")
a,b,c,d,e,f = "Mike", '1', '1', '1', 'e', 'f' #이렇게 길게쓰면 안 좋음

i = 10 #i과 j바꾸기
j = 20
temp = i
i = j
j = temp
print(i, j)
# 위에처럼 하면 되게 길어지니 안 좋음
a = 100
b = 200
print(a,b)
a, b = b, a
print(a, b)
print("#######################################")

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')
print(chose_from_two)
print(answer)