# -*- coding: utf-8 *-*
import string

baseUrl = 'http://www.pythonchallenge.com/pc/def/map.html'
upperLimit = ord('z') + 1
lowerLimit = ord('a')


def challenge2():
    # K => M = 2
    # 0 => Q = 2
    # E => G = 2
    scrambledString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    # conver to a list first because strings are immutable
    listString = list(scrambledString)

    listString = [conversionFunction(char) for char in listString]

    print ''.join(listString)


def conversionFunction(char):
    # if string.letters.find(char):
    if string.letters.find(char) > -1:
        charValue = ord(char) + 2

        if charValue >= upperLimit:
            charValue = lowerLimit + (charValue - upperLimit)

        return chr(charValue)
    else:
        return char
    # else:
    #    return char


def convertUrl():
    convertedLetters = list(string.ascii_lowercase)
    convertedLetters.append(convertedLetters.pop(0))
    convertedLetters.append(convertedLetters.pop(0))
    trantab = string.maketrans(string.ascii_lowercase, ''.join(convertedLetters))
    print baseUrl.translate(trantab)

if __name__ == '__main__':
    challenge2()
    convertUrl()

