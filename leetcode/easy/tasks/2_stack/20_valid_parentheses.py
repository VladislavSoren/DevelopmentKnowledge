"aaa2(bc2(d))"

"a2(bc)"
""""
1. 
result_str - a
2. 
result_str - a
number_str - 2

"""

numbers = set([str(i) for i in range(1, 10)])
brackets = set(["(",")"])

def unwrape(s):

    stack = [] # []
    number_str = ''
    str_in_brackets = ''
    result_str = ''

    for i, el in enumerate(s):

        # Переход с числа на букву (мгновенная развёртка)
        if el not in numbers | brackets and s[i-1] in numbers:
            result_str += int(number_str) * el
            number_str = ''
        elif el not in numbers | brackets and not stack:
            result_str += el
        elif el in numbers:
            number_str += el 
        # Переход с числа на ПЕРВУЮ скобку, начальная инициализация, стек пуст
        elif el == "(" and s[i-1] in numbers and not stack:
            stack.append((result_str, number_str))
            number_str = ''
        # собираем строку внутри скобки
        elif stack and el not in numbers | brackets:
            str_in_brackets += el
        # наполняем стек внутри скобок (увеличение вложенности)
        elif stack and el == "(":
            stack.append((str_in_brackets, number_str))
            number_str = ''
            str_in_brackets = ''
        # наткнулись на ")" - начинаем развёртку
        elif el == ")":
            stack_upper = stack.pop()
            str_in_brackets = stack_upper[0] + str_in_brackets * int(stack_upper[1])
            result_str = str_in_brackets
        # Алгоритм развёртки стека (тогда станет понятна его структура)

        # # Переход со скобки на букву
        # elif:
        # else:
        #     result_str += el

    return result_str                           

s = "2a"
print(unwrape(s))     