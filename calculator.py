# calculator.py — модуль с математическими операциями

class Calculator:
    """Простой калькулятор с базовыми операциями."""

    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел явно как float."""
        return float(a + b)

    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел. Вызывает ошибку при делении на ноль."""
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Возведение в степень."""
        return a ** b
