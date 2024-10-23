import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Проверка, является ли число простым.

    Args:
        number (int): Число для проверки.

    Returns:
        bool: True, если число простое, иначе False.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    """
    Генерация случайного числа и правильного ответа на вопрос,
    является ли число простым.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
