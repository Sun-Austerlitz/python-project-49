from brain_games.games.engine import run_game
from brain_games.games import calc


def main():
    """
    Точка входа в игру "Калькулятор"
    """
    run_game(calc)


if __name__ == '__main__':
    main()
