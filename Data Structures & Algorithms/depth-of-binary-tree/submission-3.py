# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # perform bfs, check root, put left and right in queue add one
        if not root:
            return 0
        
        count = 0
        queue = deque([root])
        level_size = len(queue)

        while queue:
            for i in range(level_size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            level_size = len(queue)
            count += 1

        return count

        
