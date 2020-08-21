class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, target):
  # TODO: Write your code here
  return dfs(root, target, [])

def dfs(curr, target, path):
  if not curr:
    return 0

  # leafnode
  if curr.left is None and curr.right is None:
    if equals_target(path+[curr.val], target): 
      return 1
    return 0

  count = 0
  count += dfs(curr.left, target, path+[curr.val])
  count += dfs(curr.right, target, path+[curr.val])
  
  return count

def equals_target(path, target):
  for idx in range(len(path)):
    if sum(path[idx:]) == target:
      return True
  return False

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
