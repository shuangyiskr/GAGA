class Link_Node():
    def __init__(self,data,next_link=None):
        self.data=data
        self.next_link=next_link

class Link_Manipulate():
    def __init__(self):
        self._head=None

    def isEmpty(self):
        return self._head is None

    def length(self):
        node=self._head
        count=0
        while node:
            count+=1
            node=node.next_link
        return count

    def add(self,data):
        node=Link_Node(data)
        node.next_link=self._head
        self._head=node

    def travel(self):
        if self._head:
            cur_node=self._head
            while cur_node:
                print(cur_node.data,end="")
                cur_node=cur_node.next_link
        else:
            raise ("The link is empty!")

    def append(self,data):
        node=Link_Node(data)
        if self._head is None:
            self._head=node
            return
        else:
            cur_node=self._head
            while cur_node:
                pre_node,cur_node=cur_node,cur_node.next_link
            pre_node.next_link=node
    def insert(self,data,index):
        if index<=0:
            self.add(data)
        elif index>=self.length():
            self.append(data)
        else:
            node=Link_Node(data)
            cur_node=self._head.next_link
            pre_node=self._head
            count=1
            while cur_node:
                if count==index:
                    pre.next_link,node.next_link=node,cur_node
                    break
                pre,cur_node=cur_node,cur_node.next_link
                count+=1

    def remove(self,data):
        if self.isEmpty():
          return "Failed because of Empty!"
        cur_node=self._head
        pre_node=None
        while cur_node:
            if cur_node.data==data:
                if pre_node==None:
                    self._head=cur_node.next_link
            else:
                pre_node.next_link=cur_node.next_link
            return data
            pre_node,cur_node=cur_node,cur_node.next_link
        raise("Not found!")
    def search(self,data):
        if self.isEmpty():
            raise("The Link is empty！")
        else:
            cur_node=self._head
            index=0
            while cur_node:
                if cur_node==data:
                    return index
                index+=1
                cur_node=cur_node.next_link
            return -1


Link_Demo=Link_Manipulate()
print(Link_Demo)
Link_Demo.add(1)
Link_Demo.append(2)
Link_Demo.append(3)
Link_Demo.append(4)
Link_Demo.append(5)
print("这个链表结点是否为空：",str(Link_Demo.isEmpty()))
print("这个链表结点长度：",str(Link_Demo.length()))
print("遍历链表：")
Link_Demo.travel()


