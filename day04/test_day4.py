import pathlib
import pytest
import day4 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_parse(example):
    nums, boards = aoc.parse(example)
    assert nums[:4] == [7, 4, 9, 5]
    assert boards[0][0] == [22, 13, 17, 11, 0]
    assert aoc.is_win(boards[0], [22, 13, 17, 11, 0]) == True
    assert aoc.is_win(boards[1], [3, 9, 19, 20, 14]) == True

def test_score():
    assert aoc.score([[1,1,1,1,1],[1,1,1,1,2]], [0,1]) == 2


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.solution(parsed_input) == (4512, 1924)


