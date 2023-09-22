import pathlib
import pytest
import day8 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input


def test_signal():
    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    p1, _  = line.split(' | ')
    nums = aoc.signals(p1)
    assert nums[0] == set('cagedb')
    assert nums[1] == set('ab')
    assert nums[2] == set('gcdfa')
    assert nums[3] == set('fbcad')
    assert nums[4] == set('eafb')
    assert nums[5] == set('cdfbe')
    assert nums[6] == set('cdfgeb')
    assert nums[7] == set('dab')
    assert nums[8] == set('acedgfb')
    assert nums[9] == set('cefabd')

def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input) == 26
    assert all(line.split().index('|') == 10 for line in parsed_input)

def test_part2(example):
    parsed_input = aoc.parse(example)
    assert aoc.part2(parsed_input) == 61229
