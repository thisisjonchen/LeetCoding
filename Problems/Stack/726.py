# LC 726. Number of Atoms | Daily - 7/14/24 (Gave up)

# Solution from Solutions - Cred: Frederic-Chopin
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = defaultdict(int)   # {element string: occurrences int}
        stack = []                  # stores multipliers for nested parentheses
        multiplier = 1              # actual counts for nested elements
        num = ''                    # num: current number builder
        element = ''                # current element builder

        for i in range(len(formula) - 1, -1, -1):      # right to left
            c = formula[i]
            if c.isdigit():             # build the number
                num = c + num 
            elif c.isalpha():
                element = c + element
                if c.isupper():         # element name completed
                    counts[element] += multiplier * (int(num) if num else 1)
                    element, num = '', ''
            elif c == ')':
                multiplier *= int(num) if num else 1
                stack.append(int(num) if num else 1)       
                num = ''
            else:   # '('
                multiplier //= stack.pop()      # revert to the previous multiplier
        
        # Construct the result string
        result = []
        for key in sorted(counts.keys()):
            result.append(key)
            if counts[key] > 1:
                result.append(str(counts[key]))
        return ''.join(result)
'''
TLDR: Use stack approach with multiplier. There are "four" cases: digit, char (both upper and lower, nested if checks for upper for complete element), closing paran, opening paran. The algorithm runs
the formula from back to front. At the end, the atom counts would be sorted and returned. Since the number of resulting atoms are < N, the final time complexity remains O(n).
'''
