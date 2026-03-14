import math

r_value = float(input("반지름(r) 입력하세요: "))


circumference_value = r_value * 2 * math.pi

area_value = 2 * math.pi * (r_value ** 2)

print(f"반지름이 {r_value}인 원의 둘레: {circumference_value}")
print(f"반지름이 {r_value}인 원의 넓이: {area_value}")
