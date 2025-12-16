#Задание1
def alpha(user_string):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    print(' '.join(alphabet))
    filtered_chars = [char for char in user_string.lower() if char in alphabet]
    used_chars = []
    for char in filtered_chars:
        if char not in used_chars:
            used_chars.append(char)
    remaining_chars = [char for char in alphabet if char not in used_chars]
    result = used_chars + remaining_chars
    print(' '.join(result))
alpha('пайтон')
#Задание2
def create_calendar(month_name, year, total_days):
    print(f"calendar: {month_name} {year}")
    day = 1           
    current_week = [] 
    while day <= total_days:
        current_week.append(str(day))
        if len(current_week) == 7 or day == total_days:
            print(' '.join(current_week))
            current_week = []       
        day += 1
create_calendar('Randomner', 2045, 23)
#Задание3
def bin_sys(start, end):
    if start > end:
        start, end = end, start
    numbers = []
    for num in range(start, end + 1):
        print(bin(num)[2:]) 
        numbers.append(num)
    total_sum = sum(numbers)
    print(f"сумма: {bin(total_sum)[2:]}")
bin_sys(3, 6)
#Задание4
def begin(field, row, col):
    if 0 <= row < len(field) and 0 <= col < len(field[row]):
        field[row][col] = '*[*]'
    else:
        print("Ошибка: индексы выходят за границы массива")
        return
    for row_items in field:
        print(' '.join(row_items))
field = [['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]']]
begin(field, 1, 2)
#Задание5
def _numbers(n1, step=1):
    print(f"[{n1}] [{n1 + 1 * step}]\n[{n1 + 2 * step}] [{n1 + 3 * step}]")
#Задание6
def count_letter(text, letter):
    text_lower = text.lower()
    letter_lower = letter.lower()
    count = text_lower.count(letter_lower)
    return count
text_input = 'My name is Sara.'
letter_input = 's'
result = count_letter(text_input, letter_input)
print(result)
text_russian = 'Привет, мир! Как дела?'
letter_russian = 'и'
result_russian = count_letter(text_russian, letter_russian)
print(result_russian)
