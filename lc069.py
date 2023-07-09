class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        elif x >= 4 and x < 9:
            return 2
        else:
            return self.findSqrt(x)
    
    def findSqrt(self, x: int) -> int:
        l = 2
        r = x // 2
        m = (l + r) // 2
        flag = False
        while not flag and l < r:
            if pow(m, 2) < x:
                l = m + 1
                m = (l + r) // 2
            elif pow(m, 2) > x:
                r = m - 1
                m = (l + r) // 2
            else:
                return m
        if pow(l, 2) > x:
            return l - 1
        return l

s = Solution()
n = 121
print(s.mySqrt(n))
