from y2021.problem10 import *


def test_find_illegal():
    assert find_illegal("{([(<{}[<>[]}>{[]{[(<()>") == "}"
    assert find_illegal("[({(<(())[]>[[{[]{<()<>>") is None


example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def test_part1_example():
    assert part1(example) == 26397


def test_part2_example():
    # TODO: populate
    assert part2(example)
