from collections import deque
import argparse

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __repr__(self) -> str:
    return f"Node({self.value}, {self.left}, {self.right})"

def dfs(root, target) -> list[Node | None]:
  if not root:
    return []

  if root.value == target:
    return [root.value]

  left_path = dfs(root.left, target - root.value)
  if left_path:
    return [root.value] + left_path

  right_path = dfs(root.right, target - root.value)
  if right_path:
    return [root.value] + right_path

  return []



def input_to_binary_tree(input_list: list) -> Node:
    if len(input_list) == 0:
        return None

    root = Node(input_list[0])
    queue = deque([root])
    i = 1
    while queue:
        current_node = queue.popleft()
        if current_node:
            if i < len(input_list) and input_list[i] is not None:
                current_node.left = Node(input_list[i])
                queue.append(current_node.left)
            i += 1
            if i < len(input_list) and input_list[i] is not None:
                current_node.right = Node(input_list[i])
                queue.append(current_node.right)
            i += 1
    return root

print("Testing dfs")
print(dfs(input_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 26))
print(dfs(input_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))
print(dfs(input_to_binary_tree([1,2,3,4,5,6,7,8,9]), 15))
print("Testing dfs done")

def custom(input_list: list, target: int) -> list:
  root = input_to_binary_tree(input_list)
  return dfs(root, target)


# usage `python dfs.py --input_list 1,2,3,4,,5,,,7 --target 4`
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_list", help="List of integers", type=str)
    parser.add_argument("--target", help="Target sum", type=int)
    args = parser.parse_args()
    input_list = [int(x) if x != "" else None for x in args.input_list.split(",")]
    print(custom(input_list, args.target))

