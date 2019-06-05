# The purpose of this code is to Create a function called remove_substring that takes two parms; a string and removes all instances of an undesirable substring.


def remove_substring(string, sub):
    output = []
    index = 0
    while index < len(string):
        if string[index: index + len(sub)] == sub:
            index += len(sub)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


# Some strings to test the function:
print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
print(remove_substring('I am NOT learning to code.', 'NOT '))
