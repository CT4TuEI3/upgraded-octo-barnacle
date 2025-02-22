import math

a, b, c = map(float, input("Введите стороны треугольника: ").replace(",", ".").split())

P = a + b + c

# Вычисление площади по формуле Герона
p = P / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"S = {S:.2f}")
print(f"P = {P:.2f}")
