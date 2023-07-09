# 最长无重复子串
# 使用滑动窗口

def solution(s: str):
    lookup = set()
    left = 0
    cur_len = 0
    max_len = 0
    n = len(s)
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])
    return max_len

print(solution("asdfaaevbaefashgvuiaefijalsfhawhgol"))
