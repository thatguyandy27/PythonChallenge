# -*- coding: utf-8 -*-
from ChallengeBase import ChallengeBase


class Challenge11(ChallengeBase):

    def __init__(self):
        super(Challenge11, self).__init__(
            'http://www.pythonchallenge.com/pc/return/bull.html')

    def getValue(self, index):
        maxCounter = index
        counter = 0
        value = '1'
        while counter < maxCounter:
            value = self.getCharacterCount(value)
            counter += 1

        return len(value)

    def getCharacterCount(self, string):
        currentCharCount = 1
        currentChar = string[0]
        currentCharIndex = 1
        characterList = []

        while (True):
            if currentCharIndex >= len(string):
                break

            if currentChar == string[currentCharIndex]:
                currentCharCount += 1
            else:
                characterList.append(str(currentCharCount))
                characterList.append(currentChar)
                currentCharCount = 1
                currentChar = string[currentCharIndex]

            currentCharIndex +=1

        characterList.append(str(currentCharCount))
        characterList.append(currentChar)

        return ''.join(characterList)

    def getNextChallengeUrl(self):
        return 'http://www.pythonchallenge.com/pc/return/' + str(self.getValue(30)) + '.html'

if __name__ == '__main__':
    challenge = Challenge11()
    challenge.openNextChallengePage()

