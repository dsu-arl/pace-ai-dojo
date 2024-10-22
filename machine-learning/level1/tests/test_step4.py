from checker import step_4_check, _correct_count
from conftest import check_output


def test_loss(capfd):
    # Loss can't be negative
    step_4_check(-1)
    captured = capfd.readouterr()
    error_msg = "`mse` doesn't match the expected value, did you pass the correct values to `mean_squared_error()`?"
    assert _correct_count['step 4'] == False
    assert check_output(captured.out, msg=error_msg)


def test_correct_check(mse_loss, capfd):
    loss = mse_loss
    step_4_check(loss)
    captured = capfd.readouterr()
    assert _correct_count['step 4'] == True
    assert check_output(captured.out)


def test_incomplete_level(mse_loss, capfd):
    # Missing step 3 completion to pass level
    _correct_count['step 1'] = True
    _correct_count['step 2'] = True
    _correct_count['step 4'] = True
    step_4_check(mse_loss)
    captured = capfd.readouterr()
    msg = "You passed this step, but not all of them. Make sure each step says 'Correct'."
    assert msg in captured.out


def test_passed_level(mse_loss, capfd):
    # Make sure all flags in _correct_count are set to True
    _correct_count['step 1'] = True
    _correct_count['step 2'] = True
    _correct_count['step 3'] = True
    _correct_count['step 4'] = True
    step_4_check(mse_loss)
    captured = capfd.readouterr()
    success_msg = 'Congratulations! You have passed this level! Here is your flag:'
    assert success_msg in captured.out