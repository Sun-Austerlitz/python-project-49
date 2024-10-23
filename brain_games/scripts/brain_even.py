import random
from prompt import string


# проверка на четность числа
def is_even(number):
    return number % 2 == 0


def main():
    """
    Описание игры и логика игры "Проверка на четность".
    Игроку показывается случайное число.
    Ему нужно ответить 'yes', если число четное, или 'no' - если нечетное.
    Игра заканчивается после трех правильных ответов или при не верном ответе.
    """
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        # генерация случайного числа
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = string("Your answer: ")

        correct_answer = "yes" if is_even(number) else "no"
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
