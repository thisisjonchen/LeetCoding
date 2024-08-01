# LC 2678. Number of Senior Citizens
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for citizen in details:
            if int(citizen[11:13]) > 60:
                seniors += 1
        return seniors

'''
TLDR: Index 11 + 12 are always the age. If they are > 60, they are a senior.
'''
