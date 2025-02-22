import math

# 6. Площадь и периметр окружности

d_input = input("Введите диаметр окружности: ").replace(',', '.')
d = float(d_input)

r = d / 2

# Вычисление площади и периметра
S = math.pi * r**2
P = math.pi * d

print(f"S = {S:.2f}")
print(f"P = {P:.2f}")
