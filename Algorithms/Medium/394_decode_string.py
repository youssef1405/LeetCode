class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        string_stack = []
        num = ''
        output = ''

        for ch in s:
            if ch.isnumeric():
                num += ch
            elif ch == '[':
                num_stack.append(int(num))
                string_stack.append(output)
                num = ''
                output = ''
            elif ch == ']':
                output = string_stack.pop() + num_stack.pop() * output
            else:
                output += ch

        return output
