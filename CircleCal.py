# CircleCal.py
import math

radius = float(input("원의 반지름을 입력하세요: "))

# 둘레 구하기 (2 * pi * r)
circumference = 2 * math.pi * radius

# 넓이 구하기 (pi * r^2)
area = math.pi * (radius ** 2)

print("반지름이 {0}인 원의 둘레: {1}".format(radius, circumference))
print("반지름이 {0}인 원의 넓이: {1}".format(radius, area))