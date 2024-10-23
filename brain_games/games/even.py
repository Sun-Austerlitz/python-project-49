import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """
    Проверка на четность числа.

    Args:
        number (int): Число для проверки.

    Returns:
        bool: True, если число четное, иначе False.
    """
    return number % 2 == 0


def generate_question_and_answer():
    """
    Генерирует случайное число и правильный ответ.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
