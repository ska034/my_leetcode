# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        print(sentence)
        length_prefix = len(searchWord)
        length_sentence = len(sentence)

        for i in range(length_sentence):
            if len(sentence[i]) >= length_prefix:
                if sentence[i][0:length_prefix] == searchWord:
                    return i + 1
        return -1
