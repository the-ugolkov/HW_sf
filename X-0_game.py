field = list(range(1, 10))


def game_field(field):
    for i in range(3):
        print(field[0+i*3], "|", field[1+i*3], "|", field[2+i*3])


def game_cell(player_icon):
    input_icon = False
    while not input_icon:
        request = input("Куда ставим " + player_icon + "?")
        try:
            request = int(request)
        except ValueError:
            print("Ошибка, введите число от 1 до 9!")
            continue
        if 1 <= request <= 9:
            if str(field[request-1]) not in "XO":
                field[request-1] = player_icon
                input_icon = True
            else:
                print("Эта клетка занята!")
        else:
            print("Введите число от 1 до 9!")


def check(field):
    win_version = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for i in win_version:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False


def main(field):
    enum = 0
    win = False
    game_field(field)
    while not win:
        if enum % 2 == 0:
            game_cell("X")
        else:
            game_cell("O")
        enum += 1
        if 4 < enum <= 9:
            check_win = check(field)
            if check_win:
                print(str(check_win) + " победил!")
                win = True
            elif enum == 9:
                print("Ничья)")
                break
        game_field(field)


main(field)
