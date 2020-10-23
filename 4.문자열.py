print('hello')
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("hello. \n How are you?")
print(r'c:\name\name')  # 앞에 r 없으면 \n을 줄바꿈으로 인식함

print("###########")
print("""\
line1
line2
line3\
""")  # 큰 따옴표 3개를 넣으면 이런식으로 \n 안 적어도됨
print("###########")  # 백슬래쉬 \ 는 다음 문장부터 출력하라는 의미

print("Hi" * 3 + "Mike")  # HiHiHiMike

print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')

s = 'aaaaaaaaaaaaaaaaa' \
    'bbbbbbbbbbbbbbbbb'
print(s)
