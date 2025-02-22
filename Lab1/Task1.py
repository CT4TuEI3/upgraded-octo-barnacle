import math

def main():
    x = int(input("Введите трехзначное число x: "))
    
    if x < 100 or x > 999:
        print("⚠️Ошибка: число должно быть трехзначным.")
        return
    
    # Разделение числа на цифры
    first_digit = x // 100
    second_digit = (x // 10) % 10
    third_digit = x % 10
    
    # Задача 1
    result1 = (x - first_digit) // 10
    result1 = int(str(result1) + str(first_digit))
    result1 *= 3
    print(f"Результат задачи 1: {result1}")
    
    # Задача 2
    result2 = (x - third_digit) // 10
    result2 = int(str(third_digit) + str(result2))
    result2 *= 2
    print(f"Результат задачи 2: {result2}")
    
    # Задача 3
    result3 = (x % 100) * 10 + first_digit
    result3 += 5
    print(f"Результат задачи 3: {result3}")
    
    # Задача 4
    result4 = (x // 100) * 10 + (x % 10)
    result4 = int(str(second_digit) + str(result4))
    result4 *= 2
    print(f"Результат задачи 4: {result4}")
    
    # Задача 5
    result5 = (x // 100) * 10 + (x % 10)
    result5 = int(str(result5) + str(second_digit))
    result5 *= 2
    print(f"Результат задачи 5: {result5}")
    
    # Задача 6
    result6 = x % 10
    result6 = int(str(result6) + str(second_digit) + str(first_digit))
    result6 = math.sqrt(result6)
    print(f"Результат задачи 6: {result6}")
    
    # Задача 7
    result7 = x % 10
    result7 = int(str(first_digit) + str(second_digit) + str(result7))
    result7 = result7 ** 2
    print(f"Результат задачи 7: {result7}")

main()