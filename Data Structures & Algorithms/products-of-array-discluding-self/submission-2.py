class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        gauche = [1] * len(nums)
        droite = [1] * len(nums)

        total = 1
        for i, n in enumerate(nums):
            gauche[i] = total
            total = total * n
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            droite[i] = total
            total = total * nums[i]

        results = []
        for i in range(len(nums)):
            results.append(gauche[i] * droite[i])

        return results