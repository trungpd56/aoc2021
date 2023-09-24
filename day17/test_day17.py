import pathlib
import pytest
import day17 as aoc


def test_part1():
    """Test part 1 on example input."""
    parsed_input = aoc.parse("target area: x=20..30, y=-10..-5")
    assert parsed_input == (20, 30, -10, -5)
    assert aoc.solution(parsed_input)[0] == 45
    assert aoc.solution(parsed_input)[1] == 112


