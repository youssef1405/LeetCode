# Solution 1 using a set
# time = O(m + n)
# space = O(m)


def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    nodes_in_A = set()

    while headA:
        nodes_in_A.add(headA)
        headA = headA.next

    while headB:
        if headB in nodes_in_A:
            return headB 
        headB = headB.next
    return None


# Solution 2 - two pointers
# time o(m+n)
# space O(1)

def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    currA = headA
    currB = headB
    while currA != currB:
        currA = headB if currA is None else currA.next
        currB = headA if currB is None else currB.next 
    
    return currB 
