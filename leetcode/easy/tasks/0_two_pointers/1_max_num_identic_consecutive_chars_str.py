"""
Задача:
Найти максимальное число одинаковых подряд идущих символов в строке
"""

"""
Проработка задачи:

1. Формулировка задачи
- Перескажите условие своими словами и спросите, правильно ли вы всё поняли
Необходимо найти длину подстроки с самым большим кол-вом идущих подряд одинаковых символов.

- Какие структуры будут поступать на вход функции, которую вам нужно реализовать?
По условию чётко прописано, что на вход будет подаваться строка

- Выясните ограничения. Есть ли условия для входных данных?
На вход подаётся строка, где может быть любое кол-во символов.

- Выясните ожидаемое поведение на краевых случаях.
Если строка пустая, то возвращаем 0 ?
Если в строке 1 символ, то вернуть 1

2. Придумывание решения
- Придумайте тестовый пример. Это должен быть хороший общий тест
Вход:
    arr - `qwweerrrtt11`
Вывод: 3

- Пользуясь этим примером, подумайте, как достичь нужного результата (стратегия)
Здесь подойдёт техника sliding window (частный случай техники two pointers).
Объявим два указателя left и right в интервале между которыми будет подсчитываться наиболее длинная последовательность.
Инициализация:
- left - имеет индекс 0
- right - имеет индекс 1
- max_len - максимальная длина подстроки
- curr_len - текущая максимальная последовательность
- curr_char - текущий символ в подстроке
- prev_char - предыдущий символ в подстроке

Условия изменения:
- right +=1, когда текущий символ равен предыдущему (условие непрерывности выполняется)
- left = right, right += 1, когда текущий символ НЕ равен предыдущему (условие непрерывности НЕ выполняется)

Инаварианты: 
- индекс right < len(arr) (right всегда меньше индекса конца массива)

- Придумайте какое-нибудь корректное решение. Оцените время работы и затраты по памяти и, если думаете, что можно решить задачу быстрее, скажите об этом.


- Первоначальное решение может оказаться оптимальным, но сложным в реализации. Подумайте, как именно вы будете его писать, чтобы избежать ошибок.
- Возможна и другая ситуация, когда существует более асимптотически эффективное решение. В этом случае могут помочь такие приёмы:
— Если у вас есть монотонность - может быть применим бинарный поиск или метод двух указателей
— Если вы много раз пересчитываете одно и то же — поможет динамическое программирование
- Часто для ускорения полезно использовать вспомогательную структуру данных, как правило, хеш-таблицу, кучу и т.п.
- Если ничего применить не получилось, вероятно, оптимальное решение основано на совсем другой идее. Сообщите интервьюеру, что собираетесь пойти в другом направлении и обязательно рассуждайте вслух

- Написать несколько корнер тестов и проверить
- Дописать функционал на их проверку
- Проверить
"""


def get_max_len_identic_consecutive_chars_str(input_str):
    # Инициализация
    """  
    Возвращает максимальное число одинаковых подряд идущих символов в строке.

    Инициализация:
    - left - имеет индекс 0
    - right - имеет индекс 0
    - max_len - максимальная длина подстроки
    - curr_len - текущая максимальная последовательность
    - curr_char - текущий символ в подстроке
    - prev_char - предыдущий символ в подстроке

    Возврат:
    max_len

    Условия изменения:
    - right +=1, когда текущий символ равен предыдущему (условие непрерывности выполняется)
    - left = right, когда текущий символ НЕ равен предыдущему (условие непрерывности НЕ выполняется)
    """

    if not input_str:
        return 0

    left = 0
    right = 0
    max_len = 0
    curr_len = 0
    prev_char = input_str[0]

    while right < len(input_str):

        curr_char = input_str[right]
        
        if curr_char == prev_char:
            prev_char = curr_char
            curr_len += 1
            max_len = max(max_len, curr_len)
            right += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
            left = right
            right += 1
            prev_char = input_str[left]
            
    return max_len


input_str = "q"
assert get_max_len_identic_consecutive_chars_str(input_str) == 1

input_str = "qq"
assert get_max_len_identic_consecutive_chars_str(input_str) == 2

input_str = "qqrrqqeee"
assert get_max_len_identic_consecutive_chars_str(input_str) == 3

input_str = "qwweerrrtt11"
assert get_max_len_identic_consecutive_chars_str(input_str) == 3

input_str = "qqrrqqe"
assert get_max_len_identic_consecutive_chars_str(input_str) == 2

input_str = ""
assert get_max_len_identic_consecutive_chars_str(input_str) == 0

input_str = "qqr"
assert get_max_len_identic_consecutive_chars_str(input_str) == 2

input_str = "qr"
assert get_max_len_identic_consecutive_chars_str(input_str) == 1


# Альтернативное решение
def max_consecutive_chars(s: str) -> int:
    if not s:
        return 0
    max_len = 1
    curr_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len


def max_consecutive_chars(s: str) -> int:
    max_len = 1
    curr_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_len += 1
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)
    return max_len

input_str = "q"
assert max_consecutive_chars(input_str) == 1

input_str = "qq"
assert max_consecutive_chars(input_str) == 2

input_str = "qqrrqqeee"
assert max_consecutive_chars(input_str) == 3

input_str = "qwweerrrtt11"
assert max_consecutive_chars(input_str) == 3