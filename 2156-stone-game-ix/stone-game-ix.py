class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        mods = [0, 0, 0]

        for val in stones:
            mods[val % 3] += 1
        if mods[0] % 2 == 0:
            return mods[1] > 0 and mods[2] > 0
        return abs(mods[1] - mods[2]) > 2
        