#! /usr/bin/env python

import random
import math

def make_one():
    return (
        f"-----------\n"
        f"|         |\n"
        f"|    *    |\n"
        f"|         |\n"
        f"-----------\n"
    )

def make_two():
    return (
        f"-----------\n"
        f"|  *      |\n"
        f"|         |\n"
        f"|      *  |\n"
        f"-----------\n"
    )

def make_three():
    return (
        f"-----------\n"
        f"|  *      |\n"
        f"|    *    |\n"
        f"|      *  |\n"
        f"-----------\n"
    )

def make_four():
    return (
        f"-----------\n"
        f"|  *   *  |\n"
        f"|         |\n"
        f"|  *   *  |\n"
        f"-----------\n"
    )

def make_five():
    return (
        f"-----------\n"
        f"|  *   *  |\n"
        f"|    *    |\n"
        f"|  *   *  |\n"
        f"-----------\n"
    )

def make_six():
    return (
        f"-----------\n"
        f"|  *   *  |\n"
        f"|  *   *  |\n"
        f"|  *   *  |\n"
        f"-----------\n"
    )

def make_die(num):
    if num < 1 or num > 6:
        raise ValueError("Argument must be an integer between 1 and 6")
    
    if num == 1:
        return make_one()
    elif num == 2:
        return make_two()
    elif num == 3:
        return make_three()
    elif num == 4:
        return make_four()
    elif num == 5:
        return make_five()
    elif num == 6:
        return make_six()
    else:
        raise Exception("This code should never execute...")

if __name__ == '__main__':
    print(make_die(random.randint(1, 6)))