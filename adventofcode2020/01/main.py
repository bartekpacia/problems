from typing import List

def solve_part_1(nums: List[int]) -> int:
  for num1 in nums:
    for num2 in nums:
      if num1 + num2 == 2020:
        return num1 * num2

# stupid but gets the job done
# maybe i'll make myself to optimize in the future
def solve_part_2(nums: List[int]) -> int:
  for num1 in nums:
    for num2 in nums:
      for num3 in nums:
        if num1 + num2 + num3 == 2020:
          return num1 * num2 * num3

with open("input.txt", "r") as f:
  nums = [int(l) for l in f.readlines()]

answer1 = solve_part_1(nums)
answer2 = solve_part_2(nums)
print(f"multiply (part 1): {answer1}")
print(f"multiply (part 2): {answer2}")
