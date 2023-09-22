import pathlib
import pytest
import day15 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert parsed_input[1][1] == 3
    assert aoc.part1(parsed_input) == 40


def test_genmap(example):
    parsed_input = aoc.parse(example)
    gmap = aoc.genmap(parsed_input)
    assert gmap[0][10] == 2
    assert gmap[0][49] == 6
    assert gmap[49][49] == 9


def test_part2(example):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.part2(parsed_input) == 315
