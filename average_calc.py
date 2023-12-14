#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Dec 6, 2023
# This program will find the avg of
# 10 numbers

import random
import constants


def main():
    # create list and sum
    list_of_int = []
    sum_of_numbers = 0

    # Generate random numbers and fill the list
    for counter1 in range(constants.MAX_ARRAY_SIZE):
        random_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        list_of_int.append(random_num)

    # Calculate the sum
    for counter2 in range(constants.MAX_ARRAY_SIZE):
        sum_of_numbers += list_of_int[counter2]

    # Calculate and display the average
    average = sum_of_numbers / constants.MAX_ARRAY_SIZE
    print(f"The average of all the numbers is {average:.2f}")


if __name__ == "__main__":
    main()
