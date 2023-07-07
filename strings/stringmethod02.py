#!/usr/bin/env python3
"""Learning to create small string || Author: RZFeeser@alta3.com"""

def main():
   """ Run-time code"""
   # create a small string
   lilstring = "GGlitter is learning python code for network development"
   newlist = lilstring.split(" ") # this returns a list
   print(newlist)

   # create a list of strings
   myiplist = ["192", "168", "0", "12"]
   # set singleip as the result of joining the list myiplist around the "."
   singleip = ".".join(myiplist)
   # display singleip
   print(singleip)

# call our main function
main()



