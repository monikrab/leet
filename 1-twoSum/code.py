class Solution:
     def twoSum(self, nums, target):
         for i in nums:
             for j in nums:
                 if i + j == target:
                     try: nums.index(j, nums.index(i) + 1)
                     except ValueError: continue
                     else: return [nums.index(i), nums.index(j, nums.index(i) + 1)]
