from brain_games.games.engine import run_game
from brain_games.games import gcd


def main():
    """
    Точка входа для игры "НОД".
    """
    run_game(gcd)


if __name__ == '__main__':
    main()