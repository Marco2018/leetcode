from collections import Counter

class Solution(object):
    def maxScoreWords(self, words, letters, score):

        def dfs(i, curr_score, letter_counter):
            if curr_score + sum(words_score[i:]) <= self.max_score:
                return
            self.max_score = max(self.max_score, curr_score)
            for j, wordcounter in enumerate(words_counter[i:], i):
                if all(n <= letter_counter.get(c, 0) for c, n in wordcounter.items()):
                    new_counter = {}
                    for c, n in letter_counter.items():
                        new_counter[c] = n - wordcounter.get(c, 0)
                    dfs(j + 1, curr_score + words_score[j], new_counter)

        self.max_score = 0
        words_score = [sum(score[ord(c) - ord('a')] for c in word) for word in words]
        words_counter = [Counter(word) for word in words]

        dfs(0, 0, Counter(letters))
        return self.max_score