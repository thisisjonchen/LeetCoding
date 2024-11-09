# LC 273. Integer to English Words
class Solution(object):
    def numberToWords(self, num):
        if num == 0: return "Zero"
        # Type out all conditions from 1-Billion (NO ZERO). Make sure to type from 1-19 (11-19 due to unique wording) too.
        d = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand", 100: "Hundred",
             90: "Ninety", 80: "Eighty", 70: "Seventy", 60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty", 20: "Twenty",
             19: "Nineteen", 18: "Eighteen", 17: "Seventeen", 16: "Sixteen", 15: "Fifteen", 14: "Fourteen", 13: "Thirteen", 12: "Twelve", 11: "Eleven",
             10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One"}

        res = ""
        for k, v in d.items():
            if num // k > 0: # Finding range
                x = num // k
                if k >= 100: # If greater than hundred (making tens + ones ineligible), recursively call once again
                    res += self.numberToWords(x) + " " # space to seperate
                res += v + " " # Using Biggest Integer
                num = num % k # Prepare for next loop
        return res.strip()

  '''
  TLDR: Loop through and find the key where within range. If k >=100, recursively call again on num // k. Regardless, add to res with space. For next loop, take num % k. At end, use .strip() to remove any spaces at end.

  TC O(nlog(num))
  SC O(1)
  '''
