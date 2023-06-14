def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    res = []
    map = {}

    for num in nums1:
        map[num] = map[num] + 1 if num in map else 1

    for num in nums2:
        if num in map and map[num] > 0:
            res.append(num)
            map[num] = 0
    return res