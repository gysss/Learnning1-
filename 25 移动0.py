"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""


def moveZeroes( nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    idx = 0  #指针1
    cur = 0  #指针2
    while idx<len(nums):
        if nums[idx]!= 0:
            nums[cur] = nums[idx]
            cur+=1
        idx+=1
    while cur<len(nums):
        nums[cur] = 0
        cur+=1

if __name__ == '__main__':
    nums = [1,0,2,0,3,4]
    moveZeroes(nums)
    print(nums)
