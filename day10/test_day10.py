import pathlib
import pytest
import day10 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input

@pytest.mark.parametrize("puzzle_input,expected",
    [
        ("{([(<{}[<>[]}>{[]{[(<()>", '}'),
        ("[[<[([]))<([[{}[[()]]]", ')'),
        ("[{[{({}]{}}([{[{{{}}([]", ']'),
        ("[<(<(<(<{}))><([]([]()", ')'),
        ("<{([([[(<>()){}]>(<<{{", '>'),
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]")
    ])
def test_check(puzzle_input, expected):
    """Test part 1 on example input."""
    assert aoc.check(puzzle_input)[1] == expected

def test_part1(example):
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input) == 26397

def test_cal():
    assert aoc.cal('])}>') == 294
    assert aoc.cal('}}]])})]') == 288957
    
def test_part2(example):
    parsed_input = aoc.parse(example)
    assert aoc.part2(parsed_input) == 288957






