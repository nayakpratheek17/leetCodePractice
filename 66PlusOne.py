class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
        if i == -1:		# if all the elements are 9 after the end of look we need to add 1 at the beginning
            digits.insert(0, 1)
        return digits
