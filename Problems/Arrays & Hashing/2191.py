# LC 2191. Sort the Jumbled Numbers | Daily LC - 7/24/24
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        unjumble = dict()
        for i in range(len(mapping)):
            unjumble[str(i)] = str(mapping[i])
        
        unjumbledNumToOG = defaultdict(list)
        for num in nums:
            num = str(num)
            curr = ""
            for i in range(len(num)):
                curr += unjumble[num[i]]
            unjumbledNumToOG[int(curr)] += [int(num)]

        res = []
        for unjumbled, jumbled in sorted(unjumbledNumToOG.items()):
            res += jumbled

        return res

  '''
  TLDR: Create two dicts, one for unjumbling the mappings and one remapping the unjumbled to the jumbled. Sort by the unjumbled and return res.
  '''
