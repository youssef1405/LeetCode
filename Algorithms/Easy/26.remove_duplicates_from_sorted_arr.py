class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[0]
        prev_index = 1
        for i in range(1,len(nums)):
            if nums[i] != prev:
                nums[prev_index] = nums[i]
                prev_index += 1
                prev = nums[i]
        return prev_index