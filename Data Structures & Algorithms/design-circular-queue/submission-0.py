class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        # front
        self.left = ListNode(0,None,None)
        # rear
        self.right = ListNode(0,None,self.left)
        self.left.next = self.right


    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        # enqueue in rear
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        # dequeue in front
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space +=1 
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        else: return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        else: return self.right.prev.val
        
    def isEmpty(self) -> bool:
        if self.left.next == self.right: return True
        else: return False

    def isFull(self) -> bool:
        if self.space==0: return True
        else: return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()