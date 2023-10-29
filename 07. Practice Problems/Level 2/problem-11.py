# lex_auth_01275172530025267279
"""
TODO: Problem Statement goes here
"""


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
            for i in range(self.__rear):
                self.__elements[i] = self.__elements[i + 1]
            self.__rear -= 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index], end='<-')
        print()

    def get_max_size(self):
        return self.__max_size


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


class Vehicle:
    def __init__(self, vehicle_type, registration_number, parking_hours):
        self.__vehicle_type = vehicle_type
        self.__registration_number = registration_number
        self.__parking_hours = parking_hours

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_registration_number(self):
        return self.__registration_number

    def get_parking_hours(self):
        return self.__parking_hours


class ParkingLot:
    occupied_parking_lots = LinkedList()

    def __init__(self, total_no_of_lots):
        self.__total_no_of_lots = total_no_of_lots

    def get_total_no_of_lots(self):
        return self.__total_no_of_lots

    def check_parking_availability(self):
        count = 0
        temp = ParkingLot.occupied_parking_lots.get_head()
        while temp:
            temp = temp.get_next()
            count += 1
        return count < self.__total_no_of_lots

    def allocate_parking_lot(self, list_of_vehicles):
        while not list_of_vehicles.is_empty():
            if self.check_parking_availability():
                ParkingLot.occupied_parking_lots.add(list_of_vehicles.dequeue())
            else:
                return list_of_vehicles

    def deallocate_parking_lot(self, registration_number):
        vehicle = ParkingLot.occupied_parking_lots.get_head()
        while vehicle:
            if vehicle.get_data().get_registration_number() == registration_number:
                parking_charge = self.calculate_parking_charge(vehicle.get_data())
                ParkingLot.occupied_parking_lots.delete(vehicle.get_data())
                return [vehicle.get_data(), parking_charge]
            vehicle = vehicle.get_next()
        return -1

    def calculate_parking_charge(self, vehicle):
        vehicle_type = vehicle.get_vehicle_type()
        parking_hours = vehicle.get_parking_hours()
        charge = 0
        if vehicle_type == 'Two Wheeler':
            charge += 10 if parking_hours < 5 else 10 + (parking_hours - 5) * 10
        elif vehicle_type == 'Four Wheeler':
            charge += 20 if parking_hours < 5 else 20 + (parking_hours - 5) * 10
        return charge


if __name__ == '__main__':
    vehicle1 = Vehicle('Two Wheeler', 'KA 05 A 8723', 12)
    vehicle2 = Vehicle('Four Wheeler', 'KL 12 B 7654', 12)
    vehicle3 = Vehicle('Two Wheeler', 'TN 07 A 8055', 12)
    vehicle_queue = Queue(3)
    vehicle_queue.enqueue(vehicle1)
    vehicle_queue.enqueue(vehicle2)
    vehicle_queue.enqueue(vehicle3)
    parking_lot = ParkingLot(2)
    remaining_vehicles = parking_lot.allocate_parking_lot(vehicle_queue)
    remaining_vehicles.display()
    amount = parking_lot.deallocate_parking_lot('KL 12 B 7654')
    print(amount)
