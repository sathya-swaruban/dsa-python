# lex_auth_01275171071766528059
"""
Problem 04:
----------
A group of students is waiting in a queue to collect their exam hall tickets from their teacher. But due to heavy crowd,
the teacher announced that the students should form two new queues, Queue1 has students whose names start with "S" and
end with "a" queue and Queue2 has remaining students.

The sequence should be maintained in both the queues as per the original queue. Write a python function which accepts
the original queue and returns a list of queues such that Queue1 is at index position 0 and Queue2 is at index position
1.

Perform case-sensitive string comparison.

Assume that both the output queues have the same size as that of the input queue.

Example:
    Input:  Queue: front->rear("Andy", "Sana", "Nick", "Sam", "George", "Veronica", "Samar", "Serena", "Shanaya")
    Output: [Queue("Sana","Serena","Shanaya"), Queue("Andy", "Nick","Sam","George", "Veronica", "Samar")]
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
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index], end='<-')

    def get_max_size(self):
        return self.__max_size


def hall_ticket_collection(queue1):
    queue_a = Queue(queue1.get_max_size())
    queue_b = Queue(queue1.get_max_size())
    while not queue1.is_empty():
        person = queue1.dequeue()
        if person[0] == 'S' and person[-1] == 'a':
            queue_a.enqueue(person)
        else:
            queue_b.enqueue(person)
    return [queue_a, queue_b]


if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue("Andy")
    queue.enqueue("Sana")
    queue.enqueue("Nick")
    queue.enqueue("Sam")
    queue.enqueue("George")
    queue.enqueue("Veronica")
    queue.enqueue("Samar")
    queue.enqueue("Sarena")
    queue.enqueue("Roger")
    queue.enqueue("Shanaya")
    result = hall_ticket_collection(queue)
    for i in result:
        print("The elements in the new queue are:")
        i.display()
