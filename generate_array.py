import random as r


def generate_array(size):
    numbers = [x + 1 for x in range(size)]
    r.shuffle(numbers)
    return numbers
