digits = input()

arr = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r", "s"],
    ["t", "u", "v"],
    ["w", "x", "y", "z"],
]

# arr[0] = possible letters for 1
# arr[1] = possible letters for 2

mapping = []
for i in digits:
    mapping.append(arr[int(i) - 2])

combinations = []
for i, match1, in enumerate(mapping):
    for j, match2 in enumerate(mapping[i]):
        merged = mapping[0][i] + match2
        combinations.append(merged)


print(combinations)
