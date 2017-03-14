from all_prefixes import all_prefixes


def test_type():
    assert all_prefixes(3) == None

def test_all_prefixes():
    assert all_prefixes('lol') == {'l', 'lol', 'lo'}
