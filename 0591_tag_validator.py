from __future__ import annotations
import re


class Solution:
    def isValid(self, code: str) -> bool:
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'


class Solution:
    def isValid(self, code: str) -> bool:
        # state_machine = ["plain", "open", "close", "cdata"]
        curr = "plain"
        stack, open_tag, close_tag = [], [], []
        idx = 0

        while idx < len(code):
            char = code[idx]
            if curr == "plain":
                if not stack and idx != 0:
                    # code is not in a closed tage
                    return False
                if code[idx:idx+9] == "<![CDATA[":
                    curr = "cdata"
                    idx += 9
                    continue
                elif code[idx:idx+2] == '</':
                    curr = 'close'
                    idx += 2
                    continue
                elif char == '<':
                    curr = "open"
            elif curr == "open":
                if char == '>':
                    if len(open_tag) > 9 or len(open_tag) < 1:
                        # open tag name length not valid
                        return False
                    stack.append("".join(open_tag))
                    open_tag = []
                    curr = 'plain'
                    idx += 1
                    continue
                if not char.isupper():
                    # open tag is not upper
                    return False
                open_tag.append(char)
            elif curr == 'close':
                if char == '>':
                    if len(close_tag) > 9 or len(close_tag) < 1:
                        # close tag name length not valid
                        return False
                    close_tag_str = "".join(close_tag)
                    if not stack or close_tag_str != stack[-1]:
                        # tag no match
                        return False
                    else:
                        stack.pop()
                    close_tag = []
                    curr = 'plain'
                    idx += 1
                    continue
                if not char.isupper():
                    # close tag is not upper
                    return False
                close_tag.append(char)
            elif curr == "cdata":
                if code[idx:idx+3] == ']]>':
                    idx += 3
                    curr = "plain"
                    continue
            idx += 1
        if stack or curr != "plain":
            return False
        return True


test = Solution()
test.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")  # True

# test = Solution()
# test.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")  # True

# test = Solution()
# test.isValid("<A>  <B> </A>   </B>")  # False
