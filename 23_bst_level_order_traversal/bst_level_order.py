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
        #Write your code here
        temp = []
        temp.append(root)
        answer = ""
        
        while temp:
            node = temp[0]
            answer = answer + str(node.data) + " "
            
            if node.left is not None:
                temp.append(node.left)
            if node.right is not None:
                temp.append(node.right)
            temp.pop(0)
        print(answer)
            
        
        
T=int(input())
