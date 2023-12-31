import sys
class Node:
def __init__(self,data):
self.right=self.left=None
self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self,root):
        if root is None:
        return
        q=[]
        q.append(root)
        while(len(q)!=0):
            if node is None:
                continue
            print(node.data,end=" ")
            q.append(node.left)
            q.append(node.right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
