# 使用二分查找在一个数组中找到某个数所应该在的位置

import math

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = math.floor((l + r) / 2)
        while l < r:
            if nums[int(mid)] > target:
                r = int(mid - 1)
                mid = (l + r) / 2
            if nums[int(mid)] < target:
                l = int(mid + 1)
                mid = (l + r) / 2
            if nums[int(mid)] == target:
                return int(mid)
        if nums[l] > target: 
            return int(l)
        if nums[l] < target:
            return int(l + 1)
        return int(l)


