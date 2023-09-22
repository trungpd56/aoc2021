import pathlib
import pytest
import day5 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_parse(example):
    data = aoc.parse(example)
    assert data[0] == ((0, 9), (5, 9))


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.solution(parsed_input) == 5

def test_part2(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    # assert aoc.solution([((1, 1), (3, 3))], p2=True) == 3
    assert aoc.solution(parsed_input, p2=True) == 12


