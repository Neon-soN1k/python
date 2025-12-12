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
