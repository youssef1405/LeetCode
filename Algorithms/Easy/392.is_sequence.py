def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    s_index = 0
    for t_index in range(len(t)):
        if s_index <= len(s) - 1:
            if s[s_index] == t[t_index]:
                s_index += 1
    return s_index == len(s)