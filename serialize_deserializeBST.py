# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        seq = []
        stack = [root]
        if not root:
            return []
        while stack:
            node = stack.pop()
            seq.append(node.val)
            if node.right and node.left:  # fork node
                seq.append(-1)
                stack.append(node.right)
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
            elif node.left:
                stack.append(node.left)
            else:  # leaf -> go to last fork node
                seq.append(-2)
        return seq

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        breakPoints = []

        root = last = None

        for d in data:
            if not last:
                root = TreeNode(d)
                last = root
            elif d == -1:
                breakPoints.append(last)
            elif d == -2:
                if breakPoints:  # otherwise it's the end
                    last = breakPoints.pop()
            else:
                newNode = TreeNode(d)
                if last.val < d:
                    last.right = newNode
                else:
                    last.left = newNode
                last = newNode
        return root
