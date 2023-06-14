'''
Answer for Question 3 - Function

Name:
SID:
unikey:

'''

# empty strings are avoided by checking that the length is positive

def is_valid_length(name):
    return len(name) > 0 and len(name) < 10


def is_valid_start(name):
    return len(name) > 0 and name[0].isalpha()


def is_one_word(name):
    return len(name) > 0 and len(name.split(' ')) == 1


def is_valid_name(name):
    return is_valid_length(name) and is_valid_start(name) and is_one_word(name)
