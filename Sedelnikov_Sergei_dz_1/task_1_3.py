"""
Реализовать склонение слова процент во фразе N процентов.
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""


def transform_string(number: int) -> str:
    trans_proc = ''
    if number % 10 == 1:
        if (number // 10) % 10 != 1:
            trans_proc = f"{number} процент"
        else:
            trans_proc = f"{number} процентов"
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        if (number // 10) % 10 == 1:
            trans_proc = f"{number} процентов"
        else:
            trans_proc = f"{number} процента"
    else:
        trans_proc = f"{number} процентов"
    return trans_proc


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))