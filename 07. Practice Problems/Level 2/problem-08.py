# lex_auth_01275171967517491271
"""
In a sequence of characters, a letter means en-queue and an asterisk means de-queue.  Write a python function which
accepts the given sequence and returns the string obtained by de-queuing.

Example-01:
    Input:  I*TS** A **BE***AUT**IF**UL** D**AY***
    Output: ITS A BEAUTIFUL DAY

Example-02:
    Input:  E*NE**M*Y S***HI**P*S* O**N T***H*E W***AY**
    Output: ENEMY SHIPS ON THE WAY
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


def create_seqeunce(message):
    result = ''
    queue = Queue(len(message))
    for character in message:
        if character == '*':
            result += queue.dequeue()
        else:
            queue.enqueue(character)
    return result


if __name__ == '__main__':
    print(create_seqeunce("E*NE**M*Y S***HI**P*S* O**N T***H*E W***AY**"))
