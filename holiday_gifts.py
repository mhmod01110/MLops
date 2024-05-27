"""
Module for calculating the total price of gifts after taxes.
"""

# your task is to clean this script in
# a way that uses the code as a single function
# that takes a path and returns the total_price variable
# that meets pep8 standards and receives a 10 score using pylint

# You may need to:
# pip install autopep8
# pip install pylint

import time
import numpy as np


def calc_total_price(cost_path):
    """
    Calculate the total cost of gifts after taxes.

    Args:
        cost_path (str): File path of gifts cost.

    Returns:
        total_price (float): Total cost of gifts.
    """
    with open(cost_path, encoding='utf-8') as file:
        gift_costs = file.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int

    start = time.time()

    total_price = 0
    for cost in gift_costs:
        if cost < 25:
            total_price += cost * 1.08  # add cost after tax

    print(total_price)
    print(f'Duration: {time.time() - start} seconds')

    start = time.time()

    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
    print(total_price)

    print(f'Duration: {time.time() - start} seconds')

    return total_price


if __name__ == '__main__':
    price_total = calc_total_price('gift_costs.txt')
    print(price_total)
