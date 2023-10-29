# lex_auth_012761717559443456689
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


# Stack Implementation
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index -= 1

    def get_max_size(self):
        return self.__max_size


def queue_ordering(input_queue, input_stack):
    output_queue = Queue(input_queue.get_max_size())
    while not input_stack.is_empty():
        if input_stack.pop() == 1:
            input_queue.enqueue(input_queue.dequeue())
        else:
            temp_queue = Queue(input_queue.get_max_size())
            while not input_queue.is_empty():
                data = input_queue.dequeue()
                if input_queue.is_empty():
                    input_queue.enqueue(data)
                    break
                temp_queue.enqueue(data)
            while not temp_queue.is_empty():
                input_queue.enqueue(temp_queue.dequeue())
    while not input_queue.is_empty():
        output_queue.enqueue(input_queue.dequeue())
    return output_queue


if __name__ == '__main__':
    stack = Stack(4)
    stack.push(2)
    stack.push(2)
    stack.push(2)
    stack.push(2)
    queue = Queue(5)
    queue.enqueue('C')
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('D')
    queue.enqueue('A')
    result = queue_ordering(queue, stack)
    result.display()
