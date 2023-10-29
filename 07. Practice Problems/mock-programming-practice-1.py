# lex_auth_012768145018527744212
"""
Consider an input_list containing strings and each strings separated by ":" in the following format:
    "<<left_string>> : <<right_string>>"

Write a function which accepts the input_list mentioned above as input parameter and returns an output_list containing
strings. The output_list is created based on following rules:

For each string in the input_list –
    -   Identify the index position of alphabets in left_string and index position of integers on right_string.
    -   Generate a left index string using the indices obtained from left_string and right index string from the indices
        obtained from right_strings. Concatenate them delimited by ":" to get output_string and add it to output_list.
    -   If the left_string contains no alphabets add "X" in place of left index string and if the right_string contains
        no integer digits add "Y" to the right index string of output_string.

Example:
    - input_list: ['Dz2A:fg12x','A12z3:xy9z1']
    - output_list: ['013:23','03:24']

Assumption:
    -   The input_list would contain at least one element
    -   Each string element of input_list would contain only one colon (":")
"""


def fun(input_list):
    output_list = []
    for string_i in input_list:
        left_string_i, right_string_i = string_i.split(':')
        left_string_o, right_string_o = '', ''
        for i, character in enumerate(left_string_i):
            if character.isalpha():
                left_string_o += str(i)
        for i, character in enumerate(right_string_i):
            if character.isnumeric():
                right_string_o += str(i)
        if not left_string_o:
            left_string_o = 'X'
        if not right_string_o:
            right_string_o = 'Y'
        string_o = (left_string_o + ':' + right_string_o)
        output_list.append(string_o)

    return output_list


if __name__ == '__main__':
    list_input = ['hea23rt:att34ack', 'hea23rt:', ':att34ack']
    list_output = fun(list_input)
    print(list_output)
