class Head:
    def __init__(self,data, next):
        self.data = data
        self.next = next

    class Linked_list:
        def __init__(self):
            self.head = None

        def add_head(self, data):
            self.head = Head(data, self.head)

        def add_next(self,data):
            if not self.head :
                self.add_head(data)
            else:
                body = self.head
                while body.next:
                    body = body.next
                body.next = Head(data,None)

        def get_last(self):
            body = self.head
            while body.next != None:
               body = body.next
            return body.data

        def get_list(self):
            n = self.head
            while n != None:
                print(n.data, end="=>")
                n = n.next
                print()



