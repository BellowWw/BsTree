class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def ins_node(data,node)->Node:
    if node is None:
        return Node(data)
    if data>node.data:
        node.right=ins_node(data,node.right)
    elif data<node.data:
        node.left=ins_node(data,node.left)
    return node
def search(root,data):
    if root is None or data==root.data:
        return root
    if data<root.data:
        return search(root.left,data)
    return search(root.right,data)




if __name__ == '__main__':
    print('PyCharm')
    arr=[10,4,6,7,8,13,14,1,3]
    srch_val=90
    root=None
    root=ins_node(arr[0],root)
    for i in range(1,len(arr)):
        ins_node(i,root)
    if search(root,srch_val) is None:
        print(srch_val, "Not Found")
    else:
        print(srch_val, "Found")

