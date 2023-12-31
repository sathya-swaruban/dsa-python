# lex_auth_01275170587139276853
"""
Problem 02:
----------
Write a python function which accepts a linked list of strings and returns the nth element in the linked list.
If the nth element is not found, return "Element not found".

Example-01:
    Input:  Mysore -> Chennai -> Pune -> Chandigarh -> Hyderabad -> Trivandrum -> Jaipur -> Bhubaneswar; n-5
    Output: Hyderabad

Example-02:
    Input:  Mysore -> Chennai -> Pune -> Chandigarh -> Hyderabad -> Trivandrum -> Jaipur -> Bhubaneswar; n-9
    Output: Element not found
"""


# Linked List Implementation
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def set_head(self, new_node):
        self.__head = new_node

    def set_tail(self, new_node):
        self.__tail = new_node

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data(), '->', end=' ')
            temp = temp.get_next()
        print()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")


def find_nth_element(list1, n):
    temp = list1.get_head()
    count = 1
    while temp:
        if count == n:
            return temp.get_data()
        count += 1
        temp = temp.get_next()
    return 'Element not found'


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add("Mysore")
    linked_list.add("Chennai")
    linked_list.add("Pune")
    linked_list.add("Chandigarh")
    linked_list.add("Hyderabad")
    linked_list.add("Trivandrum")
    linked_list.add("Jaipur")
    linked_list.add("Bhubaneswar")
    result = find_nth_element(linked_list, 4)
    print("The nth element is:", result)
