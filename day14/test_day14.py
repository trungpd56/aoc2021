import pathlib
import pytest
import day14 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input

def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert parsed_input[0] == 'NNCB'
    assert parsed_input[1]['CH'] == 'B'
    assert aoc.solution(parsed_input) == 1588
    assert aoc.solution(parsed_input, n=40) == 2188189693529
