height = int(input("몇 cm 인가요"))
weight = int(input("몇 kg 인가요"))
result = weight / ((height / 100) ** 2)
print(format(result, ".2f"))  # 소수점 2자리까지 표시
