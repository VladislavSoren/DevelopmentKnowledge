"""
Задача с собеса 2025.11.05

На вход подаётся:
- Неубывающая последовательность "a", c колличеством элементов N
- Индекс index, который определяет опорное значение, огтносительно которого будет искаться ближ. значения
! ближ. значения - разность между опортным элементом и другими наименьшая
- число k, которое определяет кол-во ближайших значений для возврата

Нужно:
- Найти k ближайших соседей для элемента c позицией index.

Ограничения:
- index и k - integer
- k <= N

Примеры:
[3,5,7,8], i=1, k=2 -> [3,5] или [5,7]
[3,5,7,8,8], i=2, k=3 -> [7,8,8]
[3,5,7,8,8], i=2, k=4 -> [5,7,8,8]

Временная и пространственная сложность равна k
"""

def get_nearest_numbers(a, index, k):
    
    left = index - 1
    right = index + 1
    nearest_numbers = []

    # Крайний случай при k == 0
    if k == 0:
        return []
    
    if len(a) > 0 and k != 0:
        nearest_numbers.append(a[index]) 

    while len(nearest_numbers) != k:

        # инварианты
        # Если правый указатель вышел за пределы массива, то добавляем элемент слева и двигаем левый указатель
        if right > len(a) - 1:
            nearest_numbers.append(a[left])
            left -= 1
        elif left < 0:
            nearest_numbers.append(a[right])
            right += 1
        # общий случай: Если дистанция справа меньше чем слева, то здесь нужный элемент 
        elif a[right] - a[index] < a[index] - a[left]:
            nearest_numbers.append(a[right])
            right += 1
        else:
            nearest_numbers.append(a[left])
            left -= 1

    return nearest_numbers
