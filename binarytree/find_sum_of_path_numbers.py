class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  # TODO: Write your code here
  return dfs(root, [], [])

def dfs(root, path, result):
    
    if not root.left and not root.right:
        return [path + [root.val]]
    elif root.left and not root.right:
        result += dfs(root.left, path + [root.val], result)
    elif not root.left and root.right:
        result += dfs(root.right, path + [root.val], result)
    elif root.left and root.right:
        result += dfs(root.left, path + [root.val], result)
        result += dfs(root.right, path + [root.val], result)
    
    result = list(set(map(tuple, result)))
    result = list(map(list, result))
    
    return result

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
