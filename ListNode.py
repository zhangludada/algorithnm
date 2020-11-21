#定义列表
class Node:
    def __init__(self,v):
        self.val=v
        self.next=None

#列表转链表
def ls_node(ls):
    head=Node(None)
    p=head  #p为链表指针
    for i in ls:
        p.next=Node(i)
        p=p.next
    return head.next

#链表转列表
def node_ls(head):
    ls=[]
    while True:
        ls.append(head.val)
        head=head.next
        if head==None:
            return ls

