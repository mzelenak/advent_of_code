import pytest
import pathlib

import haunted_wasteland as hw


this_dir = pathlib.Path(__file__).parent.resolve()


def test_read_file():
    expected = {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }
    assert hw.read_input(this_dir / "test_input1.txt") == ("RL", expected)


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("test_input1.txt", 2),
        ("test_input2.txt", 6),
    ],
)
def test_solution(filename, expected):
    assert hw.steps_to_cross_map(*hw.read_input(this_dir / filename)) == expected


def test_solution2():
    assert (
        hw.steps_to_cross_the_map_for_ghosts(
            *hw.read_input(this_dir / "test_input3.txt")
        )
        == 6
    )
