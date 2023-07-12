# solution1: Memoization

def tribonacci(n, memo={}):
    """
    :type n: int
    :rtype: int
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    memo[n] = tribonacci(n-1, memo) + tribonacci(n-2,
                                                 memo) + tribonacci(n-3, memo)
    return memo[n]

# Solution 2: Recursion


def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
