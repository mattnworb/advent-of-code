from typing import *


def hash_alg(s: str) -> int:
    n = 0
    for ch in s:
        n += ord(ch)
        n *= 17
        n = n % 256

    assert 0 <= n <= 255
    return n


def part1(inp: str):
    strs = inp.split(",")
    return sum(map(hash_alg, strs))


Lens = tuple[str, int]


def part2(inp: str):
    boxes: dict[int, list[Lens]] = {h: [] for h in range(256)}

    for step in inp.split(","):
        if step.endswith("-"):
            # If the operation character is a dash (-), go to the relevant box and remove
            # the lens with the given label if it is present in the box. Then, move any
            # remaining lenses as far forward in the box as they can go without changing
            # their order, filling any space made by removing the indicated lens. (If no
            # lens in that box has the given label, nothing happens.)
            label = step[:-1]
            h = hash_alg(label)
            # TODO: better to delete by index?
            to_remove: Optional[Lens] = None
            for lens in boxes[h]:
                if lens[0] == label:
                    to_remove = lens
                    break
            if to_remove:
                boxes[h].remove(to_remove)
        else:
            # If the operation character is an equals sign (=), it will be
            # followed by a number indicating the focal length of the lens that
            # needs to go into the relevant box; be sure to use the label maker
            # to mark the lens with the label given in the beginning of the step
            # so you can find it later. There are two possible situations:
            #
            # - If there is already a lens in the box with the same label,
            #   replace the old lens with the new lens: remove the old lens and
            #   put the new lens in its place, not moving any other lenses in
            #   the box.
            # - If there is not already a lens in the box with the same label,
            #   add the lens to the box immediately behind any lenses already in
            #   the box. Don't move any of the other lenses when you do this. If
            #   there aren't any lenses in the box, the new lens goes all the
            #   way to the front of the box.
            label = step[:-2]
            focal_len = int(step[-1])
            h = hash_alg(label)
            match: Optional[int] = None
            for ix, lens in enumerate(boxes[h]):
                if lens[0] == label:
                    match = ix
                    break
            if match is not None:
                boxes[h][match] = (label, focal_len)
            else:
                boxes[h].append((label, focal_len))

    total = 0

    for box_num, box in boxes.items():
        for ix in range(len(box)):
            lens = box[ix]
            focal_len = lens[1]
            total += (box_num + 1) * (ix + 1) * focal_len

    return total
