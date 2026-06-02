# logger.py — модуль для логирования

import datetime

class Logger:
    """Простой логгер, записывающий сообщения в файл."""

    def __init__(self, filename: str):
        self.filename = filename

    def write(self, message: str) -> None:
        """Записывает сообщение с временной меткой."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        print(entry)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

    def clear(self) -> None:
        """Очищает файл лога."""
        open(self.filename, "w").close()
