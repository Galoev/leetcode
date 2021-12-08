class NumArray:

    def __init__(self, nums: List[int]):
        self.part_sums = list()
        cur_sum = 0
        for num in nums:
            cur_sum += num
            self.part_sums.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:
        left -= 1
        if left < 0:
            return self.part_sums[right]
        return self.part_sums[right] - self.part_sums[left]