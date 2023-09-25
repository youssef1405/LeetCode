class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        pre, curr = None, slow
        while curr:
            curr.next, pre, curr = pre, curr, curr.next

        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
