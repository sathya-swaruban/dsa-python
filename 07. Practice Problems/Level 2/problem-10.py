# lex_auth_01275172151871897677
"""
Given a stack of lunch boxes maintained in a container, identify the number of lunch boxes of a given color belonging to
a manufacturer.

Class Descriptions
    a) LunchBox Class:
        - color
        - manufacturer
        - __init__(color, manufacturer)
        - get_color()
        - get_manufacturer()
        - __str__()
    b) Container Class:
        - box_stack
        - __init__(box_stack)
        - get_box_stack()
        - identify_count(color)     <-- Accept a color and return a dictionary containing the name of the manufacturer
                                        (key) and count of lunch boxes (value) of mentioned color.

Note: If a lunchbox with the specified color is not found, return 0.  Perform case-insensitive string comparison.
"""


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


class LunchBox:
    def __init__(self, color, manufacturer):
        self.__color = color
        self.__manufacturer = manufacturer

    def get_color(self):
        return self.__color

    def get_manufacturer(self):
        return self.__manufacturer

    def __str__(self):
        return '{} color {} lunch box.'.format(self.__color, self.__manufacturer)


class Container:
    def __init__(self, box_stack):
        self.__box_stack = box_stack

    def get_box_stack(self):
        return self.__box_stack

    def identify_count(self, color):
        result_dict = dict()
        while not self.__box_stack.is_empty():
            lunch_box = self.__box_stack.pop()
            if lunch_box.get_color().lower() == color.lower():
                manufacturer = lunch_box.get_manufacturer()
                if manufacturer not in result_dict.keys():
                    result_dict[manufacturer] = 1
                else:
                    result_dict[manufacturer] = result_dict.get(manufacturer) + 1
        return result_dict if result_dict else 0


if __name__ == '__main__':
    lunch_box1 = LunchBox('Blue', 'Tupperware')
    lunch_box2 = LunchBox('Blue', 'Signoraware')
    lunch_box3 = LunchBox('Green', 'Tupperware')
    lunch_box4 = LunchBox('Orange', 'Signoraware')
    lunch_box5 = LunchBox('Green', 'Tupperware')
    lunch_box6 = LunchBox('Blue', 'Signoraware')
    lunch_box7 = LunchBox('Blue', 'Tupperware')
    lunch_box8 = LunchBox('Blue', 'Signoraware')
    stack = Stack(8)
    stack.push(lunch_box1)
    stack.push(lunch_box2)
    stack.push(lunch_box3)
    stack.push(lunch_box4)
    stack.push(lunch_box5)
    stack.push(lunch_box6)
    stack.push(lunch_box7)
    stack.push(lunch_box8)
    container = Container(stack)
    result = container.identify_count('Blue')
    if result == 0:
        print(result)
    else:
        for key, value in result.items():
            print(key, '-', value)
