class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
            
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        
        dp = [[0] * n for _ in range(n)]
        
        
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        
        mid = [i - 1 for i in range(n)]
        
        
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                
                m = mid[i]
                if m < i - 1:
                    m = i - 1
                
                
                while m + 1 < j and (prefix[m + 2] - prefix[i]) * 2 <= prefix[j + 1] - prefix[i]:
                    m += 1
                    
                mid[i] = m 
                res = 0
                
                
                if m >= i:
                    left_sum = prefix[m + 1] - prefix[i]
                    total_sum = prefix[j + 1] - prefix[i]
                    
                    if left_sum * 2 == total_sum:
                        
                        if m - 1 >= i:
                            res = max(res, max_l[i][m - 1])
                        
                        res = max(res, left_sum + max(dp[i][m], dp[m + 1][j]))
                    else:
                        
                        res = max(res, max_l[i][m])
                        
              
                if m + 1 < j:
                    
                    res = max(res, max_r[m + 2][j])
                    
                dp[i][j] = res
                
                
                sum_ij = prefix[j + 1] - prefix[i]
                max_l[i][j] = max(max_l[i][j - 1], res + sum_ij)
                max_r[i][j] = max(max_r[i + 1][j], res + sum_ij)
                
        return dp[0][n - 1]