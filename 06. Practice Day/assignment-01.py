# lex_auth_01275171237137612864

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


# Stack Implementation
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        return self.__top == self.__max_size - 1

    def is_empty(self):
        return self.__top == -1

    def push(self, data):
        if self.is_full():
            print("The stack is full!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index], end='<-')
                index -= 1
        print()

    def get_max_size(self):
        return self.__max_size


def check_triangle_number(queue1):
    stack1 = Stack(queue1.get_max_size() // 2)
    while not queue1.is_empty():
        num1 = queue1.dequeue()
        num2 = queue1.dequeue()
        total = num1 * (num1 + 1) / 2
        if total == num2:
            stack1.push(num2)
    return stack1


if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue(7)
    queue.enqueue(28)
    queue.enqueue(8)
    queue.enqueue(35)
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(5)
    queue.enqueue(15)
    queue.enqueue(2)
    queue.enqueue(3)
    print("The elements in the queue are:")
    queue.display()
    check_triangle_number(queue)
