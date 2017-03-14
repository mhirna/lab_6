from is_sorted import is_sorted


def test_is_sorted():
    assert is_sorted([1, 2, 3, 4]) == True


def test_same_num():
    assert is_sorted([1, 1, 1, 1]) == True


def test_arg_type():
    assert is_sorted(5) == None


def test_blanc():
    assert is_sorted([]) == None


def test_type():
    assert is_sorted([1, 2, 5.0]) == True
