class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        limit = MAX_INT // 10

        while x != 0:
            digit = x % 10
            x //= 10

            if rev > limit or (rev == limit and digit > 7):
                return 0
            rev = rev * 10 + digit
        return sign * rev

        