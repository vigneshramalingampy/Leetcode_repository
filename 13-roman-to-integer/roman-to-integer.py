class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        character = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        while(s!=""):
            last_two = s[-2:]
            last_one = s[-1]
            flag = 0
            if last_two in character:
                result+=value[character.index(last_two)]
                flag=2
            elif last_one in character:
                print(s)
                result+=value[character.index(last_one)]
                flag=1
            s=s[:-(flag)]
        return result
            

        