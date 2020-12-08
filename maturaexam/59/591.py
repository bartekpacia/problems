def custom_decompose(num: int) -> list[int]:
  print("decomposing", num)
  factor = 2

  if num % 2 == 0:
    return False

  factors = set()
  while num > 1:
    if num % 2 == 0:
      return False

    while (num % factor != 0):
      num = num // factor
    
    factors.add(factor)

    if len(factors) > 3:
      return False

  print(num, factor, factors)
  factor += 2

  return len(factors) == 3

def main():
  with open("liczby.txt", "r") as f:
    liczby = [int(line.strip()) for line in f.readlines()]

  count = 0
  for liczba in liczby:
    is_ok = custom_decompose(liczba)
    if is_ok:
      count+=1


  print("zad1:", count)

main()