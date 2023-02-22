"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            div_by_3 = i % 3 == 0
            div_by_5 = i % 5 == 0
            
            curr_str = ""
            if div_by_3:
                curr_str += "Fizz"
            if div_by_5:
                curr_str += "Buzz"
            if curr_str == "":
                curr_str += str(i)
            answer.append(curr_str)
        return answer