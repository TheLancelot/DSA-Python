class Solution:
    #Brute Force
    # def check(self,str1,str2):
    #     if str1== str2*int(len(str1)/len(str2)):
    #         return True
    #     else:
    #         return False


    # def gcdOfStrings(self, str1: str, str2: str) -> str:

    #     if len(str1)<len(str2):
    #         str1,str2=str2,str1
     
    #     i=len(str2)
    #     for j in range(i,0,-1):
    #         if (self.check(str1,str2[:j]) and self.check(str2,str2[:j])):
    #             return str2[:j]
            
    #     return ""

    #Better approach,    
        # if gcd exists then s1+s2=s2+s1

    import math 

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2 != str2+str1:
            return ""
        
        else:
            return str1[:(math.gcd(len(str1),len(str2)))]

    def gcd(self,n1,n2):
        while n1>0 and n2>0:

            if n1>n2:
                n1=n1%n2 #repeatedly subtract means divide by that number and get remainder

            else:
                n2=n2%n1

        return n1 if n2==0 else n2        

        