# lex_auth_01275171910432358466
"""
Problem 06:
----------
Write a python function which accepts two linked lists containing integer data and an integer, n and merges the two
linked lists, such that list2 is merged with list1 after n number of nodes.

Assume that value of n will always be less than or equal to the number of nodes in list1.

Example:
    Inputs:
        list1: 1->2->3->4->5->6
        list2: 9->8->11
        n: 2
    Output:
        list3: 1->2->9->8->11->4->3->5
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


def skip_n_merge_list(list1, list2, n):
    count = 1
    list1_temp = list1.get_head()
    while list1_temp:
        list1_tail = list1.get_tail()
        list2_head = list2.get_head()
        list2_tail = list2.get_tail()
        if list1_temp == list1_tail:
            list1_tail.set_next(list2_head)
            break
        if count == n:
            list2_tail.set_next(list1_temp.get_next())
            list1_temp.set_next(list2_head)
            break
        list1_temp = list1_temp.get_next()
    return list1


if __name__ == '__main__':
    list_a = LinkedList()
    list_a.add(1)
    list_a.add(2)
    list_a.add(4)
    list_a.add(3)
    list_a.add(5)
    list_b = LinkedList()
    list_b.add(9)
    list_b.add(8)
    list_b.add(11)
    merged_list = skip_n_merge_list(list_a, list_b, 2)
    merged_list.display()
