def titleToNumber(self, columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    res = 0
    m = {chr(65 + i): i + 1 for i in range(26)}
    
    n = len(columnTitle)
    for i in range(n):
        char = columnTitle[n - 1 - i]
        res += m[char] * (26 ** i) 
    return res 