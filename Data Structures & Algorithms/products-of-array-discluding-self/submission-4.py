class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = []
        produit = 1
        for i, n in enumerate(nums):
            results.append(produit)
            produit = produit*n
        produit = 1
        for i in range(len(nums) -1, -1,-1):
            results[i] = results[i]*produit
            produit *= nums[i]
        return(results)
        