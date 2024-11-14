import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split


def print_flag():
    try:
        with open('/flag', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('Error: Flag file not found.')

_correct_count = {
    'step 1': False
}


class _Solution:
    n_estimators = 140


def _color_text(text, color):
    color_code = ''
    if color == 'red':
        color_code = '\033[31m'
    elif color == 'green':
        color_code = '\033[32m'
    reset_code = '\033[0m'
    return f'{color_code}{text}{reset_code}'


def step_1_check(n_estimators):
    global _correct_count
    try:
        assert n_estimators == _Solution.n_estimators, "Incorrect value for `n_estimators`"
    except AssertionError as e:
        if n_estimators < _Solution.n_estimators:
            direction = 'Higher'
        else:
            direction = 'Lower'

        print(_color_text('Incorrect:', 'red'), e, f'(HINT: {direction})')
        _correct_count['step 1'] = False
    else:
        print(_color_text('Correct', 'green'))
        _correct_count['step 1'] = True

        # Add in check to see if all values in _correct_count are set to True
        if all(_correct_count.values()):
            print('Congratulations! You have passed this level! Here is your flag:')
            print_flag()