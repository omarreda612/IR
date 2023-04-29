# from binarytree import build, Node

# # Construct the binary tree from a list of integers
# values = [10, 5, 15, 3, 7, 13, 18]
# root = build(values)

# # Print the binary tree
# print("Binary Tree:")
# print(root)

# # Ask the user to choose an operation
# while True:
#     print("What would you like to do?")
#     print("1. Add a new element to the binary tree")
#     print("2. Delete an element from the binary tree")
#     choice = int(input("Enter your choice (1 or 2): "))

#     if choice == 1:
#         # Ask the user for the value to add to the tree
#         value = int(input("Enter the value to add to the binary tree: "))

#         # Create a new node with the value and insert it into the tree
#         new_node = Node(value)
#         root.insert= (new_node)

#         # Print the updated binary tree
#         print("Updated Binary Tree:")
#         print(root)

#     elif choice == 2:
#         # Ask the user for the value to delete from the tree
#         value = int(input("Enter the value to delete from the binary tree: "))

#         # Find the node with the value and delete it from the tree
#         node_to_delete = root.search(value)
#         root.delete(node_to_delete)

#         # Print the updated binary tree
#         print("Updated Binary Tree:")
#         print(root)


#     else:
#         print("Invalid choice. Please enter 1 or 2")
from binarytree import build, Node

# Build the binary tree from a list of integers
integers = [7, 3, 9, 1, 5, 8, 10]
root = build(integers)

# Define a function to add a new element to the binary tree
def add_element(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = add_element(node.left, value)
    elif value > node.value:
        node.right = add_element(node.right, value)
    return node

# Define a function to delete an element from the binary tree
def delete_element(node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = delete_element(node.left, value)
    elif value > node.value:
        node.right = delete_element(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.value = temp.value
            node.right = delete_element(node.right, temp.value)
    return node

# Main loop
while True:
    print('tree',root)
    print("Select an option:")
    print("1 -Add an element")
    print("2 -Delete an element")
    print('3 -quit')
    choice = input("Enter your choice: ")
    if choice == '1':
        value = int(input("Enter the value to add: "))
        root = add_element(root, value)
        print('updated tree', root)
    elif choice == '2':
        value = int(input("Enter the value to delete: "))
        root = delete_element(root, value)
        print('updated tree', root)
    elif choice =='3':
        break    
    else:
        print("Invalid choice, please try again.")