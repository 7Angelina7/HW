class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Сложение клеток. Размер клетки: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Вычитание клеток. Размер клетки: {sub}' if sub > 0 else 'Исчезновение клетки'

    def __truediv__(self, other):
        return f'Умножение клеток. Размер клетки: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Деление клеток. Размер клетки: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(50)
cell_2 = Cell(5)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))