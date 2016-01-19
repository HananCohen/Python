#!/usr/bin/python

###########################################################################################
# File name: oddOrEven.py
# Date: 14/10/2015
# Created By: Hanan Cohen <hanan.c80@gmail.com>
# 
#
###########################################################################################


num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))

if num % 4 == 0:
    print(nm, "is a multiple of 4")
elif num % 2 == 0:
    print(nm, "Is an even number")
else:
    print(nm, "Is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)

