def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # solution 1
    return haystack.find(needle)


    # solution 2
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i: i + len(needle)] == needle:
            return i
    return -1 