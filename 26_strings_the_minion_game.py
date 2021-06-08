#!/bin/python3

def minion_game(string):
    vowels = "AEIOU"
    vow_score = 0
    cons_score = 0
    l = len(string)
    for i in range(l):
        if string[i] in vowels:
            vow_score += l - i
        else:
            cons_score += l - i
            
    if cons_score > vow_score:
        print("Stuart " + str(cons_score))
    elif cons_score < vow_score:
        print("Kevin " + str(vow_score))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)