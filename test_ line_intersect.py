from line_intersect import line_intersect


def test_line_intersect():
    assert line_intersect([(0.0, 0.0), (1.0, 3.0)], [(0.0, 2.0), (2.0, 0.0)]) == (0.5, 1.5)


def test_type_arg():
    assert line_intersect(1, 2) == None


def test_paralel():
    assert line_intersect([(0.0, 0.0), (1.0, 1.0)], [(0.0, 1.0), (1.0, 2.0)]) == None


def test_same():
    assert line_intersect([(0.0, 0.0), (1.0, 1.0)], [(0.0, 0.0), (1.0, 1.0)]) == [(0.0, 0.0), (1.0, 1.0)]


def test_list_len():
    assert line_intersect(['one'], ['two']) == None


def test_list_arg():
    assert line_intersect(['one', 'one'], ['two', 'two']) == None


test_line_intersect()
test_list_arg()
test_list_len()
test_paralel()
test_same()
test_type_arg()
