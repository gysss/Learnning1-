def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    lenOfnums = len(nums)
    step = k % lenOfnums
    nums[:] = nums[-step:] + nums[:-step]

if __name__ == '__main__':
    list = [1,2,3,4,5,6,7]
    rotate(list, 3)
    print(list)
