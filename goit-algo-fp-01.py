class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_node_at_beginning(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        if self.head:
            current = self.head
            while current:
                print(current.data)
                current = current.next
        else:
            print("Linked list is empty")

    def reverse(self):
        if self.head:
            if not self.head.next:
                return
        else:
            return
        node_stack = []
        current = self.head
        while current.next:
            node_stack.append(current)
            current = current.next
        self.head = current
        while len(node_stack) > 0:
            current.next = node_stack.pop()
            current = current.next
        current.next = None

    def sort(self, descending = False):
        if self.head:
            if not self.head.next:
                return
        else:
            return
        node_stack = []
        current = self.head
        while current.next:
            node_stack.append(current)
            current = current.next
        self.head = current
        while len(node_stack) > 0:
            current_to_insert = node_stack.pop()
            if current_to_insert.data < self.head.data:
                self.insert_node_at_beginning(current_to_insert)
            else:
                current_in_sorted_llist = self.head
                while current_in_sorted_llist.next and (current_to_insert.data >= current_in_sorted_llist.next.data):
                    current_in_sorted_llist = current_in_sorted_llist.next
                current_in_sorted_llist.next, current_to_insert.next = current_to_insert, current_in_sorted_llist.next
        if descending:
            self.reverse()

def merge_two_sorted_linked_lists(left_list:LinkedList, right_list:LinkedList, descending = False):
    merged_list = LinkedList()
    current_left = left_list.head
    current_right = right_list.head
    while current_left and current_right:
        if (current_left.data < current_right.data and not descending) or (current_left.data > current_right.data and descending):
            merged_list.insert_at_end(current_left.data)
            current_left = current_left.next
        else:
            merged_list.insert_at_end(current_right.data)
            current_right = current_right.next
    while current_left: # leftovers
        merged_list.insert_at_end(current_left.data)
        current_left = current_left.next
    while current_right: # leftovers
        merged_list.insert_at_end(current_right.data)
        current_right = current_right.next
    return merged_list

llist1 = LinkedList()
llist1.insert_at_end(5)
llist1.insert_at_end(555)
llist1.insert_at_end(55)
llist1.insert_at_end(5555)
llist1.sort()
print("sorted llist1:")
llist1.print_list()

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(222)
llist2.insert_at_end(22)
llist2.sort(descending=True)
print("sorted desc llist2:")
llist2.print_list()

llist2.reverse()
llist3 = merge_two_sorted_linked_lists(llist1, llist2)
print("merged asc llist3:")
llist3.print_list()

llist1.reverse()
llist2.reverse()
llist4 = merge_two_sorted_linked_lists(llist1, llist2, descending=True)
print("merged desc llist4:")
llist4.print_list()
