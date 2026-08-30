class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i]+=1
        sorted_items = sorted(
            seen.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return [number for number, frequency in sorted_items[:k]]
            
        