class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = -1

        # 去除前后空格
        s = s.strip()

        # 首先要保证数组不越界
        # 然后当第一次遇到空格时就可以返回了
        while n * -1 <= len(s) and s[n] != ' ':
            n = n - 1

        return (n * -1) - 1
