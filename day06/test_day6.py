import pathlib
import pytest
import day6 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert parsed_input == [3,4,3,1,2]
    assert aoc.solution(parsed_input) == 26
    assert aoc.solution(parsed_input, times=256) == 26984457539

