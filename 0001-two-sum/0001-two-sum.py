class Solution(object):
    def twoSum(self, nums, target):
      for i in range(len(nums)):
        for j in range(len(nums)):
            complement = target - nums[i]
            if nums[j] == complement:
                if i!=j:
                    return[i,j]
        

    
        