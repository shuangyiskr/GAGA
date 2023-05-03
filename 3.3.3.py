#实现一个二叉树
class BinaryTreeNode(object):
    def __init__(self):
        self.data='#'
        self.leftChild=None
        self.rightChild=None

class BinaryTree(object):
    def createBinaryTree(self,Root):
        data=input("==>")
        if data=='#':
            Root=None
        else:
            Root.data=data
            Root.leftChild=BinaryTreeNode()
            self.createBinaryTree(Root.leftChild)
            Root.rightChild=BinaryTreeNode()
            self.createBinaryTree(Root.rightChild)

    def preOrder(self,Root):
        if Root is not None:
            self.visitBinaryTreeNode(Root)
            self.preOrder(Root.leftChild)
            self.preOrder(Root.rightChild)

    def inOrder(self, Root):
        if Root is not None:
            self.preOrder(Root.leftChild)
            self.visitBinaryTreeNode(Root)
            self.preOrder(Root.rightChild)

    def postOrder(self, Root):
        if Root is not None:
            self.preOrder(Root.leftChild)
            self.preOrder(Root.rightChild)
            self.visitBinaryTreeNode(Root)

    def visitBinaryTreeNode(self,BinaryTreeNode):
        if BinaryTreeNode.data !='#':
            print(BinaryTreeNode.data,end="->")

if __name__=='__main__':
    bTN=BinaryTreeNode()
    bT=BinaryTree()
    bT.createBinaryTree(bTN)
    print("先序遍历的输出结果为：")
    bT.preOrder(bTN)
    print("\n中序遍历的输出结果为：")
    bT.inOrder(bTN)
    print("\n后序遍历的输出结果为：")
    bT.postOrder(bTN)
