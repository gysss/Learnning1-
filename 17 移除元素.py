"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    try:
        for i in range(len(nums)):
            nums.remove(val)
    except ValueError:
        return len(nums)

if __name__ == '__main__':
    nums = [1,3,3,2]
    removeElement(nums, 3)
    print(nums)

    # 更快的方法
    # def removeElement(nums, val):
    #     while val in nums:
    #         nums.remove(val)
    #     return len(nums)
