class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        val = []
        for n in nums:
            seen[n] = seen.get(n, 0)+1
        sorted_scores=sorted(seen.items(), key=lambda item:item[1], reverse=True)
        for i,n in enumerate(sorted_scores[:k]):
            val.append(n[0])
        print(val)
        return val
            