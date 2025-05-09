from colorama import Fore, Back, Style, init
init(autoreset=True)  # Автоматический сброс стилей после каждого вывода

def print_board(board):
    """Выводит цветное игровое поле с рамкой"""
    print(Style.BRIGHT + "╔═══╦═══╦═══╗")
    for i in range(3):
        print("║", end="")
        for j in range(3):
            cell = board[i*3 + j]
            if cell == 'X':
                color = Fore.RED
            elif cell == 'O':
                color = Fore.BLUE
            else:
                color = Fore.LIGHTBLACK_EX
            print(f" {color}{cell}{Style.RESET_ALL} ║", end="")
        print()
        if i < 2:
            print(Style.BRIGHT + "╠═══╬═══╬═══╣")
    print(Style.BRIGHT + "╚═══╩═══╩═══╝")

def check_win(board, player):
    """Проверяет, выиграл ли игрок"""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные
        [0, 4, 8], [2, 4, 6]              # Диагональные
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def get_player_color(player):
    """Возвращает цветовое оформление для игрока"""
    return Fore.RED + Style.BRIGHT if player == 'X' else Fore.BLUE + Style.BRIGHT

def tic_tac_toe():
    """Основная функция игры"""
    board = [str(i+1) for i in range(9)]
    current_player = 'X'
    game_on = True
    
    print(Fore.CYAN + Style.BRIGHT + "\n Добро пожаловать в Крестики-нолики! ")
    print(Fore.LIGHTBLACK_EX + "Номера клеток:")
    print_board(board)
    print(Fore.GREEN + "Игрок X: " + Fore.RED + "❌" + 
          Fore.GREEN + "  Игрок O: " + Fore.BLUE + "⭕" + "\n")
    
    # Сброс доски для игры
    board = [' ' for _ in range(9)]

    while game_on:
        print_board(board)
        player_color = get_player_color(current_player)
        print(player_color + f"\n Ход игрока {current_player} " + Style.RESET_ALL)
        
        # Получаем корректный ход
        while True:
            try:
                move = int(input(" Выберите клетку (1-9): ")) - 1
                if 0 <= move <= 8:
                    if board[move] == ' ':
                        break
                    else:
                        print(Fore.YELLOW + " Эта клетка уже занята!")
                else:
                    print(Fore.YELLOW + " Введите число от 1 до 9!")
            except ValueError:
                print(Fore.YELLOW + " Некорректный ввод. Попробуйте снова!")

        # Обновляем доску
        board[move] = current_player

        # Проверка результатов
        if check_win(board, current_player):
            print_board(board)
            print(Fore.GREEN + Style.BRIGHT + f"\n Игрок {current_player} победил! 🏆" + Style.RESET_ALL)
            game_on = False
        elif ' ' not in board:
            print_board(board)
            print(Fore.YELLOW + Style.BRIGHT + "\n Ничья! 🤝" + Style.RESET_ALL)
            game_on = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()