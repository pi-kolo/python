import random
import math

# ["1", 
#   ["2", 
#       ["4", 
#           ["8", None, None], ["9",None,None]],
#       ["5",None,None]], 
#   ["3", 
#       ["6", None, None], ["7", None, None]]]


# tree = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], None]]


def generate_tree(height):
    if height == 0:
        return None

    value = random.randint(0, 100)
    main_height = generate_tree(height-1)   #guarantees proper height of tree
    sub_branches = generate_tree(random.randint(0, height-1))

    LEFT, RIGHT = 0, 1
    direction = random.choice([LEFT, RIGHT])

    if direction == LEFT:
        return [value, main_height, sub_branches]
    else:
        return [value, sub_branches, main_height]


def bfs(tree):
    queue = [tree]
    while len(queue) > 0:
        node = queue.pop(0)
        yield node[0]
        if node[1] != None:
            queue.append(node[1])
        if node[2] != None:
            queue.append(node[2])


def dfs(tree):
    if tree == None:
        return
    yield tree[0]
    yield from dfs(tree[1])
    yield from dfs(tree[2])

