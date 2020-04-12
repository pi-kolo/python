import random

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def __str__(self):
        return str(self.value)
   
    
def generate_tree(height, n_ary):
    value = random.randint(0, 100)
    
    if height == 1:
        return Node(value, None)
    
    main_branch = random.randint(0, n_ary)

    return Node(
        value,
        [generate_tree(height-1, n_ary) if i == main_branch else generate_tree(random.randint(1, height-1), n_ary) for i in range(n_ary)]
    )


def dfs(t):
    yield t.value
    if t.children != None:
        for subtree in t.children:
            yield from dfs(subtree)


def bfs(t):
        queue = [t]
        while len(queue) > 0:
            node = queue.pop(0)
            yield node.value
            if node.children != None:
                for child in node.children:
                    queue.append(child)

tree = generate_tree(5,3)