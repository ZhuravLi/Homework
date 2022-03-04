"""Game "Guess the number"
Computer randomly guesses the number and uses less than 20 attempts.
"""

import numpy as np


def predict(number: int = 1) -> int:
    """We guess the number from 1 to 100.

    Args:
        number (int): Guessed number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
            
    left_boundary = 1 # Left boundary of segment
    right_boundary = 100 # Right boundary of segment
    count = 0 # Number of attempts
        
    while True:
        """ For each iteration we split the segment in two parts.
        Then we take the segment which contains guessed number.
        """
        count += 1
        
        if left_boundary == right_boundary:
            break
        
        mean = (left_boundary+right_boundary) // 2
        if mean == number:
            break
        elif mean < number:
            left_boundary = mean + 1
        else:
            right_boundary = mean - 1
            
    return count


def score_game(predict) -> int:
    """How many attempts our algorithm needs to guess the number, on average (1000 approaches)

    Args:
        predict ([type]): function of guessing

    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1)  # Fix the seed of reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # Fix random list of numbers

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average for {score} attempts")
    return score

if __name__ == "__main__":
    # RUN
    score_game(predict)