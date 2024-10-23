import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    """
    Генерация двух случайных чисел и вычисление их наибольшего общего
    делителя (НОД).

    Returns:
        tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
