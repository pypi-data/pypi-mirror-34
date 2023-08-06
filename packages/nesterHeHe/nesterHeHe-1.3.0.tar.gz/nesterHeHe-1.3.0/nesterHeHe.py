'''This is "nester.py",a module that provides a function called print_lol(),
 which is used to print lists, containing or not containing a nested list.
 Indentation can be chosen when printing nested lists'''
def print_lol(the_list,indent=False,level=0):
    '''This function has three parameters.The first one is "the_list",which can be
   any Python list(can contain nested lists).The second one is "indent",which was
   set to False by default.If you want a indentation when printing nested lists,
   please set to True.The third one is "level",which controls the number of tabs
   when a nested list is encountered.It was set to 0 by default.Each item of the
   specified list will output (recursively) to the screen, and each item occupies
   one line'''
    for i in the_list:
        if isinstance(i,list):
            print_lol(i,indent,level+1)
        else:
            if indent==True:
                print(level*'\t', end='')
            print(i)