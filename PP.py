#!/usr/bin/env python
# coding: utf-8

import os

continueCheck = False

while continueCheck == False:

    print("pick an option from below:")
    print("1) Generate idea")
    print("")
    print("2) Append ideas list")
    print("3) Append languages list")
    print("4) Append database list")
    print("5) Append gui list")
    print("")
    print("6) Exit")

    try:
        choice = int(input("input: "))
        if choice == 1:

            continueCheck = True

            with open("gen.py") as file:

                exec(file.read())

        elif choice == 2:

            continueCheck = True

            with open("idea.py") as file:

                exec(file.read())

        elif choice == 3:

            continueCheck = True

            with open("lang.py") as file:

                exec(file.read())

        elif choice == 4:

            continueCheck = True

            with open("dbp.py") as file:

                exec(file.read())

        elif choice == 5:

            continueCheck = True

            with open("guip.py") as file:

                exec(file.read())

        elif choice == 6:

            continueCheck = True

            quit()

        else:

            print("invalid input, please try again")

    except:

        print("invalid input, please try again")