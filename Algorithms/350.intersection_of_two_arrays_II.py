# solution 1
# time comp. O(m + n)
# space o(m)
def intersect(nums1, nums2):
    dic = {}
    res = []
    for num in nums1:
        dic[num] = dic.get(num, 0) + 1

    for num in nums2:
        if num in dic and dic[num] > 0:
            res.append(num)
            dic[num] -= 1
    return res 


# solution 2 - sorting
# time o(mlog m + nlog n)
# space O(1)
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()

    res = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res 