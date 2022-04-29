from string import ascii_lowercase
from random import choice, randint
from typing import Callable

allowed_repeat = "milo"
vowels = "aeiouy"
unspoken = "bcdfghjklmnpqrstvwxz"


def random4_12() -> int:
    return randint(4, 12)


def username(
    lenght: int = random4_12,
    symbols: iter = ascii_lowercase,
    repeat: str = allowed_repeat,
) -> str:
    """
    Generate a random username.

    :param lenght: The lenght of the username. (Default is random between 4 and 12)
    :param symbols: The symbols to use. (Default is ascii_lowercase). Please use only lowercase letters.
    :param repeat: The symbols allowed to repeat. (Default is allowed_repeat).
    :return: A random username.
    """
    if isinstance(lenght, Callable):
        # noinspection PyCallingNonCallable
        lenght = lenght()

    result = ""
    last = "_"
    for _ in range(lenght):
        value = choice(symbols)
        while (
            (last in vowels and value in vowels)
            or (last in unspoken and value in unspoken)
            or (value == last and value not in repeat)
        ):
            value = choice(symbols)
        result += value
        last = value

    return result.capitalize()
