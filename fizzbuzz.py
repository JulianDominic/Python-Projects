"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
"""
class Solution:
    def fizzbuzz(self, n):
        fizzbuzz = [(not i % 3) * "Fizz" + (not i % 5) * "Buzz" or str(i) for i in range(1, n+1)]
        print(fizzbuzz)

run = Solution()
run.fizzbuzz(3)
run.fizzbuzz(5)
run.fizzbuzz(15)


# print(not 6 % 3)
# print((not 6) % 3)
# print(not (6 % 3))
# print((not 6 % 3) == (not (6 % 3)))
# print((not 6 % 3) == ((not 6) % 3))