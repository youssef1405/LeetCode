def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # solution 1
    #return sorted([num**2 for num in nums])


    # solution 2
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1
    
    for i in range(n-1, -1, -1):
        if abs(nums[left]) < abs (nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        res[i] = square**2
    return res