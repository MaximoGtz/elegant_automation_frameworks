from pytest import mark
@mark.body
def test_body_functions_as_expected():
    assert True

@mark.body
@mark.regression
def test_body_functions_not_expected():
    assert False == False