class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            mark = str(i)
            
            while isinstance(nums[i] ,int) and (num * nums[i] > 0) and (nums[i] % len(nums) != 0):
                jump = nums[i] 
                nums[i] = mark
                i = (i + jump) % len(nums)
            
            if nums[i] == mark:
                return True
            
        return False