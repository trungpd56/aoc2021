import pathlib
import pytest
import day11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
   puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
   return puzzle_input

@pytest.fixture
def example2():
   puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
   return puzzle_input

def test_flash(example1):
    parsed_input = aoc.parse(example1)
    assert parsed_input[1][1] == 9
    assert aoc.solution(parsed_input, n=2)[0] == 9

def test_part1(example2):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example2)
    assert aoc.solution(parsed_input) == (1656, 195)

