s = "My name is Park Juhyun. Hi Park"
print(s)

is_start = s.startswith("My")
print(is_start)
is_start = s.startswith("X")
print(is_start)

print("########")
print(s.find("Park"))    #앞에서 찾음. 위치 출력
print(s.rfind("Juhyun")) #뒤에서 찾음. 위치 출력
print(s.count("Park"))
print("########")
print(s.capitalize()) #맨 앞글자 빼고 모두 소문자
print(s.title()) # 단어 앞글자만 대문자, 나머지 소문자
print(s.upper()) #모두 대문자
print(s.lower()) #모두 소문자
print(s.replace("Park", "Pretty"))
print("######################")

print('a is {}'.format('a'));
print('a is {} {} {}'.format(1,2,3));
print('a is {0} {1} {2}'.format(1,2,3));
print('a is {2} {1} {0}'.format(1,2,3));
print("My name is {0} {1}".format('jun','sakai'));
print('My name is {0} {1}. Watashi ha {1} {0}'.format("jun", "sakai")) 
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name="jun", family="sakai")) 

print(1)   #숫자1
print("1") #문자1
x = str(1)
print(type(x))
g = str(True);
print(type(g))