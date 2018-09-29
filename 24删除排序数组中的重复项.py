"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""

# 因为有序，所以不停地判断下一个是否等于上一个就好了，等于就pop掉，不等就移到下一个

def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

if __name__ == '__main__':
    nums = [0,0,1,1,2,2,3]
    removeDuplicates(nums)
    print(nums)
