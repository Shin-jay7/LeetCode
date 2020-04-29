from __future__ import annotations


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)

        return "/" + "/".join(stack)
        # print("/" + "/".join(stack))


test = Solution()
test.simplifyPath("/home/") # "/home"

test = Solution()
test.simplifyPath("/../") # "/"

test = Solution()
test.simplifyPath("/home//foo/") # "/home/foo"

test = Solution()
test.simplifyPath("/a/./b/../../c/") # "/c"

test = Solution()
test.simplifyPath("/a/../../b/../c//.//") # "/c"

test = Solution()
test.simplifyPath("/a//b////c/d//././/..") # "/a/b/c"
