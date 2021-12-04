nums_str: list[str] = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        nums_str.append(line)


def most_common_bit_in_pos(pos: int, items: list[str]) -> int | None:
    """
    returns 1 if 1 is more common, 0 if 0 is more common, None if they are
    equally common
    """
    zeros = 0
    ones = 0
    for num_str in items:
        if num_str[pos] == "0":
            zeros += 1
        elif num_str[pos] == "1":
            ones += 1

    if zeros > ones:
        return 0
    elif ones > zeros:
        return 1
    else:
        return None


def least_common_bit_in_pos(pos: int, items: list[str]) -> int | None:
    """
    returns 1 if 1 is less common, 0 if 0 is less common, None if they are
    equally common
    """
    zeros = 0
    ones = 0
    for num_str in items:
        if num_str[pos] == "0":
            zeros += 1
        elif num_str[pos] == "1":
            ones += 1

    if zeros < ones:
        return 0
    elif ones < zeros:
        return 1
    else:
        return None


def calc_rating_1(nums: list[str], pos: int = 0) -> str:
    print(f"::: {pos:}, {len(nums)=}")
    if len(nums) == 1:
        return nums[0]
    else:
        mcb = most_common_bit_in_pos(pos, nums)
        print(f"returned mcb is {mcb}")
        if mcb == None:
            mcb = 1

        print(f"mcb for {pos=} is {mcb}")

        nums = [n for n in nums if n[pos] == str(mcb)]
        for num in nums:
            print(num)

        pos += 1
        return calc_rating_1(nums, pos)


def calc_rating_2(nums: list[str], pos: int = 0) -> str:
    if len(nums) == 1:
        return nums[0]
    else:
        lcb = least_common_bit_in_pos(pos, nums)
        if lcb == None:
            lcb = 0

        nums = [n for n in nums if n[pos] == str(lcb)]

        pos += 1
        return calc_rating_2(nums, pos)


generator_rating = calc_rating_1(nums_str)
scrubber_rating = calc_rating_2(nums_str)
print(f"{generator_rating=}")
print(f"{scrubber_rating=}")

print(int(generator_rating, 2) * int(scrubber_rating, 2))


# lessons learned
# 1. always make sure that you're comparing values of right type
# 2. read full listings and descriptions!
# 3. beware of truthy and falsy values!
