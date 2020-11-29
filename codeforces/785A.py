n = int(input())

faces = 0
for i in range(n):
    line = input()

    if line == "Tetrahedron":
        faces += 4
    elif line == "Cube":
        faces += 6
    elif line == "Octahedron":
        faces += 8
    elif line == "Dodecahedron":
        faces += 12
    elif line == "Icosahedron":
        faces += 20

print(faces)
