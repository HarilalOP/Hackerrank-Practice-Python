"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = 0
        return [result := result + nums[i] for i in range(len(nums))]