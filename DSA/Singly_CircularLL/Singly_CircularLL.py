class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCL:
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0

    def InsertFirst(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = self.last = newn
        else:
            newn.next = self.first
            self.first = newn

        self.last.next = self.first
        self.iCount += 1

    def InsertLast(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = self.last = newn
        else:
            self.last.next = newn
            self.last = newn

        self.last.next = self.first
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

        if self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.last.next = self.first

        self.iCount -= 1

    def DeleteLast(self):
        if self.first is None:
            return

        if self.first == self.last:
            self.first = self.last = None
        else:
            temp = self.first
            while temp.next != self.last:
                temp = temp.next

            temp.next = self.first
            self.last = temp

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
        if self.first is None:
            return

        temp = self.first
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.first:
                break
        print("(circular)")

    def Count(self):
        return self.iCount
    

def main():
    obj = SinglyCL()

    obj.InsertFirst(30)
    obj.InsertFirst(20)
    obj.InsertFirst(10)
    obj.InsertLast(40)

    obj.Display()

    obj.DeleteFirst()
    obj.Display()

    obj.DeleteLast()
    obj.Display()

    obj.InsertAtPos(25, 2)
    obj.Display()


if __name__ == "__main__":
    main()