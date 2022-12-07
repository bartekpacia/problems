import abc
from typing import Callable


class Node:
    __metaclass__ = abc.ABCMeta

    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def get_size(self) -> int:
        """
        If it's a file, return its size
        Returns the sum of all files in this
        """


class DirNode(Node):
    def __init__(self, name: str, parent: "DirNode"):
        super().__init__(name)
        self.nodes: list["Node"] = []
        self.parent = parent

    def add_node(self, node: "Node"):
        self.nodes.append(node)

    def get_size(self):
        return sum(node.get_size() for node in self.nodes)

    def subdir(self, name: str) -> "DirNode":
        for node in self.nodes:
            if node.name == name and isinstance(node, DirNode):
                return node

        raise RuntimeError(f"subdir {name} not found")

    def __str__(self):
        return f"- {self.name} (dir)"

    def tree(self, level: int = 0) -> str:
        output: list[str] = []
        for node in self.nodes:
            output.append("  " * (level + 1) + str(node))
            if isinstance(node, DirNode):
                output.append(node.tree(level=level + 1))

        return "\n".join(output)

    def walk(self, func: Callable[["DirNode"], None]):
        for node in self.nodes:
            if not isinstance(node, DirNode):
                continue

            func(node)
            node.walk(func)


class FileNode(Node):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def get_size(self) -> int:
        return self.size

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"


root = DirNode("/", parent=None)
current_node = root

reading_output = False

with open("input.txt") as file:
    lines = file.readlines()[1:]  # first line is always "$ cd /"

    for l in lines:
        line = l.strip()

        if line.startswith("$"):
            # command parsing mode
            cmd, *args = line.split()[1:]
            if cmd == "ls":
                reading_output = True
            elif cmd == "cd":
                reading_output = False
                arg = args[0]
                if arg == "..":
                    current_node = current_node.parent
                else:
                    new_node = current_node.subdir(name=arg)
                    current_node = new_node

        else:
            assert reading_output == True
            if line.split()[0] == "dir":
                name = line.split()[1]
                current_node.add_node(DirNode(name, parent=current_node))
            elif line.split()[0].isnumeric():
                size = int(line.split()[0])
                name = line.split()[1]
                current_node.add_node(FileNode(name, size))
            else:
                raise RuntimeError("invalid state")

total_size = 0


def count_size(node: DirNode):
    size = node.get_size()
    if size > 100000:
        return
    else:
        global total_size
        total_size += size


root.walk(count_size)
print(total_size)
