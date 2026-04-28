class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self, no):
        newn = Node(no)

        newn.next = self.first
        self.first = newn

        self.iCount += 1

    def InsertLast(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = newn
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = newn

        self.iCount += 1

    def InsertAtPos(self, no, pos):
        if pos < 1 or pos > self.iCount + 1:
            return

        if pos == 1:
            self.InsertFirst(no)
        elif pos == self.iCount + 1:
            self.InsertLast(no)
        else:
            newn = Node(no)
            temp = self.first

            for i in range(1, pos - 1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn
            self.iCount += 1

    def DeleteFirst(self):
        if self.first is None:
            return

        self.first = self.first.next
        self.iCount -= 1

    def DeleteLast(self):
        if self.first is None:
            return

        if self.first.next is None:
            self.first = None
        else:
            temp = self.first
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

        self.iCount -= 1

    def DeleteAtPos(self, pos):
        if pos < 1 or pos > self.iCount:
            return

        if pos == 1:
            self.DeleteFirst()
        elif pos == self.iCount:
            self.DeleteLast()
        else:
            temp = self.first
            for i in range(1, pos - 1):
                temp = temp.next

            temp.next = temp.next.next
            self.iCount -= 1

    def Display(self):
        temp = self.first
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    def Count(self):
        return self.iCount
    

    def main():
        pass

if __name__ == "__main":
    main()        