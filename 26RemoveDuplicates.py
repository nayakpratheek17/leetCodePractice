class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        
        if nums == []:
            return 0
        
        i = 0
        j = 1
        
        while i <= N - 2 and j <= N - 1:
            if nums[i] == nums[j]:  #if the number is equal to the next number then we pop
                nums.pop(i)
                
            else:
                i += 1
                j += 1
            
            N = len(nums)
        
        return len(nums)
