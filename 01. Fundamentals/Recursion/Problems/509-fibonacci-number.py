# https://leetcode.com/problems/fibonacci-number/

# Finding the fibonacci number of a given n-th term using recursive method
# Time Complexity: O(2^n)
# Space Complexity: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
