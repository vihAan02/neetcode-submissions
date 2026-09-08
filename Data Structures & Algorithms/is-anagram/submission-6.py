class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))
        if sortedS == sortedT:
            return True
        else:
            return False
        """
        if len(s) != len(t):
            return False
        else: 
            sMap = {}
            tMap = {}
            sList = list(s)
            tList = list(t)
            for n in s:
                if n in sMap:
                    sMap[n] += 1
                else:
                    sMap[n] = 1

            for n in t:
                if n in tMap:
                    tMap[n] += 1
                else:
                    tMap[n] = 1
            
            return sMap == tMap