class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''
        for i in digits:
            s += str(i)
        sum_s = int(s) + 1
        ret = []
        for i in str(sum_s):
            ret.append(int(i))
        return ret

s = Solution()
n = [9, 9, 9]
print(s.plusOne(n))
