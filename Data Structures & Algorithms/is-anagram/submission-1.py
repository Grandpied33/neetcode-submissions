class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettersT = {}
        for i in s:
            if i in letters:
                letters[i] = letters[i]+1
            else:
                letters[i]=1

        for i in t:
            if i in lettersT:
                lettersT[i] = lettersT[i]+1
            else:
                lettersT[i]=1
        if letters != lettersT:
            return False
        else:
            return True
