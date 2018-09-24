"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对,
例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
"""
def arrayPairSum( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    sum = 0
    for i in nums[::2]:
        sum += i
    return sum

if __name__ == '__main__':
    print(arrayPairSum([1,4,3,2]))


 # def arrayPairSum(self, nums):
 #        """
 #        :type nums: List[int]
 #        :rtype: int
 #        """
 #        nums.sort()
 #        return sum(nums[::2])
