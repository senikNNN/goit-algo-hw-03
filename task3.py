import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(numbers: list) -> list:
    """
        Очищує список номерів, прибираючи літери та символи, повертаючи список номерів у вигляді +380*********
    """
    normalize_numbers = list()
    char_pattern = r'[a-z-()\\\s\+]'
    sufix_pattern = r'^\d*?(?=0)0'
    for number in numbers:
        removed_characters = re.sub(char_pattern, "", number)
        removed_sufix = re.sub(sufix_pattern, "", removed_characters)
        normalize_numbers.append("+380" + removed_sufix)
    return normalize_numbers

print("Нормалізовані номери телефонів для SMS-розсилки:\n", normalize_phone(raw_numbers))


