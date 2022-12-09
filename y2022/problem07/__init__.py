from __future__ import annotations

from typing import *


class Node:
    def __init__(self, parent=None) -> None:
        self.dirs: Dict[str, Node] = {}
        self.files: Dict[str, int] = {}
        self._parent = parent

    def get_dir(self, dirname) -> Node:
        return self.dirs[dirname]

    def add_dir(self, dirname) -> None:
        child = Node(parent=self)
        self.dirs[dirname] = child

    def add_file(self, filename: str, size: int) -> None:
        self.files[filename] = size

    def parent(self) -> Optional[Node]:
        return self._parent

    def childdirs(self) -> Iterable[Node]:
        return self.dirs.values()

    # The total size of a directory is the sum of the sizes of the files it
    # contains, directly or indirectly. (Directories themselves do not count as
    # having any intrinsic size.)
    def size(self) -> int:
        fs = sum(filesize for filesize in self.files.values())
        if self.dirs:
            return fs + sum(d.size() for d in self.dirs.values())
        else:
            return fs


def parse(inp: str) -> Node:
    root = Node(parent=None)
    current = root

    for line in inp.split("\n"):
        tokens = line.split(" ")
        if tokens[0] == "$":
            listing = False
            if tokens[1] == "cd":
                path = tokens[2]
                if path == "/":
                    current = root
                elif path == "..":
                    # go up one dir
                    p = current.parent()
                    if p is not None:
                        current = p
                    else:
                        raise ValueError("cannot cd .., already at /")
                else:
                    # for now at least, input only contains cd commands that are relative to CWD
                    current = current.get_dir(path)
            elif tokens[1] == "ls":
                listing = True
            else:
                raise ValueError("unknown cmd: " + tokens[1])
        elif listing:
            if tokens[0] == "dir":
                current.add_dir(tokens[1])
            else:
                # file and size
                name = tokens[1]
                size = int(tokens[0])
                current.add_file(name, size)
        else:
            raise ValueError("unsure how to handle line: " + line)
    return root


def part1(inp: str):
    root_node = parse(inp)

    # To begin, find all of the directories with a total size of at most 100000,
    # then calculate the sum of their total sizes.
    bigdirs = []

    queue = [root_node]
    while queue:
        node = queue.pop()
        size = node.size()
        if size <= 100_000:
            bigdirs.append(size)
        queue.extend(node.childdirs())
    return sum(bigdirs)


def part2(inp: str):
    root_node = parse(inp)

    total_disk_space = 70_000_000
    need_unused_space = 30_000_000

    unused_space = total_disk_space - root_node.size()
    deletion_target = need_unused_space - unused_space

    # Find the smallest directory that, if deleted, would free up enough space
    # on the filesystem to run the update. What is the total size of that
    # directory?

    smallest_dir_to_delete_size = 0

    queue = [root_node]
    while queue:
        node = queue.pop()
        size = node.size()

        if size >= deletion_target and (
            smallest_dir_to_delete_size == 0 or size < smallest_dir_to_delete_size
        ):
            smallest_dir_to_delete_size = size

        queue.extend(node.childdirs())

    return smallest_dir_to_delete_size
