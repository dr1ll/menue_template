#!/usr/bin/python
#-*- coding: utf-8 -*-

##################################################
# menue_template.py                              # 
# For Linux / Python 2.7.3                       #
# - template for an cli-menue                    #
# - works with vars, insert your defs            #
##################################################

__author__ = "dr1ll"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus"


import os

### Change these vars for your menue:

# Count your versions here:
versionnumber = "0.0.5"

# How many columns do you have in your window for default (Standard=80)?
columns = 80

# Name oy your app, this is shown in the first line
title = "Some Menue for Linux"

# Insert some hints
hint1 = "# This is an empty template"
hint2 = "[Enter]: More options"
hint3 = "[Q]: Quit"

# Don't change:
version = " v"+versionnumber
text_for_functions = []
emptyfunction = "This function is empty"


### Inserting your functionality:

# Insert: to os.system('[name of your intern def/function etc. or execute somescript.py]')
# Insert: text_for_functions.append("[String to decribe your function etc.]")
# Remove: print(emptyfunction)

def function1():
    os.system('python /home/user/menue_template.py')


text_for_functions.append("Noch einmal...")


def function2():
    print(emptyfunction)


text_for_functions.append("")


def function3():
    print(emptyfunction)


text_for_functions.append("")


def function4():
    print(emptyfunction)


text_for_functions.append("")


def function5():
    print(emptyfunction)


text_for_functions.append("")


def function6():
    print(emptyfunction)


text_for_functions.append("")


def function7():
    print(emptyfunction)


text_for_functions.append("")


def function8():
    print(emptyfunction)


text_for_functions.append("")


def function9():
    print(emptyfunction)


text_for_functions.append("")


def function10():
    print(emptyfunction)


text_for_functions.append("function10")


def function11():
    print(emptyfunction)


text_for_functions.append("")


def function12():
    print(emptyfunction)


text_for_functions.append("")


def function13():
    print(emptyfunction)


text_for_functions.append("")


def function14():
    print(emptyfunction)


text_for_functions.append("")


def function15():
    print(emptyfunction)


text_for_functions.append("")


def function16():
    print(emptyfunction)


text_for_functions.append("")


def function17():
    print(emptyfunction)


text_for_functions.append("")


def function18():
    print(emptyfunction)


text_for_functions.append("")


def function19():
    print(emptyfunction)


text_for_functions.append("")


def function20():
    print(emptyfunction)


text_for_functions.append("function20")


#!!! STOP inserting stuff here !!!


def header():
    os.system("clear")
    length = int(len(title+version+" "*2))
    print("+"*(int(columns/2)-int(length/2))+" "+title+version+" "+"+"*(int((columns/2)-1)-int(length/2)))
    print
    print(hint1)
    print(hint2)
    print(hint3)
    print


def footer():
    pass


def choiceinput():
    answer = str(raw_input("Your choice (0-9):\n\n>>> "))
    return answer


def menue1():
    header()
    for i in range(10):
        print(str(i)+" - "+text_for_functions[i])
    print
    footer()


def menue2():
    header()
    for i in range(10):
        print(str(i)+" - "+text_for_functions[i+10])
    print
    footer()


#def menue3():
#   header()
#   for i in range(10):
#       print(str(i)+" - "+text_for_functions[i+20])
#   print
#   footer()


if __name__ == '__main__':

    goon = True
    which_menue = 1
    counter = 0
    while goon == True:
        if counter > 0:
            raw_input("\nPress Enter to continue!")
        counter += 1
        if which_menue == 1:
            menue1()
        elif which_menue == 2:
            menue2()
#       elif which_menue == 3:
#           menue3()
        menue_counter = int((which_menue*10)-10)
        choice = choiceinput()
        choices = range(10)
        choice_control = 999
        if choice == "0" or choice == "1" or choice == "2" or choice == "3" or choice == "4":
            choice_control = int(choice)
        if choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9":
            choice_control = int(choice)
        if choice_control in range(10):
            function_string = 'function'+str(choice_control+1+menue_counter)
            locals()[function_string]()
        if choice == "Q" or choice == "q":
            goon = False
        elif choice == "":
            if which_menue == 1:
                which_menue = 2
            elif which_menue == 2:
                which_menue = 1
#           elif which_menue == 3:
#               which_menue = 1
            counter = 0
    os.system('clear')
    print(">>> end\n")
# end
