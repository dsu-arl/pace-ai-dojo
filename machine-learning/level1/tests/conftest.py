import sys
import os
# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import _correct_count
import pandas as pd
import pytest
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


_red_color_code = '\033[31m'
_green_color_code = '\033[32m'
_reset_code = '\033[0m'


def check_output(captured, msg=None):
    if msg is None:
        output_msg = f'{_green_color_code}Correct{_reset_code}'
    else:
        output_msg =f'{_red_color_code}Incorrect:{_reset_code} {msg}'
    return output_msg in captured


@pytest.fixture(autouse=True)
def reset_correct_count():
    _correct_count['step 1'] = False
    _correct_count['step 2'] = False
    _correct_count['step 3'] = False
    _correct_count['step 4'] = False


@pytest.fixture(scope='session')
def california_data():
    california = fetch_california_housing()
    df = pd.DataFrame(california.data, columns=california.feature_names)
    df['MedHouseVal'] = california.target

    X = df.drop('MedHouseVal', axis=1)
    y = df['MedHouseVal']

    return X, y

@pytest.fixture(scope='session')
def split_data(california_data):
    X, y = california_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

@pytest.fixture(scope='session')
def trained_model(split_data):
    X_train, X_test, y_train, y_test = split_data
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test

@pytest.fixture(scope='session')
def predictions(trained_model):
    model, X_test, _ = trained_model
    y_pred = model.predict(X_test)
    return y_pred

@pytest.fixture(scope='session')
def mse_loss(trained_model, predictions):
    _, _, y_test = trained_model
    y_pred = predictions
    mse_value = mean_squared_error(y_test, y_pred)
    return mse_value