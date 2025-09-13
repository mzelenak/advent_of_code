import lanternfish as lfsh


def test_reproduce():
    assert lfsh.reproduce([3, 4, 3, 1, 2], 18) == 26
