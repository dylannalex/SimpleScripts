def reverse1(string):
    reversed_string = ""
    for character in string:
        reversed_string = character + reversed_string
    return reversed_string


def reverse2(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string


def reverse3(string):
    return string[::-1]


string = "Hello world!"
print(reverse1(string))
print(reverse2(string))
print(reverse3(string))
