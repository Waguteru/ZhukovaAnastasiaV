def triangle_area(base, height):
    # вычислим площадь прямоугольного треугольника
    return 0.5 * base * height

def rectangle_area(length, width):
    # вычислим площадь прямоугольника
    return length * width

X = float(input("Введите длину стороны X: "))  
Y = float(input("Введите длину стороны Y: "))  
Z = float(input("Введите длину стороны Z: "))  
T = float(input("Введите длину стороны T: "))  

# Площадь прямоугольного треугольника
area_triangle = triangle_area(X, Y)

# Площадь прямоугольника
area_rectangle = rectangle_area(Z, T)

total_area = area_triangle + area_rectangle

print(f"Площадь четырехугольника: {total_area}")


def to_octal_with_leading_zeros(num):
    if num < 0:
        raise ValueError("Число должно быть неотрицательным")
    octal_str = oct(num)[2:]  # Преобразуем в восьмеричное и убираем "0o"
    return octal_str.zfill(10)  # заполним нулями до 10 знаков

number = 83
octal_code = to_octal_with_leading_zeros(number)
print(f'Восьмеричное представление {number} представляет собой: {octal_code}')

