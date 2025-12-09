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
