class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        popped_index = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popped_index]:
                stack.pop()
                popped_index += 1
        return popped_index == len(popped)
