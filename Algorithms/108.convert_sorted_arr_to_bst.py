class Solution:
    def sortedArrayToBST(self, nums):
        return self.makeBST(nums, 0, len(nums))
    
    def makeBST(self, nums, start, end):
        if start >= end: 
            return None
        node = TreeNode(nums[(start + end)//2])
        node.left = self.makeBST(nums, start, (start + end)//2)
        node.right = right=self.makeBST(nums, 1+((start+end)//2), end)
        return node