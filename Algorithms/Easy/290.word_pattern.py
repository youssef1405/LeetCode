# first solution
def wordPattern(self, pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    dic = {}
    s_list = s.split(' ')
    if len(pattern) != len(s_list) or len(set(pattern)) != len(set(s_list)):
        return False
        
    for i in range(len(pattern)):
        if pattern[i] not in dic:
            dic[pattern[i]] = s_list[i]
        else:
            if dic[pattern[i]] != s_list[i]:
                return False
    return True


# second solution

    s_list = s.split()
    return map(pattern.index, pattern) == map(s_list.index, s_list)