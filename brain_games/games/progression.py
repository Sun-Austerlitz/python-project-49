import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    """
    Генерация арифметической прогрессии.

    Args:
        start (int): Начальное число прогрессии.
        step (int): Шаг прогрессии.
        length (int): Длина прогрессии.

    Returns:
        list: Список чисел, образующих арифметическую прогрессию.
    """
    return [start + step * i for i in range(length)]


def generate_question_and_answer():
    """
    Генерация арифметической прогрессии с пропущенным числом и правильного
    ответа.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = generate_progression(start, step, length)
    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
