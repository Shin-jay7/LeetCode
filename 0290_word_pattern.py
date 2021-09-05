from __future__ import annotations


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sign_word_dic, word_sign_dic, words = {}, {}, s.split()

        if len(pattern) != len(words):
            return False

        for sign, word in zip(pattern, words):
            if sign not in sign_word_dic:
                if word in word_sign_dic:
                    return False
                else:
                    sign_word_dic[sign] = word
                    word_sign_dic[word] = sign
            elif sign_word_dic[sign] != word:
                return False

        return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = pattern
        s = s.split()

        return len(set(zip(p, s))) == len(set(p)) == len(set(s)) and len(p) == len(s)
