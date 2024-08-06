# LC 3016. Minimum Number of Pushes to Type Word II | LC Daily - 8/5/24
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = defaultdict(int)
        for char in word:
            freq[char] += 1

        currCost, count, res = 1, 0, 0
        freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True)) # O(26) Max
        for char, fr in freq.items():
            res += currCost * fr
            count += 1
            if count % 8 == 0:
                currCost += 1

        return res

  '''
  TLDR: At its core, this is a greedy problem. Get freq, then sort them by their freqs. Also use a counter to check when we hit "8" digits and need to rollover,
  like in a phone keypad. This will increase the cost (ex: 1 tap -> 2 taps).

  TC O(n)
  SC O(26) -> O(1)
  '''
