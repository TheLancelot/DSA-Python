class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)

        # map1={}
        # map2={}
        
        if len(s)!=len(t):
            return False

        # for char in s:
        #     if not char in map1:
        #         map1[char]=0
        #     map1[char]+=1

        # for char in t:
        #     if not char in map2:
        #         map2[char]=0
        #     map2[char]+=1

        # return map1==map2

        #or just use one dictionary, after add s to dict, then remove t from dict, in the end all values should be 0
        freq={}

        # for cs, ct in zip(s, t):
        #     freq[cs] = freq.get(cs, 0) + 1
        #     freq[ct] = freq.get(ct, 0) - 1

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 0
            freq[s[i]] += 1

            if t[i] not in freq:
                freq[t[i]] = 0
            freq[t[i]] -= 1

        return all(value == 0 for value in freq.values())
    # If all values are 0, then it's an anagram

#if only first 26 alphabets are given we can jsut use a constant array of size 26 rather than a map, will be faster,but map approach works good for all kinds of characters
#if k is 26 then space o1 else ok


        