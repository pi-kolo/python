import random


# ["1", 
#   ["2", 
#       ["4", 
#           ["8", None, None], ["9",None,None]],
#       ["5",None,None]], 
#   ["3", 
#       ["6", None, None], ["7", None, None]]]


# tree = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], None]]

#nie działa tak jak powinno jescze

def gen_tree(height):
    counter = 2
    left = sub_tree(height, 2)
    right = sub_tree(height, 2)
    return [1, left, right]

def sub_tree(total, curr):
    if total == curr:
        return [curr, None, None]
    choice = random.random()
    if choice > 0.75:
        return [curr, sub_tree(total, curr+1), sub_tree(total, curr+1)]
    elif choice > 0.5:
        return [curr, sub_tree(total, curr+1), None]
    elif choice > 0.25:
        return [curr, None, sub_tree(total, curr+1)]
    else:
        return [curr, None, None]
