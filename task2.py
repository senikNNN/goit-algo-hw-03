import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
        Return quantity ща random number in range[min:max]
    """
    if quantity > max or quantity < min:
        return []
    else:
        numbers = list()
        while len(numbers) != quantity:
            number = random.randint(min, max)
            if number in numbers:
                continue
            numbers.append(number)
        numbers.sort()
        return numbers
    

print("Result of task2:", get_numbers_ticket(1, 40, 15))