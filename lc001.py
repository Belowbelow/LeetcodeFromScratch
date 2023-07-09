# 输入：数组，目标值
# 输出：目标和为目标值的两个数（假定数组中只有一组数符合）

def twoSum(arr: list[int], target: int) -> list[int]:
    if len(arr) < 2:
        raise ValueError("数组中必须包含两个及以上的数字")
    d = dict()
    for i in range(len(arr)):
        if target - arr[i] in d.keys():
            return [i, d[target - arr[i]]]
        else:
            d[arr[i]] = i
    return []
        
