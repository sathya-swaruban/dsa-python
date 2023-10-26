# lex_auth_0127717096857518081088

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


# Queue Implementation
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        return self.__rear == self.__max_size - 1

    def is_empty(self):
        return self.__front > self.__rear

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index], end='<-')

    def get_max_size(self):
        return self.__max_size


class Goods:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        return '{}: {}'.format(
            self.__product,
            self.__quantity
        )


class Compartment:
    def __init__(self, name, no_of_passengers, no_of_goods):
        self.__name = name
        self.__no_of_passengers = no_of_passengers
        self.__no_of_goods = no_of_goods

    def get_name(self):
        return self.__name

    def get_no_of_passengers(self):
        return self.__no_of_passengers

    def get_no_of_goods(self):
        return self.__no_of_goods

    def __str__(self):
        return 'Compartment {} is accommodating {} passengers and {} goods.'.format(
            self.__name,
            self.__no_of_passengers,
            self.__no_of_goods
        )


class Train:
    def __init__(self, train_name, source, destination, passenger_capacity_per_compartment, passenger_goods_ratio):
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__passenger_capacity_per_compartment = passenger_capacity_per_compartment
        self.__passenger_goods_ratio = passenger_goods_ratio
        self.__compartment_list = LinkedList()

    def get_train_name(self):
        return self.__train_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_passenger_capacity_per_compartment(self):
        return self.__passenger_capacity_per_compartment

    def get_passenger_goods_ratio(self):
        return self.__passenger_goods_ratio

    def get_compartment_list(self):
        return self.__compartment_list

    def add_passenger_compartments(self, no_of_passengers):
        serial_number = 0
        passenger_capacity = self.__passenger_capacity_per_compartment
        while no_of_passengers > 0:
            passenger_count = passenger_capacity
            if no_of_passengers < passenger_capacity:
                passenger_count = no_of_passengers % passenger_capacity
            compartment_name = self.__train_name[0] + str(serial_number)
            compartment = Compartment(compartment_name, passenger_count, 0)
            self.__compartment_list.add(compartment)
            no_of_passengers -= passenger_capacity
            serial_number += 1

    def add_goods(self, goods_list):
        no_of_goods = 0
        while not goods_list.is_empty():
            no_of_goods += goods_list.dequeue().get_quantity()
        while no_of_goods > 0:
            tail_compartment = self.__compartment_list.get_tail().get_data()
            passenger_available = tail_compartment.get_no_of_passengers()
            goods_available = tail_compartment.get_no_of_goods()
            remaining_space = (passenger_available // self.__passenger_goods_ratio) - goods_available
            # TODO: check if we can accommodate any goods in the tail compartment
            pass

    def __str__(self):
        return ('Train {} travels from {} to {} with a capacity of {} passenger per compartment and the passenger to '
                'goods ratio is {}.').format(
            self.__train_name,
            self.__source,
            self.__destination,
            self.__passenger_capacity_per_compartment,
            self.__passenger_goods_ratio
        )


if __name__ == '__main__':
    pass
