# Remove Letter To Equalize Frequency #2423

# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

# Note:

# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        for c in cnt.keys():
            cnt[c] -= 1
            if len(set(v for v in cnt.values() if v)) == 1:
                return True
            cnt[c] += 1
        return False