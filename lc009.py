# 判断一个数是否是回文数

def solution(x: int):
    return str(x) == str(x)[::-1]
