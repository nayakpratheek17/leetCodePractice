class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if needle[0:len(needle)] == haystack[i:(i+len(needle))]:      # entire needle is searched throughout the haystack 
                return i
        else:
            return -1
