def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # solution 1
    return map(s.index, s) == map(t.index, t)

    # soltion 2
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))