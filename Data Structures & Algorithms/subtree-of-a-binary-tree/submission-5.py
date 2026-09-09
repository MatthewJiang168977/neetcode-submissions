# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: 
            return True 
    
        def sameTree(p, q): 
            if not p and not q: 
                return True 
            if (not p and q) or (p and not q): 
                return False 
            if p.val != q.val:
                return False 
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)
            return left and right 

        def dfs(curr): 
            if not curr: 
                return False 
            elif sameTree(curr, subRoot): 
                return True 
            return dfs(curr.left) or dfs(curr.right)
        return dfs(root)