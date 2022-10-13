


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
        
def insert(root,val):
    newnode = Node(val)
    temp = root
    parent = None
    while temp != None:
        parent = temp
        if temp.data > val:
            temp = temp.left
        else:
            temp = temp.right
    if parent is None:
        root = newnode
    elif parent.data > val:
        parent.left = newnode
    else :
        parent.right = newnode
    return root    
def calcInorder(node):
 
    if node:
 
        # Recurring on left child
        calcInorder(node.left)
 
        # Printing data of node
        print(node.data, end=" "),
 
        # Recurring on right child
        calcInorder(node.right)       
        
root = Node(10)
root = insert(root, 5)
root= insert(root, 15)
root = insert(root, 3)
root= insert(root, 7)
                       
calcInorder(root)