from checker import step_2_check, _correct_count
from conftest import check_output
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier


def test_incorrect_model(capfd):
    model = DecisionTreeClassifier()
    step_2_check(model)
    captured = capfd.readouterr()
    error_msg = f"Expected `model` to be of type LinearRegressor but got an object of type `{type(model)}`"
    assert _correct_count['step 2'] == False
    assert check_output(captured.out, msg=error_msg)


# Make sure model is fitted
def test_incorrect_train(capfd):
    model = LinearRegression()
    step_2_check(model)
    captured = capfd.readouterr()
    error_msg = 'You have not fit the model.'
    assert _correct_count['step 2'] == False
    assert check_output(captured.out, msg=error_msg)


def test_correct_check(trained_model, capfd):
    model, _, _ = trained_model
    step_2_check(model)
    captured = capfd.readouterr()
    assert _correct_count['step 2'] == True
    assert check_output(captured.out)