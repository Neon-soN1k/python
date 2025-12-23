#Задание1
while True:
    user_input = input(">>> число: ")
    try:
        x = int(user_input)
        if x > 0:
            print("Вывод: ", end="")
            for i in range(x + 1):
                print(i, end=" ")
            print()
            break
        else:
            print(f">>> {user_input} - не число. Повторите ввод.")
    except ValueError:
        print(f">>> {user_input} - не число. Повторите ввод.")
#Задание2
any_list = [4, 3.2, 16, 9, 13.5, 67]
for index, element in enumerate(any_list):
    try:
        result = element / index
        print(f"{element} / {index} = {result}")
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент: {element}")
#Задание3
numbers = []
print("Введите 5 чисел (нечисловые значения будут проигнорированы):")
while len(numbers) < 5:
    user_input = input(f"Введите число {len(numbers) + 1}: ")
    try:
        num = int(user_input)
        numbers.append(num) 
    except ValueError:
        print(f"'{user_input}' не является числом. Попробуйте еще раз.")
print("\nЧисла в списке:", numbers)
