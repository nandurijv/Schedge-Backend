import random

def biased_coin_flip(bias):
    if not 0 <= bias <= 1:
        raise ValueError("Bias must be a float between 0 and 1.")
    result = random.random() < bias
    return "heads" if result else "tails"

