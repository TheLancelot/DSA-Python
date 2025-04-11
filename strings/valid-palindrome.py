import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= re.sub(r'[^a-zA-Z0-9]', '', s)

        # s = ''.join(char for char in s if char.isalnum())

        # return s==s[::-1]
        # return s==''.join(reversed(s))

        i=0
        end=len(s)-1
        while i<end:
            if s[i]==s[end]:
                i+=1
                end-=1
                continue
                
            else:
                return False

        return True    

inp=input("Enter string to check: ")
print(Solution().isPalindrome(inp))
        




        