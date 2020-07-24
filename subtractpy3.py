import re
import sys
import string
import time


name = "melanie"


code = name+"-code.txt"

kept_words_file = name+"-words.txt"

code_file = open(code, 'r').read()



# print (code_file)


kept_words = ["\n","\\\"",")","(","<",">",".","[","]","{","}","="]
for line in open(kept_words_file):
    kept_words.append(line.strip())
# print(kept_words)




def replaceSpace(code, word):
    newCode = str.replace(code, word, ' ' * len(word))
    # print(newCode)
    return newCode


def keepSpecial(code_file, kept_words):
    codeToSubtract = code_file
    for word in kept_words:
        codeToSubtract = replaceSpace(codeToSubtract, word)
        # print(subtractStrings(code_file, codeToSubtract))
    return subtractStrings(code_file, codeToSubtract)


def subtractStrings(originalCode, codeToSubtract):
    newstring = ""

    for i in range(len(originalCode)):
        if originalCode[i] == codeToSubtract[i]:
            newstring += ' '
            # print(newstring)
        else:
            newstring += originalCode[i]
    return newstring


my_string = code_file

for word in kept_words:
    my_string = replaceSpace(my_string, word)
# print('\033[31m')
# print keepSpecial(code, keptWords)

for line in keepSpecial(code_file, kept_words).splitlines():
    print("\t" * 3 + line)
    time.sleep(0.1)
