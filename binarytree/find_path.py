class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, path):
  # TODO: Write your code here
  result = dfs(root, [])  
  if path in result:
    return True
  return False

def dfs(curr, path):
  if not curr:
    return []
  
  if curr.left is None and curr.right is None:
    return [path + [curr.val]]

  paths = list()
  paths += dfs(curr.left, path + [curr.val])
  paths += dfs(curr.right, path + [curr.val])

  return paths

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
