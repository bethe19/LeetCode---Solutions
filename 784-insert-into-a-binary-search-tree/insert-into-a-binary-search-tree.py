# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(key)
        move = root
        tail = None
        while move:
            tail = move
            if move.val == key:
                return
            elif key > move.val:
                move = move.right
            else:
                move = move.left

        if tail.val < key: tail.right = TreeNode(key)
        else: tail.left = TreeNode(key)

        return root