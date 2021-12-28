"""
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`.
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7.

*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо
перепишите существующую sum_list_2)
"""


def sum_list_1(dataset: list) -> int:
    # создание списка кубов нечетных чисел
    for el in range(1, 1000):
        if el % 2 == 1:
            dataset.append(el ** 3)
    # вычисление суммы чисел
    sum_out = 0
    for el in range(len(dataset)):
        temp_sum = 0
        temp_el = dataset[el]
        while temp_el > 0:
            temp_sum += temp_el % 10
            temp_el = temp_el // 10
        if temp_sum % 7 == 0:
            sum_out += dataset[el]
    return sum_out


def sum_list_2(dataset: list) -> int:
    # вычисление суммы чисел
    sum_out = 0
    for el in range(len(dataset)):
        dataset[el] += 17
        temp_sum = 0
        temp_el = dataset[el]
        while temp_el > 0:
            temp_sum += temp_el % 10
            temp_el = temp_el // 10
        if temp_sum % 7 == 0:
            sum_out += dataset[el]
    return sum_out


my_list = []  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
