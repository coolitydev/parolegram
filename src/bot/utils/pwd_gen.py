import secrets
import string


class PasswordGenerator:
    """
    Класс генератор паролей

    :param length: int: длина пароля
    :param use_letters: bool: использовать буквы
    :param use_digits: bool: использовать цифры
    :param use_punctuation: bool: использовать знаки пунктуации
    """

    def __init__(
            self,
            length: int,
            use_letters: bool = True,
            use_digits: bool = True,
            use_punctuation: bool = True
    ) -> None:
        """
        Иницициализация класса

        :param length: int: длина пароля
        :param use_letters: bool: использовать буквы
        :param use_digits: bool: использовать цифры
        :param use_punctuation: bool: использовать знаки пунктуации

        :return: None
        """
        self.length: str = length
        self.use_letters: bool = use_letters
        self.use_digits: bool = use_digits
        self.use_punctuation: bool = use_punctuation

    @staticmethod
    def _build_symbols(use_letters: bool, use_digits: bool, use_punctuation: bool) -> str:
        """
        Создаёт текст из символов на основе настроек

        :return: str: символы для генерации пароля
        """
        symbols: str = ""

        if use_letters:
            symbols += string.ascii_letters
        if use_digits:
            symbols += string.digits
        if use_punctuation:
            symbols += string.punctuation
        return symbols

    def generate(self) -> str:
        """
        Генерирует пароль на основе символов

        :raises ValueError: если алфавит пустой
        :return: str: сгенерированный пароль
        """
        symbols: str = self._build_symbols(
            use_letters=self.use_letters,
            use_digits=self.use_digits,
            use_punctuation=self.use_punctuation
        )

        if not symbols:
            raise ValueError("Alphabet is empty")

        return "".join(
            secrets.choice(symbols) for _ in range(self.length)
        )
