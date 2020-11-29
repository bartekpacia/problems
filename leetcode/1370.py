class Solution:
    iters = 0

    def pick_largest_smaller_than(self, largest_num: int, s: str):
        largest = "/"
        for char in s:
            if ord(char) > ord(largest) and ord(char) < largest_num:
                largest = char

        return largest if largest != "/" else None

    def pick_smallest_greater_than(self, lower_num: int, s: str):
        smallest = "ź"
        for char in s:
            if ord(char) < ord(smallest) and ord(char) > lower_num:
                smallest = char

        return smallest if smallest != "ź" else None

    def sortString(self, s: str) -> str:
        result = ""

        last_picked = "ź"
        while self.iters < len(s):
            for char in s:
                if self.iters < len(s):
                    if ord(char) < ord(last_picked):
                        last_picked = char

            result += last_picked
            self.iters += 1
            # print(f"appending {last_picked}")

            for char in s:
                if self.iters < len(s):
                    candidate = self.pick_smallest_greater_than(
                        ord(last_picked), s)
                    if not candidate:
                        break

                    last_picked = candidate
                    result += last_picked
                    self.iters += 1
                    # print(f"appending {last_picked}")

            for char in s:
                if self.iters < len(s):
                    if ord(char) > ord(last_picked):
                        last_picked = char

            result += last_picked
            self.iters += 1
            # print(f"appending {last_picked}")

            for char in s:
                if self.iters < len(s):
                    candidate = self.pick_largest_smaller_than(
                        ord(last_picked), s)
                    if not candidate:
                        break

                    last_picked = candidate
                    result += last_picked
                    self.iters += 1
                    # print(f"appending {last_picked}")

        return result, self.iters


t1 = Solution().sortString("aaaabbbbcccc")
print(f"aaaabbbbcccc -> {t1[0]}, l: {t1[1]}")

t2 = Solution().sortString("art")
print(f"rat -> {t2[0]}, l: {t2[1]}")

t3 = Solution().sortString("leetcode")
print(f"leetcode -> {t3[0]}, l: {t3[1]}")

t4 = Solution().sortString("ggggggg")
print(f"ggggggg -> {t4[0]}, l: {t4[1]}")

t5 = Solution().sortString("spo")
print(f"spo -> {t5[0]}, l: {t5[1]}")
