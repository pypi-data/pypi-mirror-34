'''This is "nester.py",a module that provides a function called print_lol(),
 which is used to print lists, containing or not containing a nested list.
 Indentation occurs when printing nested lists'''
def print_lol(the_list,level):
    '''This function has two parameters.The first one is "the_list",which can be
   any Python list(can contain nested lists).The second one is "level",which was
   used to insert a tab when a nested list is encountered.Each item of the specified
   list will output (recursively) to the screen, and each item occupies one line'''
    for i in the_list:
        if isinstance(i,list):
            print_lol(i,level+1)
        else:
            for j in range(level):
                print('\t',end='')
            print(i)
