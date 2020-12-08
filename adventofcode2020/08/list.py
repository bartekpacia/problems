l = []

for i in range(1_000_000):
  l.append(i)
  print(f"appended {i}")

for i in l:
  print(i)