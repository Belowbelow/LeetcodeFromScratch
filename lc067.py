class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = self.b2n(a) + self.b2n(b)
        return self.n2b(r)

    def b2n(self, a: str) -> int:
        ret = 0
        for i in range(len(a)):
            ret += int(a[i]) * pow(2, len(a) - i - 1)
        return int(ret)

    def n2b(self, n: int) -> str:
        if n == 0:
            return "0"
        s = []
        while n > 0:
            s.append(str(n % 2))
            n = n // 2
        return ''.join(s[::-1])

s = Solution()
a = '101'
b = '1'
print(s.addBinary(a, b))
