class Solution:
    def maxBuilding(self, n, r):
        if not r:
            return n - 1

        r.sort()

        id_, h = 1, 0

        for i in range(len(r)):
            x, y = r[i]
            r[i][1] = min(y, x - id_ + h)
            id_, h = x, r[i][1]

        for i in range(len(r) - 2, -1, -1):
            r[i][1] = min(r[i][1], r[i+1][1] + r[i+1][0] - r[i][0])

        ans = n - r[-1][0] + r[-1][1]
        id_, h = 1, 0

        for x, y in r:
            steps = x - id_ - abs(y - h)
            higher = max(y, h)
            ans = max(ans, higher + steps // 2)
            id_, h = x, y

        return ans