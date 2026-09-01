class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""

        for i in range(len(min(strs, key=len))):
            if len(set([s[i] for s in strs])) == 1:
                lcp += strs[0][i]
            else: break
        
        return lcp
