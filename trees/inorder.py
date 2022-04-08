# def inorder(root):
#     if not root:
#         return
#     curr = root
#     done = False
#     list = []
#     traversal_list = []
#
#     while not done:
#         if curr:
#             list.append(curr)
#             curr = curr.left
#         else:
#             if not list:
#                 done = True
#             else:
#                 curr = list.pop()
#                 traversal_list.append(curr)
#                 curr = curr.right
#     return traversal_list


left = 1
right = 2
result = 1 + (left if left > right else right)
print(result)
