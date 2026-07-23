# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # breadth first search way first:
        #Base case
        if not root:
            return None

        # we use a deque as our data sttrucutr to pop from the left side of  FIFO data strcuiture
        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right,node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root
        

            


        