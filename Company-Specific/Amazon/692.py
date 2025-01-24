# LC 692. Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for w in words:
            freq[w] += 1

        freq = sorted(freq.items(), key=lambda x: (-x[1], x[0])) # sort freq in descending order (with negative, largest freq is first) and THEN by alphabetical

        res = []
        for wp in range(k):
            w, f = freq[wp]
            res.append(w)
        return res

'''
TLDR: Gather freq of each word, sort by freq first in descending order, then by the alphabetical order (lexicographical)

TC O(klogn)
SC O(n)
'''
