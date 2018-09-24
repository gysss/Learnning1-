"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
"""
#我采用的方法是遍历+二分查找，比较慢

def twoSum( numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    lenOfNumbers = len(numbers)
    low = 0
    high = lenOfNumbers - 1
    for i in range(lenOfNumbers):
        anotherOne = target - numbers[i]
        low = i + 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == anotherOne:
                return [i + 1, mid + 1]
            elif numbers[mid] > anotherOne:
                high = mid - 1
            else:
                low = mid + 1

if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))

    # 很巧妙的方法
    # def twoSum(self, numbers, target):
    #     """
    #     :type numbers: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     i, j = 0, len(numbers) - 1
    #     while i < j:
    #         if numbers[i] + numbers[j] > target:
    #             j -= 1
    #         if numbers[i] + numbers[j] == target:
    #             return [i + 1, j + 1]
    #         if numbers[i] + numbers[j] < target:
    #             i += 1
