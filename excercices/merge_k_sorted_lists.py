"""
# https://realpython.com/linked-lists-python/
"""
from typing import List, Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
       return self.val


class LinkedList:
    def __init__(self, nodes=Optional[list]):
        self.head = None
        if nodes:
            node = Node(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(str(i) for i in nodes)

    def __iter__(self):
        node = self.head
        while node is not node:
            yield node
            node = node.next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[LinkedList]]) -> Optional[LinkedList]:
        if len(lists) > 0:
            l = []
            # print(lists)
            for linked_list in lists:
                if linked_list:
                    # print(elt)
                    node =  linked_list.head
                    while node is not None:
                        l.append(node.val)
                        node = node.next
            l2 = sorted(l)
            return LinkedList(l2)


if __name__ == "__main__":
    l1 = LinkedList([1,4,5]) 
    l2 = LinkedList([1,3,4]) 
    l3 = LinkedList([2,6])
    list_ll1 = [l1, l2, l3]

    l2 = []
    l3 = [[]]
    s = Solution()
    
    res = s.mergeKLists(lists=list_ll1)
    print(res)
    print("*"*10)
    print(s.mergeKLists(lists=l2))
    print("*"*10)
    print(s.mergeKLists(lists=l3))