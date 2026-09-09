# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_counter = k
        self.res = 0
        def dfs(curr): 
            if not curr: 
                return 
            left = dfs(curr.left)
            self.k_counter -= 1 
            if self.k_counter == 0: 
                self.res = curr.val
                return
            
            right= dfs(curr.right)  
            
        dfs(root)
        return self.res
        [2, 3, 4, 5]