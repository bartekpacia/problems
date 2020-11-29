def rotLeft(arr, d):
    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5]
rot = int(input("rotate by: "))
arr = rotLeft(arr, rot)
print(arr)
