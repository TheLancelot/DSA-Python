class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force O(n^2 will give TLE) for every day, check the next days and update the profit

        #optimal O(n) sliding window
        #we keep track of the lowest element in the window, keep calculating and updating max profit
        #if element at i is smaller than the smallest element (the profit will be negative// ith element is the smallest, so we update the smallest element to i)
        max_profit=0
        profit=0
        curr=0
        for i in range(1,len(prices)):
            
            if prices[i]>prices[curr]:
                profit=prices[i]-prices[curr]
            else:
                curr=i

            if profit>max_profit:
                max_profit=profit
            
        return max_profit





        