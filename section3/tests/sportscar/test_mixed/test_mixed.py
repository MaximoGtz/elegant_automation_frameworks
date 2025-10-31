from pytest import mark

@mark.engine
@mark.body
def test_mixed_markers():
    assert True