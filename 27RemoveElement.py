class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        
        i = 0
        
        while i < N:
            if nums[i] == val:
                nums.pop(i)
                N = len(nums)   # update the length after popping of the element
            else:
                i += 1
            
        return len(nums)
