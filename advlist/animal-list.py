#!/usr/bin/env python3
"""Practicing making  lists |GGlitter
    List - making a list of animals with three letter in their name"""

def main():
    animals = ["fox", "dog", "cow", "hen", "hog"]
    
#displays my list of animals , my first list
    print(animals)

#my second list of animals
    animals2 = ["cat", "jay"]

#display only item 2 in my first list
    print(animals[2])

#append to my first list by my second list
    animals.append(animals2)
    print(animals)

main()


