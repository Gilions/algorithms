class LinkedList:
    """
    LinketList
    Methods:
        append - adds new item.
        count - displays the number of values
        out - show all items
        get - get value on index
            param:
                index: int
        insert - insert new item
            param:
                item: Any type, index: int
        delete - delete any item
            param:
                index: int
    """
    class Node:
        # Initialization
        def __init__(self, item, next_item=None):
            self.item = item
            self.next_item = next_item

    head = None

    def append(self, item):
        # Add item
        if self.head is None:
            self.head = self.Node(item)
            return item

        node = self.head
        while node.next_item:
            node = node.next_item

        node.next_item = self.Node(item)
        return item

    def out(self):
        # Show all items
        node = self.head
        if node is None:
            print('linked list is empty')
        else:
            while node.next_item:
                print(node.item)
                node = node.next_item
            print(node.item)

    def count(self):
        # Displays the number of values
        if self.head == None:
            return 0
        node = self.head
        count = 1
        while node.next_item:
            node = node.next_item
            count += 1
        return count

    def get(self, index):
        # Get value on index
        if self.head == None:
            return f'Linked list is empty'
        i = 0
        node = self.head
        try:
            while i < index:
                i += 1
                node = node.next_item
            return node.item
        except Exception:
            return f'Index out of range, max index = {self.count() - 1}'

    def insert(self, item, index):
        # Insert new item
        if index > self.count():
            print(f'Index out of range, max index = {self.count()}')
        else:
            node = self.head
            i = 0
            while i < index:
                i += 1
                prev_node = node
                node = node.next_item
            prev_node.next_item = self.Node(item, next_item=node)

    def delete(self, index):
        # Delete item
        if index >= self.count():
            print(f'Index out of range, max index = {self.count() - 1}')
        else:
            node = self.head
            if index == 0:
                self.head = node.next_item
                del node
            else:
                i = 0
                while i < index:
                    i += 1
                    prev_node = node
                    node = node.next_item

                prev_node.next_item = node.next_item
                del_node = node
                del node
                return del_node
