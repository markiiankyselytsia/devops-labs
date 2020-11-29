import logging


def print_nums(is_even):
    print(list(range(2, 101, 2) if is_even else range(1, 101, 2)))

def inverse(num):
    try:
        print(1 / num)
    except ZeroDivisionError:
        logging.getLogger().info('Число не може бути 0') 

