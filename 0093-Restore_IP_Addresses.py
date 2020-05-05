from __future__ import annotations


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, 0, "", ans)

        return ans
        # print(ans)

    def dfs(self, s, idx, path, ans):
        if idx == 4:
            if not s:
                ans.append(path[:-1])
                # If we don't do this, the last ip part would end with a dot
            return

        for i in range(1,4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], idx+1, path+s[:i]+".", ans)
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], idx+1, path+s[:i]+".", ans)
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], idx+1, path+s[:i]+".", ans)


test = Solution()
test.restoreIpAddresses("25525511135") # ["255.255.11.135", "255.255.111.35"]
