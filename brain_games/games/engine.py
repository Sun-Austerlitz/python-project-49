from prompt import string

# Количество раундов
MAX_ROUNDS = 3


def run_game(game):
    """
    Запускает игру, принимает на вход объект игры, возвращает результат игры
    """
    # Приветствие
    print("Welcome to the Brain Games!")
    # Запрос имени
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    # Описание игры
    print(game.DESCRIPTION)

    # Количество правильных ответов
    correct_answers = 0
    # пока правильных ответов меньше, чем MAX_ROUNDS
    while correct_answers < MAX_ROUNDS:
        # Генерация вопроса и правильного ответа
        question, correct_answer = game.generate_question_and_answer()
        # Вывод вопроса
        print(f"Question: {question}")
        # Ответ пользователя
        answer = string("Your answer: ")

        # если ответ верный - увеличиваем счетчик правильных ответов
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        # иначе - завершаем игру
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    # Поздравление с победой
    print(f"Congratulations, {name}!")
