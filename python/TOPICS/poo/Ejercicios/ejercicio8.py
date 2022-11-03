"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def __init__(self, nums, target):
        self.nums = nums 
        self.target = target
        
    def twoSum(self):
        two_nums = None
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target and i != j:
                    two_nums = [i,j]
        return two_nums
        
obj = Solution([3,3], 6)
print(obj.twoSum())
