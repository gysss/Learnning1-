"""
给定一个二进制数组， 计算其中最大连续1的个数。
"""
def findMaxConsecutiveOnes( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    ans = []
    for i in nums[:]:
        if i != 1:
            ans.append(count)
            count = 0
        else:
            count+=1
    ans.append(count)
    return max(ans)


if __name__ == '__main__':
    print(findMaxConsecutiveOnes([0]))
