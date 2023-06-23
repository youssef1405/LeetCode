def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = {}
    for index, num in enumerate(nums):
        if num in dic and index - dic[num] <= k:
            return True
        else:
            dic[num] = index
    return False
