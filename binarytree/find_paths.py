class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, target):
    if not root: return []
    
    all_paths = list()
    
    return dfs(root, target, 0, [], set())

def dfs(root, target, curr_sum, path, answer):
    # base
    if not root: 
        if curr_sum == target:
            answer.add(tuple(path))
            return True
        return False
    
    # traversal
    curr = root
    dfs(curr.left, target, curr_sum + curr.val, path + [curr.val], answer)
    dfs(curr.right, target, curr_sum + curr.val, path + [curr.val], answer)
    return list(map(list,answer))

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()