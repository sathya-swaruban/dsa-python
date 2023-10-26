# lex_auth_01275171005175398456
"""
Problem 03:
----------
A bank wants to maintain the list of its customers. Write a python program to implement the class description given
below:

Class Descriptions
    a) Customer Class:
        - name
        - account_balance
        - __init__(name, account_balance)
        - get_name()
        - get_account_balance()
        - get_account_balance()
        - __str__()
    b) Bank Class:
        - bank_name
        - customer_list             <--Linked list where data in each node refers to a customer
        - __init__(bank_name, customer_list)
        - get_bank_name()
        - get_customer_list()
        - insert_customer(customer) <--Accept a customer object and insert it as the second customer in the linked list

Create objects of Customer class, represent list of customers as a Linked list, create object of Bank class and test
your program by invoking the methods.
"""


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


class Bank:
    def __init__(self, bank_name, customer_list):
        self.__bank_name = bank_name
        self.__customer_list = customer_list

    def get_bank_name(self):
        return self.__bank_name

    def get_customer_list(self):
        return self.__customer_list

    def insert_customer(self, customer):
        head = self.__customer_list.get_head()
        node = Node(customer)
        node.set_next(head.get_next())
        head.set_next(node)


class Customer:
    def __init__(self, name, account_balance):
        self.__name = name
        self.__account_balance = account_balance

    def get_name(self):
        return self.__name

    def get_account_balance(self):
        return self.__account_balance

    def __str__(self):
        print(self.__name, self.__account_balance)


if __name__ == '__main__':
    customer1 = Customer('Alice', 10000)
    customer2 = Customer('Bob', 15000)
    customer3 = Customer('Clair', 12000)
    customers = LinkedList()
    customers.add(customer1)
    customers.add(customer2)
    customers.add(customer3)
    bank = Bank('ICICI', customers)
    customer4 = Customer('David', 20000)
    bank.insert_customer(customer4)
    records = bank.get_customer_list()
    records.display()
