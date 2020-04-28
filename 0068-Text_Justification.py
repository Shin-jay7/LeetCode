from __future__ import annotations


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int)\
                    -> List[int]:
        line = ""
        lines = []

        for word in words:
            if len(line)+len(word) > maxWidth:
                lines.append(line.strip())
                line = ""
            line += word + " "

        if line:
            lines.append(line.strip())

        ans = []
        for idx,line in enumerate(lines):
            if idx == len(lines)-1 or " " not in line:
                ans.append(line.ljust(maxWidth))
            else:
                diff = maxWidth-len(line)
                add, left = divmod(diff, line.count(" "))
                i = j = 0
                for char in line:
                    if char == " ":
                        line = line[:i+1] + " "*add + line[i+1:]
                        i += add
                        if left:
                            line = line[:j+1] + " " + line[j+1:]
                            left -= 1
                            j += 1
                    i += 1
                    j += 1

                ans.append(line)

        return ans
        # print(ans)


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
