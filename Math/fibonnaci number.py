# iterative bottom-up DP approach, stores previously solved sequences
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
            
        values = [0, 1]
        for i in range(2, n):
            values.append(values[i- 1] + values[i - 2])

        return values[n - 1] + values[n - 2]
    
# recursive solution, however inefficient since it solves the same fib number more than once
class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n==0:
            return n
        
        return self.fib(n-1) + self.fib(n-2)