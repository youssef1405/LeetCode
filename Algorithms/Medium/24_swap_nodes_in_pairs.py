class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy

    while head and head.next:
        curr = head
        next = head.next
        pre.next = next
        curr.next = next.next
        next.next = curr
        pre = curr
        head = curr.next

    return dummy.next