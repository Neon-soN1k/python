#Вариант1_Задание1
try:
    number_str = input("Введите целое число: ")
    number = int(number_str)
    if number < 0:
        number = abs(number)
        print(number)
    elif number == 0:
        number = 1
        print(number)
    else:
        print(number)
except ValueError:
    print("Ошибка: Введите корректное целое число.")
#Вариант1_Задание2
string = input()
if '.' in string or ',' in string:
    print(True)
else:
    print(False)
#Вариант1_Задание3
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
if x % 3 == 0 and y % 3 == 0:
  print(True)
elif x % 3 == 0 or y % 3 == 0:
  print("Одно число делится на 3")
else:
  print(False)
#Вариант2_Задание1
num = int(input())
if num > 100:
  print("*")
elif num >0:
  print("*" * num)
else:
  print("Звездочки не выводятся")
#Вариант2_Задание2
string1 = input()
string2 = input()
if string1 == string2:
  print(True)
else:
  print(False)
#Вариант2_Задание3
r = int(input("Введите значение R (0-255): "))
g = int(input("Введите значение G (0-255): "))
b = int(input("Введите значение B (0-255): "))
if r == 0 and g == 0 and b == 0:
    print("Чёрный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")
#Вариант3_Задание1
num = int(input("Введите число: "))
if num > 0:
    print(f"Результат: {num - 1}, {num}, {num + 1}")
else:
    num = 1
    print(f"Результат: {num - 1}, {num}, {num + 1}")
#Вариант3_Задание2
filename = input("Введите имя файла с расширением (например, 'file.doc'): ")
extension = filename.split('.')[-1].lower()
if extension == 'doc':
    print("Word file")
elif extension == 'py':
    print("Python file")
elif extension == 'txt':
    print("Text file")
else:
    print(f"Неизвестное расширение файла: {extension}")
#Вариант3_Задание3
try:
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    c = float(input("Введите длину стороны C: "))
except ValueError:
    print("Ошибка: введите корректные числовые значения для сторон.")
    exit()
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Треугольник равносторонний (все стороны равны).")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный (две стороны равны).")
    else:
        print("Треугольник разносторонний (все стороны разные).")
else:
    print("Треугольник с заданными сторонами не существует (нарушено правило суммы сторон).")
#Вариант4_Задание1
text = 'important information in one line'
letter = input("Введите букву: ")
if letter in text:
    print(True)
else:
    print(False)
#Вариант4_Задание2
try:
    side1 = float(input("Введите длину первой стороны: "))
    side2 = float(input("Введите длину второй стороны: "))
except ValueError:
    print("Ошибка: введите корректные числовые значения для сторон.")
    exit()
if side1 <= 0 or side2 <= 0:
    print("Ошибка: длины сторон должны быть положительными числами.")
    exit()
if side1 == side2:
    figure_type = "Квадрат"
    area = side1 * side2
    print(f"{figure_type}. Площадь: {area}")
else:
    figure_type = "Прямоугольник"
    area = side1 * side2
    print(f"{figure_type}. Площадь: {area}")
#Вариант4_Задание3
def check_mood(response):  
    positive = ['хорошо', 'нормально', 'отлично']     
    negative = ['плохо', 'не хорошо']   
    response = response.lower()  
    if response in positive:  
        return '😊'  
    elif response in negative:  
        return '🙁'  
    else:  
        return '😐'
user_response = input("Как твои дела? ")  
print(check_mood(user_response))  
#Вариант5_Задание1
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
  result = num1 ** num2
  print(f"Первое число больше. Результат: {result}")
elif num2 > num1:
  result = num2 ** num1
  print(f"Второе число больше. Результат: {result}")
else:
  result = num1 + num2
  print(f"Числа равны. Сумма: {result}")
#Вариант5_Задание2
new_message = "Hello! How are you?"
user_answer = input("Введите ваш ответ на сообщение 'Hello! How are you?': ")
if len(new_message) > 0 and len(user_answer) > 0:
    if new_message[0] == user_answer[0]:
        print(True)
    else:
        print(False)
else:
    print(False) 
#Вариант5_Задание3
try:
    length1 = float(input("Введите длину первого отрезка: "))
    length2 = float(input("Введите длину второго отрезка: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()

if length1 > length2:
    difference = length1 - length2
    print(f"Первый отрезок длиннее второго на **{difference}**.")
elif length2 > length1:
    difference = length2 - length1
    print(f"Второй отрезок длиннее первого на **{difference}**.")
else:
    print("Отрезки **равны**.")
#Вариант6_Задание1
input_string = input("Введите произвольную строку: ")

if len(input_string) > 0:

    first_char = input_string[0]
    last_char = input_string[-1]

    if first_char == last_char:
        print(True)
    else:
        print(False)
else:

    print(False)
#Вариант6_Задание2
try:
    number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Введено не целое число.")
    exit()
result = 0
if number % 2 == 0:
    result = number ** 2
    print(f"Число кратно двум. Результат (число в квадрате): {result}")
elif number % 3 == 0:
    result = number ** 3
    print(f"Число кратно трём. Результат (число в кубе): {result}")
else:
    result = number * 100
    print(f"Число не кратно ни двум, ни трём. Результат (число * 100): {result}")
#Вариант6_Задание3
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()
if num1 < 0 and num2 < 0:
    print(False)
elif num1 >= 0 and num2 >= 0:
    print(True)
elif num1 < 0:
    num1 += 1000
    print(f"Первое число было отрицательным. Результат: num1 = {num1}, num2 = {num2}")
elif num2 < 0:
    num2 += 1000 
    print(f"Второе число было отрицательным. Результат: num1 = {num1}, num2 = {num2}")
#Вариант7_Задание1
input_string = input("Введите произвольную строку: ")
target_chars = ['я', 'и', 'е', 'ю']
if len(input_string) > 0:
    last_char = input_string[-1]
    if last_char in target_chars:
        print(True)
    else:
        print(False)
else:
    print(False)
#Вариант7_Задание2
try:
    a = float(input("Введите длину первой стороны (a): "))
    b = float(input("Введите длину второй стороны (b): "))
    c = float(input("Введите длину третьей стороны (c): "))
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
    exit()
if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print(True)
    else:
        print(False)
else:
    print(False)
#Вариант7_Задание3
try:
    number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Введено не целое число.")
    exit()
last_digit = abs(number) % 10
result = None

print(f"Последняя цифра числа: {last_digit}")
if last_digit == 0:
    result = number ** 10
    print(f"Результат (число в степени 10): {result}")
elif last_digit == 1:
    result = number % 3
    print(f"Результат (деление на 3 с остатком): {result}")
elif last_digit == 2:
    result = number // 2
    print(f"Результат (деление на 2 без остатка): {result}")
else:
    result = number ** 2
    print(f"Результат (число в степени 2): {result}")
#Вариант8_Задание1
def check_password(password):  
    if len(password) < 8 or password == 'qwerty123':  
        return False  
    return True  
password = input("Введите пароль:")  
print(check_password(password))  
#Вариант8_Задание2
pc_number = 777
try:
    user_num1 = float(input("Введите первое число: "))
    user_num2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Введите корректные числа.")
    exit()
condition1 = (user_num1 < pc_number) and (user_num2 > pc_number)
condition2 = (user_num2 < pc_number) and (user_num1 > pc_number)
if condition1 or condition2:
    print(True)
else:
    print(False)
#Вариант8_Задание3
lamp_1 = 0
lamp_2 = 0
user_choice = input("Какую лампочку зажечь? (Введите '1' или '2'): ")
if user_choice == "1":
    lamp_1 = 1
    print(f"Лампочка 1 зажжена. Статус: lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
elif user_choice == "2":
    lamp_2 = 1
    print(f"Лампочка 2 зажжена. Статус: lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
else:
    print("Обе лампочки не горят")
    print(f"Статус: lamp_1 = {lamp_1}, lamp_2 = {lamp_2}")
#Вариант9_Задание1
switch_1 = False
switch_2 = False
user_input = input("Включить? ")
if user_input.lower() == "да":
    switch_1 = True
    switch_2 = True
    print("Всё включено")
    print(f"switch_1 = {switch_1}")
    print(f"switch_2 = {switch_2}")
else:
    print(f"switch_1 = {switch_1}")
    print(f"switch_2 = {switch_2}")
#Вариант9_Задание2
try:
    number = int(input("Введите целое число: "))
    if number > 0:
        if number % 2 == 0:
            print(True, "even")
        else:
            print(True, "odd")
    else:
        print(False)
except ValueError:
    print("Ошибка ввода: введено не целое число.")
#Вариант9_Задание3
input_string = input("Введите строку: ")
if input_string:
    if input_string[0] == '/':
        print("command")
    else:
        print("It’s string")
else:
    print("Была введена пустая строка. Это строка.")
#Вариант10_Задание1
input_string = input("Введите строку: ")
string_length = len(input_string)
if string_length == 0:
    print(None)
elif string_length <= 5:
    print("short")
elif 6 <= string_length <= 10:
    print("normal")
else:
    print("long")
#Вариант10_Задание2
try:
    number = int(input("Введите целое число: "))
    if number < 0:
        number = 1_000_000
        print(f"Число было отрицательным. Новое значение: {number}")
    elif number == 0:
        number = 2 ** 2 
        print(f"Число было равно нулю. Новое значение (2^2): {number}")
    else:
        number = number ** 3
        print(f"Число было положительным. Новое значение (в степени 3): {number}")
except ValueError:
    print("Ошибка ввода: введено не целое число.")
#Вариант10_Задание3
number_1 = 10
number_2 = 100
try:
    user_number = int(input("Введите целое число: "))
    if number_1 < user_number < number_2:
        print(True)
    else:
        print(False)
except ValueError:
    print(False)
#Вариант11_Задание1
prog_num = 0
try:
    num1 = int(input("Введите первое целое число: "))
    num2 = int(input("Введите второе целое число: "))
    if num1 < 0 and num2 < 0:
        prog_num = num1 + num2
        print(prog_num)
    elif num1 > 0 and num2 > 0:
        prog_num = num1 - num2
        print(prog_num)
    else:
        print(False)
except ValueError:
    print("Ошибка ввода: введено не целое число.")
#Вариант11_Задание2
try:
    number = int(input("Введите целое число: "))
    if number % 2 != 0:
        number += 1
        print(number)
    else:
        print(True)
except ValueError:
    print("Ошибка ввода: введено не целое число.")
#Вариант11_Задание3
input_string = input("Введите строку: ")
string_length = len(input_string)
if string_length > 10:
    print(input_string[:5])
else:
    print(input_string)
#Вариант12_Задание1
def check_language(letter):
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    en = 'abcdefghijklmnopqrstuvwxyz'
    letter_lower = letter.lower()
    if letter_lower in ru:
        return 'rus'
    elif letter_lower in en:
        return 'eng'
    else:
        return None
user_input = input("Введите одну букву: ")
if len(user_input) == 1:
    result = check_language(user_input)
    print(result)
else:
    print("Ошибка ввода: Введите ровно один символ.")
#Вариант12_Задание2
def check_number_proximity(user_num, pc_num):
    difference = abs(user_num - pc_num)
    if difference <= 1:
        return True
    else:
        return False
pc_num = 10
try:
    user_input = int(input(f"Введите целое число для сравнения с {pc_num}: "))

    result = check_number_proximity(user_input, pc_num)
    print(result)
except ValueError:
    print("Ошибка ввода: Введите корректное целое число.")
#Вариант12_Задание3
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("True")
    elif user_answer > correct_answer:
        print(">")
    else:
        print("<")
correct_result = (221 - 13) * 2
print('(221 - 13) * 2')
try:
    user_input_str = input("Введите ваш ответ: ")
    user_answer = float(user_input_str)
    check_answer(user_answer, correct_result)
except ValueError:
    print("Ошибка ввода: Введите корректное числовое значение.")
