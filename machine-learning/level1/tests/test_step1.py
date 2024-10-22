from checker import step_1_check, _correct_count
from conftest import check_output
from sklearn.model_selection import train_test_split


# Make sure that data for X is correct (X_train length + X_test length == X length)
def test_incorrect_X(split_data, capfd):
    X_train, _, y_train, y_test = split_data
    step_1_check(X_train, X_train, y_train, y_test)
    captured = capfd.readouterr()
    error_msg = "X_train and X_test don't match the expected data, did you pass the correct value to `train_test_split()` for X?"
    assert _correct_count['step 1'] == False
    assert check_output(captured.out, msg=error_msg)


# Make sure that data for y is correct (y_train length + y_test length == y length)
def test_y(split_data, capfd):
    X_train, X_test, y_train, _ = split_data
    step_1_check(X_train, X_test, y_train, y_train)
    captured = capfd.readouterr()
    error_msg = "y_train and y_test don't match the expected data, did you pass the correct value to `train_test_split()` for y?"
    assert _correct_count['step 1'] == False
    assert check_output(captured.out, msg=error_msg)


# Make sure that data is split 80% training 20% testing
def test_incorrect_data_split(california_data, capfd):
    # Makes sure that error is thrown if data isn't 80% training and 20% testing
    X, y = california_data
    # Split data incorrectly into 70% training and 30% testing
    incorrect_test_size = 0.3
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=incorrect_test_size, random_state=42)
    
    step_1_check(X_train, X_test, y_train, y_test)

    # Get error message printed out
    captured = capfd.readouterr()

    # Make sure that correct error message is thrown
    error_msg = 'X_train is not 80% of the dataset, did you set `test_size` correctly?'
    assert _correct_count['step 1'] == False
    assert check_output(captured.out, msg=error_msg)


# Make sure that random state is set to 42 (each parameter should match its correct equivalent)
def test_incorrect_random_state(california_data, capfd):
    X, y = california_data
    incorrect_random_state = 23
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=incorrect_random_state)
    step_1_check(X_train, X_test, y_train, y_test)
    captured = capfd.readouterr()
    error_msg = "Split data doesn't match what's expected, did you set `random_state` to be 42?"
    assert _correct_count['step 1'] == False
    assert check_output(captured.out, msg=error_msg)


# Make sure that it shows "Correct" when the solution is correct
def test_correct_check(split_data, capfd):
    X_train, X_test, y_train, y_test = split_data
    step_1_check(X_train, X_test, y_train, y_test)
    captured = capfd.readouterr()
    assert _correct_count['step 1'] == True
    assert check_output(captured.out)