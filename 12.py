#Задание1
x = lambda a, b: a * b
print(x(2, 3))
print(x(5, 5))
print(x(10, 0.5))
№задание2
try:
    count_of_numbers_input = input("Всего чисел будет: ")
    count_of_numbers = int(count_of_numbers_input)
except ValueError:
    print("Ошибка ввода: введите корректное целое число для количества элементов.")
    exit()
numbers_list = []
print(f"Введите {count_of_numbers} чисел:")
for i in range(count_of_numbers):
    while True:
        num_input = input(f"Число #{i+1}: ")
        try:
            num = int(num_input)
            numbers_list.append(num)
            break
        except ValueError:
            print("Ошибка ввода: введите целое число.")
print(f"\nИсходный список чисел: {numbers_list}")
filtered_list = list(filter(lambda item: item % 3 == 0 and item % 5 == 0, numbers_list))
print(f"\nОтфильтрованный список (кратные 3 и 5): {filtered_list}")
