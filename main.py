# main.py — точка входа приложения

from calculator import Calculator
from logger import Logger

def main():
    log = Logger("app.log")
    calc = Calculator()

    log.write("Приложение запущено")

    a, b = 10, 5
    print(f"Сложение:      {a} + {b} = {calc.add(a, b)}")
    print(f"Вычитание:     {a} - {b} = {calc.subtract(a, b)}")
    print(f"Умножение:     {a} * {b} = {calc.multiply(a, b)}")
    print(f"Деление:       {a} / {b} = {calc.divide(a, b)}")

    log.write("Вычисления выполнены успешно")
    log.write("Приложение завершено")

if __name__ == "__main__":
    main()
# изменение 1
# изменение 2
# изменение 3
