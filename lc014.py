# 找出最长公共子前缀

def solution(l: list[str]) -> str:
    if not l:
        return ""
    prefix, count = l[0], len(l)
    for i in range(1, count):
        prefix = lp(prefix, l[i])
        if not prefix:
            break
    return prefix

def lp(s1, s2):
    l, i = min(len(s1), len(s2)), 0
    while i < l and s1[i] == s2[i]:
        i += 1
    return s1[:i]
l = ['abcd', 'abcddd', 'abcef', 'abcdddde']
print(solution(l))

