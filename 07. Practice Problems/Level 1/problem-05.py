# lex_auth_01275171685269504062
"""
Problem 05:
----------
Write a python function which accepts two linked list containing integer data sorted in increasing order and returns a
new linked list containing common elements from the two linked lists.

Assume that there always be at least one element in common between the two linked lists.

Example:
    Inputs:
        list1: 1->2->3->4->5->6
        list2: 2->4->6->8
    Output:
        list3: 2->4->6
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


def sorted_intersection_of_lists(list1, list2):
    list3 = LinkedList()
    list1_temp = list1.get_head()
    while list1_temp:
        list2_temp = list2.get_head()
        while list2_temp:
            list1_data = list1_temp.get_data()
            list2_data = list2_temp.get_data()
            if list1_data == list2_data:
                list3.add(list1_data)
            list2_temp = list2_temp.get_next()
        list1_temp = list1_temp.get_next()
    return list3


if __name__ == '__main__':
    list_a = LinkedList()
    list_a.add(1)
    list_a.add(2)
    list_a.add(3)
    list_a.add(4)
    list_a.add(5)
    list_a.add(6)
    list_b = LinkedList()
    list_b.add(2)
    list_b.add(4)
    list_b.add(6)
    list_b.add(8)
    intersected_list = sorted_intersection_of_lists(list_a, list_b)
    intersected_list.display()
