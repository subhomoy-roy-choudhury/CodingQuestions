class  LinkedList(object):
    """docstring for  LinkedList."""

    def __init__(self,value):
        super( LinkedList, self).__init__()
        self.head = {
            "value" :value,
            next: None
        }
        self.tail = self.head
        self.length = 1

    def printList(self):
        arr = []
        temp = self.head
        while(temp!=None):
            arr.append(temp["value"])
            temp = temp[next]
        return arr

    def append(self,value):
        newNode = {
            "value" : value,
            next : None
        }
        ptr = self.tail
        ptr[next] = newNode
        self.tail = newNode
        self.length +=1
        return self.printList()

    def prepend(self,value):
        newNode = {
            "value" : value,
            next : None
        }
        ptr = self.head
        newNode[next] = ptr
        self.head = newNode
        self.length+=1
        return self.printList()

    def insert(self,pos,value):
        if pos > self.length :
            self.append(value)
            return self.printList()
        newNode = {
            "value" : value,
            next : None
        }
        ptr = self.head
        idx = 0
        while(ptr[next] != None):
            if (idx == pos-1):
                temp = ptr[next]
                ptr[next] = newNode
                newNode[next] = temp
                ptr = newNode
            ptr = ptr[next]
            idx+=1
        return self.printList();

    def remove(self,pos):
        ptr = self.head
        idx = 0
        while(ptr[next]!= None):
            if (idx == pos-1):
                temp = ptr[next]
                ptr[next] = temp[next]
            ptr = ptr[next]
            idx +=1
        return self.printList();

    def reverse(self):
        prev = None
        current = self.head
        while(current!=None):
            temp = current[next]
            current[next] = prev
            prev = current
            current = temp
        self.head = prev
        return self.printList();

    def sort(self):
        current = self.head
        idx = None
        while current!=None :
            idx = current[next]
            while idx!= None :
                if current['value'] > idx['value']:
                    tmp=current['value']
                    current['value']=idx['value']
                    idx['value']=tmp
                idx = idx[next]
            current = current[next]
        return self.printList();

if __name__ == '__main__':

    linked_list = LinkedList(12)
    print(linked_list.append(10))
    print(linked_list.append(15))
    print(linked_list.prepend(1))
    print(linked_list.prepend(0))
    print(linked_list.insert(3,20))
    print(linked_list.remove(3))
    print(linked_list.reverse())
    print(linked_list.sort())
