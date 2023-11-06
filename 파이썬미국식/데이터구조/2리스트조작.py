s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])
s[0] = 'X'
print(s)
print(s[2:5])
s[2:5] = ["S" , "X", "K"]
print(s)
s[2:5] = [] #지우기 공백
print(s)
s[:] = [] # : 처음부터 끝까지
print(s)
print("#############################")
n = [1,2,3,4,5,6,7,8,9,10]
n.append(11) #젤 뒤에
print(n)
n.insert(0, 200)
print(n)
n.pop() #젤 뒤에꺼 꺼내기
print(n)
n.pop(0) #원하는거 삭제
print(n)
del n[0] #맨 앞 삭제, del은 주의해서 사용, del n 하면 n 존재 삭제
print(n)
print("#############################")
#append는 맨 뒤에
#insert는 앞에
#pop은 삭제 , 디폴트 맨뒤, pop(0) 이런식으로 지정가능

f = [1,2,3,4,5]
f.remove(2)
print(f)
print("################################")
a= [1,2,3,4,5]
b= [6,7,8,9,10]
print(a+b)
a += b
print(a)
print("################################")
x= [1,2,3]
y= [3,5,6]
x.extend(y)
print(x)