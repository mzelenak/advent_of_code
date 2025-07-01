import pytest
import pathlib

import plutonian_pebbles as pp


this_dir = pathlib.Path(__file__).parent.resolve()


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("input_test_1.txt", [0, 1, 10, 99, 999]),
        ("input_test_2.txt", [125, 17]),
    ],
)
def test_read_file(filename, expected):
    assert pp.read_input(str(this_dir / filename)) == [str(x) for x in expected]


@pytest.mark.parametrize(
    "filename, blinks, expected",
    [
        ("input_test_1.txt", 1, 7),
        ("input_test_2.txt", 6, 22),
    ],
)
def test_main(filename, blinks, expected):
    assert pp.main([str(this_dir / filename), blinks]) == expected