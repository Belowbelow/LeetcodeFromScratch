# 将罗马数字转换为整数 

def solution(s: str):
    c = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    nums = [1, 5, 10, 50, 100, 500, 1000]
    d = {}

    for i in range(7):
        d[c[i]] = i

    ps = ''
    for i in s:
        ps += str(d[i])

    minus = []
    sum = 0

    for i in range(len(ps) - 1):
        if int(ps[i]) < int(ps[i + 1]):
            minus.append(int(ps[i]))
            continue
        sum += nums[int(ps[i])]
    sum += nums[int(ps[-1])]

    for k in minus:
        sum -= nums[k]
    return sum

s = "MMDDCCLLXXIV"
n = solution(s)
print(n)

