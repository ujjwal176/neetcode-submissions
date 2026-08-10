class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       prvsval ={}
       for i,j in enumerate(nums):
        diff = target - j 
        if diff in prvsval:
            return [prvsval[diff],i]
        prvsval[j]=i
          