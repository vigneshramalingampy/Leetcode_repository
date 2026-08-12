class Solution:
    def longestPalindrome(self, s: str) -> str:
        longer =0
        sss = ""
        for i in range(len(s)):
            new_s = s[i:]
            while(new_s !=""):
                if (new_s == new_s[::-1] and len(new_s)>longer):
                    longer = len(new_s)
                    sss = new_s
                new_s=new_s[:-1]
        return sss