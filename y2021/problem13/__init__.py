from typing import *


def part1(inp: str):
    # represent the paper as a set of x,y coordinates where presence in the set means a X (dot on paper)
    dots = set()

    dotlines, foldlines = inp.split("\n\n")

    for line in dotlines.split("\n"):
        sp = line.split(",")
        x = int(sp[0])
        y = int(sp[1])
        dots.add((x, y))

    sp = foldlines.split("\n")[0][len("fold along ") :].split("=")
    fold_dir = sp[0]
    fold_pos = int(sp[1])

    assert fold_dir in ("x", "y")

    new_paper = set()
    for dot in dots:
        x, y = dot

        if fold_dir == "y":
            if y < fold_pos:
                new_paper.add((x, y))
            elif y == fold_pos:
                # drop because we are folding on this line
                continue
            else:
                # determine new y
                new_y = fold_pos - (y - fold_pos)
                new_paper.add((x, new_y))
        elif fold_dir == "x":
            if x < fold_pos:
                new_paper.add((x, y))
            elif x == fold_pos:
                continue
            else:
                new_x = fold_pos - (x - fold_pos)
                new_paper.add((new_x, y))
    return len(new_paper)


def part2(inp: str):
    dots = set()

    dotlines, foldlines = inp.split("\n\n")

    for line in dotlines.split("\n"):
        sp = line.split(",")
        x = int(sp[0])
        y = int(sp[1])
        dots.add((x, y))

    for line in foldlines.split("\n"):
        sp = line[len("fold along ") :].split("=")
        fold_dir = sp[0]
        fold_pos = int(sp[1])

        assert fold_dir in ("x", "y")

        new_paper = set()
        for dot in dots:
            x, y = dot

            if fold_dir == "y":
                if y < fold_pos:
                    new_paper.add((x, y))
                elif y == fold_pos:
                    # drop because we are folding on this line
                    continue
                else:
                    # determine new y
                    new_y = fold_pos - (y - fold_pos)
                    new_paper.add((x, new_y))
            elif fold_dir == "x":
                if x < fold_pos:
                    new_paper.add((x, y))
                elif x == fold_pos:
                    continue
                else:
                    new_x = fold_pos - (x - fold_pos)
                    new_paper.add((new_x, y))
        dots = new_paper

    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)

    paper: List[str] = []
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if (x, y) in dots:
                line += "#"
            else:
                line += "."
        paper.append(line)
    print("\n".join(paper))
    return len(new_paper)
