import random
import re
from fractions import Fraction

rnum1 = random.randint(1, 10)


def enter_num():
    pattern = r"\d"
    global nguess
    guess = input("guess the random number between 1 and 9")
    if re.match(pattern, guess) and len(guess) <= 1:
        nguess = int(guess)
        return nguess
    else:
        print("only numbers allowed")
        enter_num()


enter_num()


if nguess > rnum1:
    print("number is too big")
    print(nguess, rnum1)
elif nguess < rnum1:
    print("number is too small")
    print(nguess, rnum1)
elif nguess == rnum1:
    print("congratulations you are right")
    print(nguess, rnum1)
