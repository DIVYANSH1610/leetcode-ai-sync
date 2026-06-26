class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        n = len(s)

        for i in range(n):
            ch = s[i]

            if ch == '*':
                if len(res) != 0:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            elif ch == '%':
                res.reverse()
            else:
                res.append(ch)

        return ''.join(res)