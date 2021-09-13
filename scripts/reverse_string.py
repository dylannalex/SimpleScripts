def reverse1(string):
    reversed_string = ""
    for character in string:
        reversed_string = character + reversed_string
    return reversed_string
