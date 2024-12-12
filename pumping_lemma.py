#!/usr/bin/env python3

import re
import exrex
import random

# function to check if the infinite string is pumpable 
def is_pumpable(reg_ex, p):

    # generate strings of length >= pumping_length and with a max for simplicity 
    strings = generate_strings(reg_ex, p, p + 10)

    # list to store the pumpable strings we generated, so that later we cna return a random one to the user
    pumpable = []
    # go through generated strings and check if any of them satisfy the pumping lemma
    for s in strings:
        if satisfies_pumping_lemma(s, reg_ex, p):
            pumpable.append(s)

    if len(pumpable) != 0: 
        # get random string from the pumpable ones 
        random_index = random.randint(0, len(pumpable)-1)
        output = pumpable[random_index]

        return output
    
    # none found
    return None


def generate_strings(exp, min_length, max_length):

    # generate strings matching the regex using built-in library
    results = []
    for s in exrex.generate(exp):
        if min_length <= len(s) <= max_length:
            results.append(s)
    return results


# function to check if the string is pumpable
def satisfies_pumping_lemma(s, reg_ex, p):

    n = len(s)
    # split string into 3 substrings 
    for i in range(1, p+1):
        for j in range(i + 1, min(n+1, i+p+1)):
            x = s[:i]
            y = s[i:j]
            z = s[j:]

            # y can't be empty and |xy| <= p
            if len(y) > 0 and len(x+y)<=p:

                # once we have valid substrings, we need to see if we can pump them 
                # test for just a few i to save time 
                for k in range(0, 7):
                    pumped = x + (y * k) +z     # pump y up 

                    # if the pumped string isn't a full match with the regex, it isn't pumpable
                    if not re.fullmatch(reg_ex, pumped):
                        return False
    return True


def main():
    reg_ex = input("Enter an infinited string language: ").strip()
    p = int(input("Enter the pumping length as a positive integer (p): ").strip())
    if p <= 0:
            print("Pumping length must be a positive integer")

    string = is_pumpable(reg_ex, p)
    if string is not None:
        print(f"String '{string}' is pumpable for the langage '{reg_ex}'.")
    else: 
        print(f"No string is pumpable for the language, so it is not regular '{reg_ex}'.")


if __name__ == "__main__":
    main()