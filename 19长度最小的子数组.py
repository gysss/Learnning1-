"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0
"""

# 此方法采用双指针，时间复杂度为O(n)
def minSubArrayLen( s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    leftIndex = 0
    rightIndex = 0
    sumOfAll = 0
    nums_len = len(nums)
    minlen = nums_len+1
    while leftIndex<nums_len:
        if rightIndex<nums_len and sumOfAll<s:
            sumOfAll+=nums[rightIndex]
            rightIndex += 1
        else:
            sumOfAll -= nums[leftIndex]
            leftIndex += 1
        if sumOfAll >= s:
            minlen = min(minlen, rightIndex-leftIndex )
    if minlen == nums_len + 1:
        return  0
    return minlen


if __name__ == '__main__':
    print(minSubArrayLen(7, [2,3,1,2,4,3]))
