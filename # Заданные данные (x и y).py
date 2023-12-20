# Заданные данные (x и y)
x = [1, 2, 3, 4, 5]
y = [2, 5, 10, 17, 26]

# Функция для вычисления коэффициентов параболы через метод наименьших квадратов
def parabolic_coefficients(x, y):
    n = len(x)
    x2 = [xi ** 2 for xi in x]
    x3 = [xi ** 3 for xi in x]
    x4 = [xi ** 4 for xi in x]
    
    sum_x = sum(x)
    sum_x2 = sum(x2)
    sum_x3 = sum(x3)
    sum_x4 = sum(x4)
    sum_y = sum(y)
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])
    sum_x2y = sum([xi ** 2 * yi for xi, yi in zip(x, y)])
    
    a = (sum_x2y * sum_x2 - sum_xy * sum_x3) / (sum_x4 * n - sum_x2 ** 2)
    b = (sum_xy - a * sum_x2) / sum_x
    c = (sum_y - sum_x * b - sum_x2 * a) / n
    
    return a, b, c

# Вычисляем коэффициенты параболы
a, b, c = parabolic_coefficients(x, y)

# Создаем новый набор точек для интерполяции
x_new = [i/10 for i in range(10, 51)]  # Новые значения x от 1.0 до 5.0 с шагом 0.1
y_new = [a * xi**2 + b * xi + c for xi in x_new]

# Вывод результатов
print("Исходные данные:")
print("x =", x)
print("y =", y)

print("\nНовые данные после интерполяции:")
print("x_new =", x_new)
print("y_new =", y_new)
