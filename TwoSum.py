# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target): #nums: List[int], target: int and returntype List[int]: 
        temp_dict = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if temp_dict.get(val, None) is not None:
                return [i, temp_dict.get(val)]
            temp_dict[nums[i]]= i


nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))