from checker import step_3_check, _correct_count
from conftest import check_output


def test_incorrect_test_data(trained_model, split_data, capfd):
    model, _, _ = trained_model
    X_train, _, _, _ = split_data
    incorrect_y_pred = model.predict(X_train)
    step_3_check(incorrect_y_pred)
    captured = capfd.readouterr()
    error_msg = "`y_pred` doesn't match the expected prediction output, did you use the correct data for predicting?"
    assert _correct_count['step 3'] == False
    assert check_output(captured.out, msg=error_msg)


def test_correct_check(predictions, capfd):
    y_pred = predictions
    step_3_check(y_pred)
    captured = capfd.readouterr()
    assert _correct_count['step 3'] == True
    assert check_output(captured.out)