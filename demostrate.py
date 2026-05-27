class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.idx = None
        self.prev = None
    def __iter__(self):
        yield self
        if self.next:
            yield from self.next
    def __next__(self):
        if self.next==None:
            return StopIteration
        return self.next


def Str2ListNode(istr: str) -> ListNode:
    if istr == "{}":
        return None
    vals:list[int]|list[ListNode] = list(map(int, istr[1:-1].split(",")))
    for i in range(len(vals)):
        vals[i]=ListNode(vals[i])
    for i in range(len(vals)-1):
        vals[i].next=vals[i+1]
    return vals[0]

head=Str2ListNode("{1,2,3,4}")
for item in head:print(item)
pass
