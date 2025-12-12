notebook = {}
def create_note():
    global notebook
    print("\n--- Создание новой заметки ---")
    header = input("Введите заголовок (Header): ")
    text = input("Введите текст заметки (Text): ")
     if header and text:
        notebook[header] = text
        print(f"-> Заметка '{header}' успешно добавлена.")
    else:
        print("!!! Заголовок или текст не могут быть пустыми.")
def read_notes():
    print("\n--- Чтение заметок ---")
    if not notebook:
        print("Заметок нет.")
        return
    print("Список заметок:", ", ".join(notebook.keys()))
    header_to_read = input("Какую заметку прочитать? (Which note to read?): ")
    if header_to_read in notebook:
        print(f"-- Текст заметки '{header_to_read}': --")
        print(notebook[header_to_read])
    else:
        print(f"Такой заметки нет ('{header_to_read}').")
def delete_note():
    global notebook   
    print("\n--- Удаление заметки ---")
    if not notebook:
        print("Заметок нет для удаления.")
        return   
    print("Список заметок:", ", ".join(notebook.keys()))    
    header_to_delete = input("Какую заметку удалить? (Which note to delete?): ")
    if header_to_delete in notebook:
        notebook.pop(header_to_delete)
        print(f"-> Заметка '{header_to_delete}' успешно удалена (Note {header_to_delete} removed).")
    else:
        print(f"Такой заметки нет ('{header_to_delete}').")
def menu():
    while True:
        print("\n[1] - Create a new note.")
        print("[2] - Read all notes.")
        print("[3] - Delete entry.")
        print("[4] - Exit.")
        choice = input("> ")
        if choice == '1':
            create_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Завершение программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 4.")
if __name__ == "__main__":
    menu()
