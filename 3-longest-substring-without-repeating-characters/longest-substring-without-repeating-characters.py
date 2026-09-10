class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1 :
            return 1
        substring = []
        stringer =""
        for x in s:
            if x not in substring:
                substring.append(x)
            else:
                if len(substring) > len(stringer):
                    stringer = "".join(substring)
                index = substring.index(x)
                substring = substring[index + 1:]
                substring.append(x)
        return max(len(substring), len(stringer))
        



        