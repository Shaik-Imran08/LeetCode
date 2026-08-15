# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subtree_sums = []

        def get_sum(node):
            if not node:
                return 0
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            subtree_sums.append(current_sum)

            return current_sum

        total_sum = get_sum(root)

        max_product = 0

        for sub_sum in subtree_sums:
            product = sub_sum * (total_sum - sub_sum)
            if product > max_product:
                max_product = product
        return max_product % MOD
