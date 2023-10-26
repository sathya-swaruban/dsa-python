# lex_auth_0127716946325422081069

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


if __name__ == '__main__':
    goods1 = Goods('television', 26)
    goods2 = Goods('microwave', 15)
    goods3 = Goods('mixers', 20)
    goods4 = Goods('sofaset', 5)
    goods5 = Goods('chairs', 12)
    goods6 = Goods('computertables', 5)
    queue = Queue(6)
    queue.enqueue(goods1)
    queue.enqueue(goods2)
    queue.enqueue(goods3)
    queue.enqueue(goods4)
    queue.enqueue(goods5)
    queue.enqueue(goods6)
    while not queue.is_empty():
        print(queue.dequeue())
