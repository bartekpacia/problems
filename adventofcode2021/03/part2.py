nums_str: list[str] = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        nums_str.append(line)


def most_common_bit_in_pos(pos: int) -> int | None:
    """
    returns 1 if 1 is more common, 0 if 0 is more common, None if they are
    equally common
    """
    zeros = 0
    ones = 0
    for num_str in nums_str:
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


def least_common_bit_in_pos(pos: int) -> int | None:
    """
    returns 1 if 1 is less common, 0 if 0 is less common, None if they are
    equally common
    """
    zeros = 0
    ones = 0
    for num_str in nums_str:
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


# The problem is Step 3: Repeat the process! Don't take remove numbers into
# account


def calc_rating(least_common: bool = False) -> int | None:
    filtered_nums: set[str] = set(nums_str)
    for pos in range(12):
        if least_common:
            common_bit = least_common_bit_in_pos(pos)
            print(f"lcb for {pos=}: {common_bit}")
        else:
            common_bit = most_common_bit_in_pos(pos)
            print(f"mcb for {pos=}: {common_bit}")
        if not common_bit:
            if least_common:
                common_bit = 0
            else:
                common_bit = 1

        common_bit = str(common_bit)

        for num in filtered_nums.copy():
            bit = num[pos]
            if bit != common_bit:
                if num in filtered_nums:
                    filtered_nums.remove(num)

        print(len(filtered_nums))
        if len(filtered_nums) == 1:
            last_element = filtered_nums.pop()
            print(f"{last_element=}")
            return int(last_element, 2)


generator_rating = calc_rating()
scrubber_rating = calc_rating(least_common=True)
# print(f"{generator_rating=}, {scrubber_rating=}")

# print(generator_rating * scrubber_rating)
