class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.all_path: List[int] = []
        cur_path = []
        self.find_all_path(root, cur_path)
        self.ans = []
        for path in self.all_path:
            self.ans.append("->".join(str(num) for num in path))

        return self.ans

    def find_all_path(self, node, cur_path):
        cur_path.append(node.val)
        if not node.left and not node.right:
            self.all_path.append(cur_path[:])

        if node.left:
            self.find_all_path(node.left, cur_path)

        if node.right:
            self.find_all_path(node.right, cur_path)

        cur_path.pop()
