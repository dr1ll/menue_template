#!/usr/bin/python
#-*- coding: utf-8 -*-

##################################################
# menue_template.py                              # 
# For Linux / Python 2.7.3 / standard-windowsize #
# - template for an cli-menue                    #
# - works with vars, insert your defs            #
##################################################

__author__ = "dr1ll"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus"


import os

### menue-vars

# Count your versions here:
version = "0.0.4"

# How many columns do you have for default (Standard=80)?
columns = 80

# Name oy your app, showed in first line
title = "Some Menue for Linux v"

# Insert some hints
hint1 = "# This is an empty template"
hint2 = "[Enter]: More options"
hint3 = "[Q]: Quit"


# Enter the name of functions from your py-script instead

text_for_functions = []

# Functiontext1
text_for_functions.append("function1")
# 2
text_for_functions.append("")
# 3
text_for_functions.append("")
# 4
text_for_functions.append("")
# 5
text_for_functions.append("")
# 6
text_for_functions.append("")
# 7
text_for_functions.append("")
# 8
text_for_functions.append("")
# 9
text_for_functions.append("")
# 10
text_for_functions.append("function10")
# 11
text_for_functions.append("function11")
# 12
text_for_functions.append("")
# 13
text_for_functions.append("")
# 14
text_for_functions.append("")
# 15
text_for_functions.append("")
# 16
text_for_functions.append("")
# 17
text_for_functions.append("")
# 18
text_for_functions.append("")
# 19
text_for_functions.append("")
# 20
text_for_functions.append("function20")



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


def function1():
    print"function1 is empty"


def function2():
    print"function2 is empty"


def function3():
    print"function3 is empty"


def function4():
    print"function4 is empty"


def function5():
    print"function5 is empty"


def function6():
    print"function6 is empty"


def function7():
    print"function7 is empty"


def function8():
    print"function8 is empty"


def function9():
    print"function9 is empty"


def function10():
    print"function10 is empty"


def function11():
    print"function11 is empty"


def function12():
    print"function12 is empty"


def function13():
    print"function13 is empty"


def function14():
    print"function14 is empty"


def function15():
    print"function15 is empty"


def function16():
    print"function16 is empty"


def function17():
    print"function17 is empty"


def function18():
    print"function18 is empty"


def function19():
    print"function19 is empty"


def function20():
    print"function20 is empty"


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
            menue_counter = int((which_menue*10)-10)
        elif which_menue == 2:
            menue_counter = int((which_menue*10)-10)
            menue2()
#       elif which_menue == 3:
#           menue3()
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
    print(">>> end\n")

# end