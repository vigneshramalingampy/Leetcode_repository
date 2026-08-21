class Solution:
    def isPalindrome(self, s: str) -> bool:
        result =""
        s=s.lower()
        for i in s:
            if i.isalnum():
                result+=i
        if (result == result[::-1]):
            return True
        else:
            return False