
# solution 1: recursion
def fib(self, n):
    """
    :type n: int
    :rtype: int
    """
    seq = 0
    
    if n <= 1:
        return n
    
    return self.fib(n-1) + self.fib(n-2)


# solution 2: memoization
def fib(self, n):
    """
    :type n: int
    :rtype: int
    """
    memo = {}
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = self.fib(n-1) + self.fib(n-2)
    return memo[n]