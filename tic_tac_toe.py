def print_board(board):
    """Выводит игровое поле в удобном консольном виде."""
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} " + " | ".join(row))
        if i < 2:
            print("  --------")
    print()

def check_winner(board):
    """Проверяет линии на наличие победителя."""
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
            
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
        
    return None

def is_board_full(board):
    """Проверяет, остались ли свободные клетки."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    print("=== КРЕСТИКИ-НОЛИКИ ===")
    print("Игроки ходят по очереди. Нужно вводить номер строки и столбца (от 0 до 2).")
    
    # Создаем пустое поле 3x3
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Ходит игрок '{current_player}'")
        
        try:
            row = int(input("Введите номер строки (0-2): "))
            col = int(input("Введите номер столбца (0-2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("⚠️ Ошибка: Номер должен быть от 0 до 2!")
                continue
                
            if board[row][col] != " ":
                print("⚠️ Эта клетка уже занята! Выберите другую.")
                continue
                
        except ValueError:
            print("⚠️ Ошибка: Нужно ввести целое число от 0 до 2.")
            continue
            
        # Делаем ход
        board[row][col] = current_player
        
        # Проверяем на победу
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Поздравляем! Игрок '{winner}' победил!")
            break
            
        # Проверяем на ничью
        if is_board_full(board):
            print_board(board)
            print("🤝 Ничья! Свободных клеток больше нет.")
            break
            
        # Меняем игрока
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
