class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val =  0
        for i in range(len(s)-1,-1,-1):
            # print("input: ",s[i])
            if s[i]!=" ":
                val +=1
            if s[i]!=" " and s[i-1] ==" ":
                break
        return(val)