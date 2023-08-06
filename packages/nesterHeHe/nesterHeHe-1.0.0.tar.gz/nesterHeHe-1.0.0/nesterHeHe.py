'''This is "nester.py", a module that provides a function called print_lol(),
which is used to print a table,containing or not containing a nested list'''

def print_lol(the_list):
    '''This function takes a positional parameter called "the_list", which can
    be any Python list(can contain nested lists).Each item of the specified list
    is output (recursively) to the screen, and each item occupies one line'''
    for i in the_list:
        if isinstance(i,list):
            print_lol(i)
        else:
            print(i)
