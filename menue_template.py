#!/usr/bin/python
#-*- coding: utf-8 -*-

###########################################
# - menue_template.py -
# For Linux / Python 2.7.3 / standard-window
# - template for an cli-menue
# - works with vars
###########################################

__author__ = "dr1ll"
__copyright__ = "GPL 2013"
__license__ = "GPL v3 Plus"


import os

### menue-vars

# count your versions here:
version = "0.0.2"

# How many columns do you have for default (Standard=80)?
columns = 80

# name oy your app, showed in first line
title = "Some Menue for Linux version"

# insert some hints
hint1 = "# This is an empyty template"
hint2 = "[Enter]: More options"
hint3 = "[Q]: Quit"


# enter the name of functions from your py-script instead

text_for_functions = []
# text0
text_for_functions.append("Editor")
# text1
text_for_functions.append("Hamster")
# text2
text_for_functions.append("Sonstwas")
# text3
text_for_functions.append("Irgendwas")
# text4
text_for_functions.append("Something")
# text5
text_for_functions.append("")
# text6
text_for_functions.append("")
# text7
text_for_functions.append("")
# text8
text_for_functions.append("")
# text9
text_for_functions.append("")
# text10
text_for_functions.append("")
# text11
text_for_functions.append("")
# text12
text_for_functions.append("")
# text13
text_for_functions.append("")
# text14
text_for_functions.append("")
# text15
text_for_functions.append("")
# text16
text_for_functions.append("")
# text17
text_for_functions.append("")
# text18
text_for_functions.append("")
# text19
text_for_functions.append("")
# text20
text_for_functions.append("")


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
    answer = str(raw_input("Your choice (1-9):\n\n>>> "))
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
    print"function10 is empty"


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
            menue_counter = 10
            menue2()
'''
# Add another menue:
        elif which_menue == 3:
            menue_counter = 20
            menue3()
'''
        choice = choiceinput()

        if choice == "0":
            function1()
        elif choice == "1":
            function2()
        elif choice == "2":
            function3()
        elif choice == "3":
            function4()
        elif choice == "4":
            function5()
        elif choice == "5":
            function6()
        elif choice == "6":
            function7()
        elif choice == "7":
            function8()
        elif choice == "8":
            function9()
        elif choice == "9":
            function10()
        elif choice == "Q" or choice == "q":
            goon = False
        elif choice == "":
            if which_menue == 1:
                which_menue = 2
                counter = 0
            elif which_menue == 2:
                which_menue = 1
                counter = 0
    print("\n>>> end\n")

# end