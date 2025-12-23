import random
def maze_game():
    print("Начинаем игру. Повороты: [a]-Налево, [w]-Прямо, [d]-Направо")
    left_turns = 0
    straight_moves = 0
    right_turns = 0
    while True:
        print("Куда идти? ", end="")
        choice = input().lower().strip() 
        if choice == 'a':
            left_turns += 1
            print("Повернул налево. Выхода пока нет...")
        elif choice == 'w':
            straight_moves += 1
            print("Пошёл прямо. Выхода пока нет...")
        elif choice == 'd':
            right_turns +=1
            print("Повернул направо. Выхода пока нет...")
        else:
            print("Неверный ввод. Пожалуйста, используйте 'a', 'w' или 'd'.")
            continue 
        if random.randint(1, 10) == 1:
            print("Выход найден. Ты выиграл!")
            print(f"Для того, чтобы найти выход ты {left_turns} раз повернул налево, "
                  f"{straight_moves} раз пошёл прямо и {right_turns} раз повернул направо.")
            break        
    print("\nИгра завершена.")
maze_game()
