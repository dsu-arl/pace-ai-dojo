import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


_correct_count = {
    'step 1': False,
    'step 2': False,
    'step 3': False,
    'step 4': False
}


class _Solution:
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)


def _color_text(text, color):
    color_code = ''
    if color == 'red':
        color_code = '\033[31m'
    elif color == 'green':
        color_code = '\033[32m'
    reset_code = '\033[0m'
    return f'{color_code}{text}{reset_code}'


def step_1_check(X_train, X_test, y_train, y_test):
    global _correct_count
    try:
        # Make sure that data for X is correct (X_train length + X_test length == X length)
        assert (X_train.shape[0] + X_test.shape[0]) == _Solution.X.shape[0], "X_train and X_test don't match the expected data, did you pass the correct value to `train_test_split()` for X?"

        # Make sure that data for y is correct (y_train length + y_test length == y length)
        assert (y_train.shape[0] + y_test.shape[0]) == _Solution.y.shape[0], "y_train and y_test don't match the expected data, did you pass the correct value to `train_test_split()` for y?"

        # Make sure that data is split 80% training 20% testing
        assert X_train.shape[0] / _Solution.X.shape[0] == 0.8, 'X_train is not 80% of the dataset, did you set `test_size` correctly?'
        assert X_test.shape[0] / _Solution.X.shape[0] == 0.2, 'X_test is not 20% of the dataset, did you set `test_size` correctly?'

        # Make sure that random state is set to 42 (each parameter should match its correct equivalent)
        assert np.array_equal(X_train, _Solution.X_train) \
            or np.array_equal(X_test, _Solution.X_test) \
            or np.array_equal(y_train, _Solution.y_train) \
            or np.array_equal(y_test, _Solution.y_test), \
            "Split data doesn't match what's expected, did you set `random_state` to be 42?"
    except AssertionError as e:
        print(_color_text('Incorrect:', 'red'), e)
        _correct_count['step 1'] = False
    else:
        print(_color_text('Correct', 'green'))
        _correct_count['step 1'] = True


def step_2_check(model):
    global _correct_count
    try:
        assert type(model) == type(LogisticRegression()), f"Expected `model` to be of type LogisticRegression but got an object of type `{type(model)}`"
        assert getattr(model, 'coef_', None) is not None, 'You have not fit the model.'
    except AssertionError as e:
        print(_color_text('Incorrect:', 'red'), e)
        _correct_count['step 2'] = False
    else:
        print(_color_text('Correct', 'green'))
        _correct_count['step 2'] = True


def step_3_check(y_pred):
    global _correct_count
    try:
        assert np.array_equal(y_pred, _Solution.y_pred), "`y_pred` doesn't match the expected prediction output, did you use the correct data for predicting?"
    except AssertionError as e:
        print(_color_text('Incorrect:', 'red'), e)
        _correct_count['step 3'] = False
    else:
        print(_color_text('Correct', 'green'))
        _correct_count['step 3'] = True


def step_4_check(accuracy):
    global _correct_count
    try:
        assert accuracy == _Solution.accuracy, "`accuracy` doesn't match the expected value, did you pass the correct values to `accuracy_score()`?"
    except AssertionError as e:
        print(_color_text('Incorrect:', 'red'), e)
        _correct_count['step 4'] = False
    else:
        print(_color_text('Correct', 'green'))
        _correct_count['step 4'] = True

        # Add in check to see if all values in _correct_count are set to True
        if all(_correct_count.values()):
            print('Congratulations! You have passed this level! Here is your flag:')
            print('pwn.college{Y7o9vEOKP3wb9p32wW14Ypr9XIn.dljM3MDL2QjNzYzW}')
        else:
            print("You passed this step, but not all of them. Make sure each step says 'Correct'.")