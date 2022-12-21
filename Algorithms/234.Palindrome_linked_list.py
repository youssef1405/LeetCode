# Solution 1: O(n) time, O(n) space
#-----------------------------------
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr_node = head 
        values = [] 
        while curr_node:
            values.append(curr_node.val) 
            curr_node = curr_node.next 
        
        return values == values[::-1]


#Solution 2: o(n) time, o(n) space
#----------------------------------

class Solution:
    def isPalindrome(self, head) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True