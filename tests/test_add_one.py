from inm_package.add_one import plus_one


def test_plus_one():
    # Test with positive number
    assert plus_one(3) == 4
    # Test with negative number
    assert plus_one(-1) == 0
