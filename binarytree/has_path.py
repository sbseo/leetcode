class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, target):
    if not root: return False
    return dfs(root, target, 0)

def dfs(root, target, curr_sum):
    # Base
    if not root: 
        return True if curr_sum == target else False
    
    # DFS from root to leaf
    curr, curr_sum = root, curr_sum
    curr_sum += curr.val
        
    return dfs(curr.left, target, curr_sum) or dfs(curr.right, target, curr_sum)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()