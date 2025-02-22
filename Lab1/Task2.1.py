a, b = map(float, input("Введите стороны прямоугольника: ").replace(',', '.').split())

S = a * b
P = 2 * (a + b)

# Вывод результата
print(f"S = {S:.2f}")
print(f"P = {P:.2f}")