import pathlib
import pytest
import day3 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input) == 198


def test_rating(example):
    parsed_input = aoc.parse(example)
    assert aoc.rating(parsed_input, most=True) == "10111"


def test_rating2(example):
    parsed_input = aoc.parse(example)
    assert aoc.rating(parsed_input, most=False) == "01010"


def test_part2(example):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.part2(parsed_input) == 230
