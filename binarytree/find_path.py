class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
    return dfs(root, sequence, 0)    
  
def dfs(curr, sequence, idx):
        
    if not curr: 
        return False    
    
    if sequence[idx] != curr.val:
        return False
    
    if curr.left is None and curr.right is None:
        return True
    
    return dfs(curr.left, sequence, idx+1) or dfs(curr.right, sequence, idx+1)         

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  root.right.right.right = TreeNode(7)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()