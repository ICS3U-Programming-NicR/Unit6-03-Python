#!/usr/bin/env python3.10

# Created by: Nic Riscalas
# Created on: May 2022
# This program shows the user the smallest number between 10 random numbers

import random
import constants


def smallest_number_check(list_of_numbers):
    # this functions figures out the largest number

    min_num = list_of_numbers[0]

    for num_in_array in list_of_numbers:
        if num_in_array < min_num:
            min_num = num_in_array

    return min_num


def main():
    # this function uses a list

    random_numbers = []

    # input
    for i in range(0, constants.MAX_ARRAY_SIZE):
        single_random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        random_numbers.append(single_random_number)
        print("The random number {0} is {1} ".format(i + 1, single_random_number))

    # call functions
    smallest_number = smallest_number_check(random_numbers)
    # output
    print("The smallest_number number is: {} ".format(smallest_number))


if __name__ == "__main__":
    main()
