#Задание1
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}
print("1. Исходный словарь:")
print(my_dict)
print("-" * 20)
removed_value = my_dict.pop(3, "Ключ не найден")
print(f"2. Удален элемент с ключом 3 (значение '{removed_value}').")
print("   Словарь после удаления:")
print(my_dict)
print("-" * 20)
my_dict[10] = '0100101'
print("3. После добавления нового элемента (ключ 10):")
print(my_dict)
print("-" * 20)
#Задание2
sl = {'</>': 13, 'script': 1, '__init__': 10, 'self': 5,
      'number_9': 6, '#comment': 100}
print("1. Исходный словарь:")
print(sl)
print("-" * 30)
new_key = input("Введите новый ключ (key): ")
new_value_input = input(f"Введите значение для ключа '{new_key}': ")
try:
    new_value = int(new_value_input)
except ValueError:
    new_value = new_value_input
sl[new_key] = new_value
print("-" * 30)
print("3. Словарь после добавления нового элемента:")
print(sl)
#Задание3
user_dict = {}
print("Программа будет принимать ввод до тех пор, пока в словаре не будет 3 элемента.")
print("Ключ должен быть числом.")
while len(user_dict) < 3:
    print(f"\nТекущее количество элементов в словаре: {len(user_dict)}. Требуется еще {3 - len(user_dict)}.")
    key_input = input("Введите ключ (числовой тип): ")
        try:
        key = int(key_input)
        value = input(f"Введите значение для ключа '{key}': ")
        user_dict[key] = value
        print(f"-> Элемент успешно добавлен/обновлен.")
    except ValueError:
        print("!!! Ошибка: Ключ обязательно должен иметь числовой тип данных. Попробуйте снова.")
        continue
print("\n--------------------------------------------------")
print("Словарь заполнен (достигнуто 3 элемента).")
print("Итоговый словарь:")
print(user_dict)
#Задание4
all_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 44, 3: 9}
print("Исходный словарь:")
print(all_d)
keys_to_remove = [1, 101, 3]
for key in keys_to_remove:
    if key in all_d:
        del all_d[key]
        print(f"Удален ключ: {key}")
    else:
        print(f"Ключ {key} не найден в словаре.")
print("\nСловарь после удаления элементов:")
print(all_d)
