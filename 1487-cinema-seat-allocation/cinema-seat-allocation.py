import collections
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = collections.defaultdict(int)

        for row, seat in reservedSeats:
            if 2 <= seat <= 3:
                row_masks[row] |= 1
            elif 4 <= seat <= 5:
                row_masks[row] |= 2
            elif 6 <= seat <= 7:
                row_masks[row] |= 4
            elif 8 <= seat <= 9:
                row_masks[row] |= 8
        total_groups = 2 * n

        for mask  in row_masks.values():
            total_groups -= 2

            if (mask & 3) == 0 and (mask & 12) == 0:
                total_groups += 2

            elif (mask & 3) == 0:
                total_groups += 1
            elif (mask & 12) == 0:
                total_groups += 1
            elif (mask & 6) == 0:
                total_groups += 1
        return total_groups

        