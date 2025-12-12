#Задание1
data = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]
print("--- Начальный массив ---")
for row in data:
    print(row)
modified_data = []
for row in data:
    new_row = []
    for item in row:
        if item == 'folder':
            continue
        elif item == 'data.accdb':
            new_row.append('data.sql')
        else:
            new_row.append(item)
    modified_data.append(new_row)
print("\n--- После удаления папок и замены data.accdb ---")
for row in modified_data:
    print(row)
py_files = []
for row in data:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)
print("\n--- Все файлы .py ---")
print(py_files)
new_js_files = []
for row in data:
    for item in row:
        if item.endswith('.js'):
            new_js_files.append('new_' + item)

print("\n--- Все файлы .js с префиксом new_ ---")
print(new_js_files)
#Задание2
word_numb = ["ноль", "один", "два", "три", "четыре", "пять",
"шесть", "семь", "восемь", "девять"]
try:
    n = int(input("Введите число n от 0 до 9: "))
    if 0 <= n <= 9:
        print(f"Элементы списка от первого до {n}-го (включительно):")
        for i in range(n + 1):
            print(word_numb[i])
    else:
        print('Введите число <= 9')
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите целое число.")
#Задание3
bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
decimal_numbers = []
print("Десятичные представления элементов списка:")
for binary_str in bin_sy:
    decimal_num = int(binary_str, 2)
    decimal_numbers.append(decimal_num)
    print(decimal_num)
max_num = max(decimal_numbers)
min_num = min(decimal_numbers)
print(f"\nМаксимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
#Задание4
A = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, 'error', 8]
]
print(f"Исходная матрица A:\n{A}\n")
for row_index, row in enumerate(A):
    for col_index, element in enumerate(row):
        if isinstance(element, str):
            replacement_value = len(element)
            A[row_index][col_index] = replacement_value
            print(f"Элемент '{element}' по адресу [{row_index}][{col_index}] заменен на число: {replacement_value}")
print(f"\nИзмененная матрица A:\n{A}\n")
total_sum = 0
for row in A:
    for element in row:
        total_sum += element
print(f"Сумма всех элементов матрицы: {total_sum}")
#Задание5
matrix = [
    [10, 2, 3],
    [4, 50, 6],
    [7, 8, 90]
]
print(f"Исходная матрица:\n{matrix}\n")
diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_element = matrix[i][i]
    diagonal_sum += diagonal_element
    print(f"Добавляем элемент [{i}][{i}]: {diagonal_element}")
print(f"\nСумма чисел по главной диагонали: {diagonal_sum}")
secondary_diagonal_sum = 0
n = len(matrix) # Размер матрицы (3)
print("\n--- Расчет побочной диагонали ---")
for i in range(n):
    element = matrix[i][n - 1 - i]
    secondary_diagonal_sum += element
    print(f"Добавляем элемент [{i}][{n - 1 - i}]: {element}")
print(f"\nСумма чисел по побочной диагонали: {secondary_diagonal_sum}")
