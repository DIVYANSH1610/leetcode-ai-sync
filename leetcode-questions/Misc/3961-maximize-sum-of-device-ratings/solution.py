class Solution(object):
    def maxRatings(self, units):
        """
        :type units: List[List[int]]
        :rtype: int
        """
        n = len(units[0])

        # Special case: every device has exactly one unit
        if n == 1:
            return sum(row[0] for row in units)

        smallest_first = float('inf')
        smallest_second = float('inf')
        sum_seconds = 0

        for row in units:
            row.sort()

            smallest_first = min(smallest_first, row[0])
            smallest_second = min(smallest_second, row[1])

            sum_seconds += row[1]

        return sum_seconds - smallest_second + smallest_first