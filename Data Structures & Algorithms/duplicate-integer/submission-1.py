class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i not in seen and seen != 1:
                seen[i] = 1
            else:
                return True
        
        return False