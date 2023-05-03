#双链表
class Double_link_Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Double_Link(object):
    def __init__(self):
        self._head=None

    def isEmpty(self):
        return self._head==None

    def length(self):
        cur_data=self._head
        count=0
        while cur_data!=None:
            count+=1
            cur_data=cur_data.next
        return count

    def travel(self):
        cur_data=self._head
        while cur_data!=None:
            print(cur_data.data,end="")
            cur_data=cur_data.next
        print("遍历完毕")

    def add(self,data):
        Dnode=Double_link_Node(data)
        if self.isEmpty():
            self._head=Dnode
        else:
            Dnode.next=self._head
            self._head.prev=Dnode
            self._head=Dnode

    def append(self,data):
        Dnode=Double_link_Node(data)
        if self.isEmpty():
            self._head=Dnode
        else:
            cur_data=self._head
            while cur_data.next!=None:
                cur_data=cur_data.next
            cur_data.next=Dnode
            Dnode.prev=cur_data

    def search(self,data):
        cur_data=self._head
        while cur_data!=None:
            if cur_data.data==data:
                return True
            cur_data=cur_data.next
        return False

    def insert(self,data,index):
        if index<=0:
            self.add(data)
        elif index>(self.length()-1):
            self.append(data)
        else:
            Dnode=Double_link_Node(data)
            cur_data=self._head
            count=0
            while count<(index-1):
                count+=1
                cur_data=cur_data.next
            Dnode.prev=cur_data
            Dnode.next=cur_data.next
            cur_data.next.prev=Dnode
            cur_data.next=Dnode

    def remove(self,data):
        if self.isEmpty():
            return
        else:
            cur_data=self._head
            if cur_data.data==data:
                if cur_data.next==None:
                    self._head=None
                else:
                    cur_data.next.prev=None
                    self._head=cur_data.next
                return
            while cur_data!=data:
                if cur_data.data==data:
                    cur_data.prev.next=cur_data.next
                    cur_data.next.prev=cur_data.prev
                    break
                cur_data=cur_data.next

Double_Link_Demo=Double_Link()
Double_Link_Demo.add(1)
Double_Link_Demo.append(2)
Double_Link_Demo.append(3)
Double_Link_Demo.append(4)
Double_Link_Demo.append(5)
print("链表节点是否为空：",str(Double_Link_Demo.isEmpty()))
print("链表节点长度为：",str(Double_Link_Demo.length()))
print("遍历链表：")
Double_Link_Demo.travel()

Double_Link_Demo.insert(6,2)
print("遍历链表：")
Double_Link_Demo.travel()

Double_Link_Demo.remove(6)
print("遍历链表：")
Double_Link_Demo.travel()