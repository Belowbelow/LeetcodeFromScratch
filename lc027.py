# 移除数组中的某个元素

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = 0
        l = len(nums)
        for i in nums:
            if val == i:
                n += 1

        for i in range(n):
            nums.remove(val)

        return l - n
