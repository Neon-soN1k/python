#Задание1
def upper(t: str):
    uppercase_chars = ""
    for char in t:
        if char.isupper():
            uppercase_chars += char + " "
    if uppercase_chars:
        print(uppercase_chars.strip())
upper('PriVet')
upper('HelloWorld')
upper('нижний регистр') 
upper('Только Заглавные') 
#Задание2
def punct(txt: str):
   target_punctuations = "! ? . , ( )"
    count = 0
    for char in txt:
        if char in target_punctuations:
            count += 1
    if count > 0:
        print(count)
punct('(Как дела?)')
punct("Привет, мир!")
punct("Без знаков препинания")
punct("Точка в конце.")
#Задание3
def create_cube(x: int, y: int):
    if x <= 0 or y <= 0:
        print("Длина и высота должны быть положительными числами.")
        return
    for _ in range(y):
        line = '*' * x
        print(line)
print("Пример 1:")
create_cube(5, 3)
print("\nПример 2 (квадрат 4х4):")
create_cube(4, 4)
print("\nПример 3 (тонкая линия):")
create_cube(10, 1)
#Задание4
def double(s: str):
    doubled_string = ""
    for char in s:
        doubled_string += char * 2
    print(doubled_string)
double('строка')
double('Python')
double('123! ')
#Задание5
def Constructor(details_supply: int, figures_supply: int, cars_supply: int, trees_supply: int) -> int:
    required_details = 72
    required_figures = 4
    required_cars = 2
    required_trees = 7
    sets_from_details = details_supply // required_details
    sets_from_figures = figures_supply // required_figures
    sets_from_cars = cars_supply // required_cars
    sets_from_trees = trees_supply // required_trees
    max_possible_sets = min(sets_from_details, sets_from_figures, sets_from_cars, sets_from_trees)
    return max_possible_sets
print(f">>> Constructor(144, 8, 4, 14)\n>>> {Constructor(144, 8, 4, 14)}")
print(f">>> Constructor(10000, 16, 6, 2)\n>>> {Constructor(10000, 16, 6, 2)}")
#Задание6
def create_list(length: int, number: int = 0) -> list[int]:
    generated_list = [number] * length
    return generated_list
result1 = create_list(5, 3)
print(f">>> create_list(5, 3)\n>>> {result1}")
print("-" * 20)
result2 = create_list(3)
print(f">>> create_list(3)\n>>> {result2}")
#Задание7
def custom_filter(input_list: list):
    sum_divisible_by_7 = 0    
    for item in input_list:
        if isinstance(item, int) and not isinstance(item, bool):
            if item % 7 == 0:
                sum_divisible_by_7 += item
    print(f">>> сумма: {sum_divisible_by_7}")
    if sum_divisible_by_7 > 83:
        return False
    else:
        return True
print(f">>> {custom_filter([7, 10.5, 'txt', 14, 2, 56])}")
#Задание8
def square(x: int, y: int):
    x_str = str(x)
    y_str = str(y)
    cell_width = max(len(x_str), len(y_str)) + 2
    format_str = f"{{:^{cell_width}}}"
    total_width = 3 + 2 * cell_width
    top_border = "_" * total_width
    print(top_border)
    row_content = f"|{format_str.format(x_str)}|{format_str.format(y_str)}|"
    print(row_content)
    bottom_border = "¯" * total_width
    print(bottom_border)
print("Пример: square(2, 3)")
square(2, 3)
print("\nПример с большими числами: square(100, 5)")
square(100, 5)
