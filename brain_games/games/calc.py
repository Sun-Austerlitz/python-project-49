import random
import operator

# Описание игры
DESCRIPTION = 'What is the result of the expression?'

# Словарь операций
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_question_and_answer():
    """
    Генерация матем. выражения из двух случайных чисел и случайной операции.

    Returns:
        tuple: Вопрос в виде строки и правильный ответ в виде строки.
    """
    # Генерация случайных чисел
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # Выбор случайной операции
    operation = random.choice(list(OPERATIONS.keys()))
    # Формирование вопроса
    question = f"{num1} {operation} {num2}"
    # Вычисление правильного ответа
    correct_answer = str(OPERATIONS[operation](num1, num2))
    return question, correct_answer
