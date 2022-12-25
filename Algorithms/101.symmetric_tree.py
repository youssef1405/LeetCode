def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return self.is_mirror(root.left, root.right)
def is_mirror(self, left, right):
    if left is None and right is None:
        return True 
    if left is None or right is None:
        return False
    return (left.val == right.val) \
    and self.is_mirror(left.left, right.right) \
    and self.is_mirror(left.right, right.left) 