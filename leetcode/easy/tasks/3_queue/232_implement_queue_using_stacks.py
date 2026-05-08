class MyQueue:
    def __init__(self):
        self.stack_in = []   # для push
        self.stack_out = []  # для pop/peek

    def push(self, x: int) -> None:
        # Просто добавляем в стек ввода
        self.stack_in.append(x)

    def _transfer(self) -> None:
        # Перекладываем все элементы из stack_in в stack_out,
        # если stack_out пуст. Это происходит только при pop/peek.
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def pop(self) -> int:
        # Готовим стек вывода (перекладываем, если нужно)
        self._transfer()
        # Теперь верхний элемент stack_out — это первый в очереди
        return self.stack_out.pop()

    def peek(self) -> int:
        self._transfer()
        # Смотрим верхний элемент без удаления
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Очередь пуста, если оба стека пусты
        return not self.stack_in and not self.stack_out
    

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # 1
print(q.pop())   # 1
print(q.empty()) # False
q.push(3)
print(q.pop())   # 2
print(q.pop())   # 3
print(q.empty()) # True