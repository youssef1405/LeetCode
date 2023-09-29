# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry, res = 0, 0
        curr1 = l1
        curr2 = l2
        new_head, tail = None, None

        while curr1 or curr2:
            if curr1 is None:
                res = curr2.val + carry
                curr2 = curr2.next
            elif curr2 is None:
                res = curr1.val + carry
                curr1 = curr1.next
            else:
                res = curr1.val + curr2.val + carry
                curr1 = curr1.next
                curr2 = curr2.next

            if res > 9:
                res -= 10
                carry = 1
            else:
                carry = 0

            if new_head is None:
                new_head = ListNode(res)
                tail = new_head
            else:
                new_node = ListNode(res)
                tail.next = new_node
                tail = new_node

        if carry == 1:
            tail.next = ListNode(carry)
        return new_head
