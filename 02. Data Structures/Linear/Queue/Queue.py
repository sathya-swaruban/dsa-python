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


if __name__ == '__main__':
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.display()
