"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
* до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

Примеры:

> duration = 53
53 сек

> duration = 153
2 мин 33 сек

> duration = 4153
1 час 9 мин 13 сек

> duration = 400153
4 дн 15 час 9 мин 13 сек
Примечание: можете проверить себя здесь,
подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности,
будет ли тут полезен список?

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    return "верните итоговую строку с результатом"


duration = 400153
result = convert_time(duration)
print(result)
"""


def convert_time(duration: int) -> str:
    if duration < 60:
        result_out = f"{duration} сек"
    elif duration < 3600:
        minutes_out = duration // 60
        seconds_out = duration % 60

        result_out = f"{minutes_out} мин {seconds_out} сек"
    elif duration < 86400:
        hours_out = duration // 3600
        minutes_out = (duration % 3600) // 60
        seconds_out = (duration % 3600) % 60

        result_out = f"{hours_out} час {minutes_out} мин {seconds_out} сек"
    else:
        days_out = duration // 86400
        hours_out = (duration % 86400) // 3600
        minutes_out = ((duration % 86400) % 3600) // 60
        seconds_out = ((duration % 86400) % 3600) % 60

        result_out = f"{days_out} дн {hours_out} час {minutes_out} мин {seconds_out} сек"
    return result_out


duration = 400153
result = convert_time(duration)
print(result)
