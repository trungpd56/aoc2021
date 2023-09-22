import pathlib
import pytest
import day12 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return puzzle_input


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return puzzle_input


@pytest.mark.parametrize(
    "fixture, expected", [("example", 10), ("example2", 19), ("example3", 226)]
)
def test_part1(fixture, expected, request):
    """Test part 1 on example input."""
    example = request.getfixturevalue(fixture)
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input) == expected


# @pytest.mark.skip()
@pytest.mark.parametrize(
    "fixture, expected", [("example", 36), ("example2", 103), ("example3", 3509)]
)
def test_part2(fixture, expected, request):
    """Test part 2 on example input."""
    example = request.getfixturevalue(fixture)
    parsed_input = aoc.parse(example)
    assert aoc.part2(parsed_input) == expected
