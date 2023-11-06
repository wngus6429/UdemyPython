r = [1,2,3,4,5,1,2,3]
print(r.index(3)) #3이 어디잇노? 2번째에 잇지
print(r.index(3, 3)) #3번째에 있는 4부터 검색 해주세요
print(r.count(3))

if 5 in r: #r안에 5가 있다면 밑에 실행
    print("exit")
r.sort()
print(r)
r.reverse()
print(r)
print("#####################")
s = "My name is Park"
to_split = s.split(" ") #공백을 기준으로 나눠라
print(to_split)
print("#####################")
x = ' ##'.join(to_split) # ##을 기준으로 연결해라
print(x)
# print(help(list))

# 리스트 복사
i = [1,2,3,4,5]
j = i
j[0] = 100  #위치 참조값으로 넘겨서 그렇다
print("j=",j)
print('i=',i)
print("################")
x = [1,2,3,4,5]
y = x.copy() #혹은 y = x[:]
y[0] = 100
print('y=', y)
print('x=', x)

X = 20
Y = X
Y = 5  #수치전달 하면 ID가 다르다
print(id(X)) # 터미널 보면 id나오는데
print(id(Y)) # 각각 다른데 보존되어 있다는거
print(Y)
print(X)

X = ['a', 'b']
Y = X
Y[0] = "p"
print(id(X)) #참조 전달하면 id가 같고
print(id(Y))
print(Y)
print(X)

print("#####################")
#택시
seat = []
min = 0
max = 4
print(min <= len(seat) < max)
seat.append("p")
print(min <= len(seat) < max)
print(len(seat))
seat.append("p")
seat.append("p")
seat.append("p")
seat.append("p")
print(len(seat))
print(min <= len(seat) <= max)
seat.pop(0)
print(seat)
print(min <= len(seat) <= max)