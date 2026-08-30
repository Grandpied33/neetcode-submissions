class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = {}
        stringT= {}
        if len(s) != len(t):
            return False
        else:
            
            for i,n in enumerate(s):
                stringS[n]= stringS.get(n,0)+1
            for i,n in enumerate(t):
                stringT[n]= stringT.get(n,0)+1
            if stringS == stringT:
                print(stringT)
                return True
            else:
                return False

        