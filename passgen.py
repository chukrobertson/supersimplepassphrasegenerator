#!/usr/bin/env python
# coding: utf-8

import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
filename = r'words.txt'
lines = open(filename).read().split('\n')

def passWordGen():
    passlen = int(input("How many characters required? \n"))
    if passlen <=100:
        password = " ".join(secure_random.choice(symbols) for i in range(passlen))
        print("Your password is:","\n",password)
    else:
        print("Choose a password length of 100 characters or less.")
        passWordGen()

def passPhraseGen():
    phralen = int(input("How many words in phrase? \n"))
    if phralen <=100:
        phrase = " ".join(secure_random.choice(lines) for i in range(phralen))
        print("Your passphrase is:","\n",phrase)
    else:
        print("Choose a passphrase with 100 words or less.")
        passPhraseGen()

def randPhraseGen():
    tmp = []
    print("Generating a list of 1000 random 4 character passwordlets.\n")
    for _ in range(1000):
        password = " ".join(secure_random.choice(symbols) for i in range(4))
        tmp.append(password+"  ")
    print("Done!\n")
    phralen2 = int(input("How many words in phrase?\n"))
    if phralen2 <= 100:
        phrase = " ".join(secure_random.choice(tmp) for i in range(phralen2))
        print("Your VERY secure passphrase is:","\n",phrase)
    else:
        print("Choose a passphrase with 100 words or less.")
        randPhraseGen()

def entry():
    try:
        cmd = int(input("""
                        ################################################
                        Simple Password/Passphrase Generator(passgen.py)
                        ------------------------------------------------
                        Generate a random secure password or passphrase.
                        This does NOT save what you generate. Enjoy :)
                        ################################################
                        Select:
                        1. To generate a secure password of (x) length.
                        2. To generate a secure passphrase of (x) length.
                        3. To generate a VERY secure passphrase of (x) length from random passwords of 4 chars.
                        4. Exit

                        """))

        if cmd == int(1):
            passWordGen()
        elif cmd == int(2):
            passPhraseGen()
        elif cmd == int(3):
            randPhraseGen()
        elif cmd == int(4):
            print("Goodbye!")
        else:
            print("Please press 1 or 2 or 3 or 4")
            entry()
    except:
        print("Please press 1 or 2 or 3 or 4")
        entry()

entry()