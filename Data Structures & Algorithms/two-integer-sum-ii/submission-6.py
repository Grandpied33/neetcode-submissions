class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        total =0
        total = numbers[left] + numbers[right]
        while total != target:
            total = numbers[left] + numbers[right]
            if total <target :
                left+=1
            elif total >target:
                right-=1
            
        return [left+1,right+1]