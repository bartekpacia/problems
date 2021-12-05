# list of vectors
vectors: list[tuple[tuple[int, int], tuple[int, int]]] = []

with open("sample.txt") as file:
    for line in file:
        seg = line.strip().split("->")
        x1, y1 = tuple(map(lambda x: int(x), seg[0].strip().split(",")))
        x2, y2 = tuple(map(lambda x: int(x), seg[1].strip().split(",")))

        v = ((x1, y1), (x2, y2))
        vectors.append(v)

for v in vectors:
    print(v)
