import math

# Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0

    # 4,5,6 digit nos - 1
    # 7 digit nos - 2
    # count digits floor log10 n + 1, if multple of 3 then quotient -1 many commas else quotient
    #brute force is absolute shit, TLE, 457/1100 passed


    # counter=0
    # for i in range(1000,n+1):
    #     digit_count = int(math.log10(i))+ 1
    #     comma_count=(digit_count//3)-1 if digit_count%3==0 else digit_count//3
    #     counter+= comma_count
    
    # return counter


    # n=2514827
    # (2 commas) 7 digits
    # round to 1,000,000

    # count of numbers between 1000000 and 2514827 * 2
    # then k/10, count numbers between k/10 and k/100*1 and so on types

    #now gotta just think based on 7 digits, do num commas*no of numbers types
    #Count the numbers in each comma group (1-3 digits, 4-6 digits, 7-9 digits, ...) and multiply by how many commas each number in that group has, below implementation might still be a bit redundant but it works

        counter=0
        init_nums=n-pow(10, int(math.log10(n)))+1 #count of numbers from n to closest lower power of 10

        init_digit_count = len(str(abs(n))) #now the below logic for digit count worked for 1109/1110 test cases, just one extreme edge case failed where the number was 15 9's, the int(math.log(n)) gave answer as 15 instead of 14 (rounding down 14.9999999999999) and + 1 then ended up giving 16 instead of the correct 15 and then all went wrong, this is due to the  floating-point precision limitations The Exact Value: Mathematically, \(\log_{10}(999,999,999,999,998) \approx 14.99999999999999913\dots\)Floating-Point Rounding: A standard 64-bit float only handles about 15 to 17 significant decimal digits of precision. Because your number is extremely close to \(10^{15}\) (\(1,000,000,000,000,000\)), the float math library rounds the result up to exactly 15.0.

        # init_digit_count = int(math.log10(n))+ 1 #count number of digits in n

        first_comma_count=(init_digit_count//3)-1 if init_digit_count%3==0 else init_digit_count//3 #count number of commas in n by using the above logic to count groups of 3s

        init_count=(init_nums*first_comma_count) #total number of commas from n to closes power of 10 because each number will have same amt of commas

        counter+=init_count

        for i in range(int(math.log10(n)),3,-1):
            comma_count=(i//3)-1 if i%3==0 else i//3 #calcuate comma for any number with i many digits

            commas=(pow(10,i)-pow(10,i-1))*comma_count #multiply it with number of numbers in that range
            counter+=commas
        return counter



Soln = Solution()
print(Soln.countCommas(1547299999999))





        