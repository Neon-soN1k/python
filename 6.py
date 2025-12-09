#Задание1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matrix:")
for row in matrix:
    print(row)
odd_numbers = []
for row in matrix:
    for item in row:
        if item % 2 != 0:
            odd_numbers.append(str(item))
print("\nнечётные числа matrix", " ".join(odd_numbers))
even_count = 0
for row in matrix:
    for item in row:
        if item % 2 == 0:
            even_count += 1
print(f"\nкол-во чётных: {even_count}")
#Задание2
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
rows = len(matrix_1)
cols = len(matrix_1[0])
answer_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]
print(f"[[{', '.join(map(str, answer_matrix[0]))}], [{', '.join(map(str, answer_matrix[1]))}]]")
for i in range(rows):
    row_sum = sum(answer_matrix[i])
    print(f"{answer_matrix[i]} сумма строки: {row_sum}")
#Задание3
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
for row in fruits:
    for fruit in row:
        if fruit.isupper():
            print(fruit)
#Задание4

#Задание5
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Введите значение элемента [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)
print("\nВаш двумерный массив:")
for row in matrix:
    print(row)
print("\nВаш двумерный массив (формат из примера):")
for row in matrix:
    print(row) # В Python списки выводятся в формате [a, b, c], что соответствует примеру
