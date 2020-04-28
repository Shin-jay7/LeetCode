from __future__ import annotations


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int)\
                    -> List[int]:
        ans, wordsList, wordsLength = [], [], 0
        for word in words:
            if wordsLength + len(word) + len(wordsList) > maxWidth:
                for i in range(maxWidth-wordsLength):
                    wordsList[i % (len(wordsList)-1 or 1)] += " "
                    """
                    You can argue that the string concatenation for the round robin
                    is costly as it's O(m) increasing the worst case by that factor.
                    Instead you could convert to a list and append the blank spaces.
                    """
                ans.append("".join(wordsList))
                wordsList, wordsLength = [], 0
            wordsList += [word]
            wordsLength += len(word)

        return ans + [" ".join(wordsList).ljust(maxWidth)]
        # print(ans + [" ".join(wordsList).ljust(maxWidth)])


test = Solution()
test.fullJustify([
    "This", "is", "an", "example",
    "of", "text", "justification."], 16)
"""
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

test = Solution()
test.fullJustify([
    "What","must","be","acknowledgment","shall","be"], 16)
"""
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""

test = Solution()
test.fullJustify([
    "Science","is","what","we","understand","well","enough",
    "to","explain","to","a","computer.","Art","is",
    "everything","else","we","do"], 20)
"""
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",               ']
  "everything  else  we",
  "do                  "
]
"""
