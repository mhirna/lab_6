from all_prefixes import all_prefixes


def test_type():
    assert all_prefixes(3) == None


def test_all_prefixes():
    assert all_prefixes('lock') == {'l', 'loc', 'lo', 'lock'}


def test_mult_let():
    assert all_prefixes('pepsi') == {'pep', 'peps', 'pepsi', 'p', 'pe', 'psi', 'ps'}


def test_blanc():
    assert all_prefixes('') == set()


test_all_prefixes()
test_blanc()
test_mult_let()
test_type()
