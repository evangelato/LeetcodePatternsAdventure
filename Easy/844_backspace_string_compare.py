class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_type = []
        for c in s:
            if c == "#":
                if len(s_type) > 0:
                    s_type.pop()
            else:
                s_type.append(c)

        t_type = []
        for c in t:
            if c == "#":
                if len(t_type) > 0:
                    t_type.pop()
            else:
                t_type.append(c)

        return s_type == t_type
