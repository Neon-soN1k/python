#Задание1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
figure_names = ['круг', 'квадрат', 'треугольник', 'овал']
i = 0
while i < len(m):
    if isinstance(m[i], str) and m[i] in figure_names:
        i += 1
    else:
        m.remove(m[i])

print(m)
#Задание2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)
#Задание3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)
#Задание4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
filtered_mass = [x for x in mass if x >= 0]
asc_sorted_mass = sorted(filtered_mass)
desc_sorted_mass = sorted(filtered_mass, reverse=True)
print(f">>> {asc_sorted_mass}")
print(f">>> {desc_sorted_mass}")
#Задание5
negative_nums = []
positive_nums = []
zeros = []
try:
    count = int(input("Введите количество чисел: "))
    print("Введите числа через пробел или по одному:")
    for _ in range(count):
        num = float(input())
        if num < 0:
            negative_nums.append(num)
        elif num > 0:
            positive_nums.append(num)
        else:
            zeros.append(num)
except ValueError:
    print("Ошибка ввода: введите корректное число.")
    exit()
sum_negative = sum(negative_nums)
print(f"\nСумма отрицательных чисел: {sum_negative}")
if positive_nums:
    avg_positive = sum(positive_nums) / len(positive_nums)
else:
    avg_positive = 0
print(f"Среднее арифметическое положительных чисел: {avg_positive}")
modified_zeros = ['*' if x == 0 else x for x in zeros]
print(f"Количество нулей: {len(modified_zeros)}")
print(f"Элементы списка нулей (заменены на '*'): {modified_zeros}")
