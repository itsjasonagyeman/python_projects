class Solution(object):
    def romanToInt(self, s):
        numeral_conversion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        convert = list(s)
        conv_one = convert[1:]
        alpha = numeral_conversion[convert[0]]
        for char in conv_one: 
            alpha += numeral_conversion[char]
        print(alpha)
    
a = Solution()
print(a.romanToInt('IV'))
    



            
            

        



