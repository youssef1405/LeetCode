def minDeletionSize(strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    n, m = len(strs), len(strs[0])
    del_count = 0
    for i in range(m):
        for j in range(n - 1):
            if strs[j][i] > strs[j+1][i]:
                del_count += 1
                break
    return del_count