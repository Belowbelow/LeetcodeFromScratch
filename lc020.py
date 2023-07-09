# 判断一个只有括号的字符串是否逻辑正确

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        judge = deque()
        for i in s:
            if len(judge) == 0:
                judge.append(i)
            else:
                if judge[-1] == '(' and i == ')':
                    judge.pop()
                if judge[-1] == '[' and i == ']':
                    judge.pop()
                if judge[-1] == '{' and i == '}':
                    judge.pop()
        if len(judge) == 0:
            return True
        return False
