class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)

        if needle not in haystack:
            return -1

        res_val = []

        for i in range(len(haystack) - len_needle + 1):

            res_val = []

            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    res_val.append(needle[j])
                else:
                    break

            if ''.join(res_val) == needle:
                return i

        return -1