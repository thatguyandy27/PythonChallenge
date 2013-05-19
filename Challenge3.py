# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import re


class Challenge3(ChallengeBase):

    def __init__(self):
        super(Challenge3, self).__init__(
            'http://www.pythonchallenge.com/pc/def/ocr.html')

    def getPageSource(self):
        response = urllib2.urlopen(self.challengeUrl)
        content = response.read()
        return content

    def getMess(self):
        content = self.getPageSource()
        regex = re.compile('<!--([\S\s]*?)-->')
        return regex.findall(content)[1]

    def getMessCharacters(self, mess):
        count = {}
        for c in mess:
            if not c in count:
                count[c] = 0
            count[c] += 1

        return count

    def getSingleAppearanceChars(self, characterMess):
        singleCharacterList = []
        for c in characterMess:
            if characterMess[c] == 1:
                singleCharacterList.append(c)

        return singleCharacterList

    def getSingleAppearanceCharsInOrder(self):
        mess = self.getMess()
        characterMess = self.getMessCharacters(mess)
        characters = self.getSingleAppearanceChars(characterMess)
        characterIndex = {}
        for c in characters:
            characterIndex[c] = mess.find(c)

        return sorted((value, key) for (key, value) in characterIndex.items())

    def getNextChallengeUrl(self):
        nextPageTuple = self.getSingleAppearanceCharsInOrder()
        # print nextPageTuple
        # print [x[1] for x in nextPageTuple]
        return 'http://www.pythonchallenge.com/pc/def/' + ''.join([
            x[1] for x in nextPageTuple]) + '.html'


if __name__ == '__main__':
    challenge = Challenge3()
    # challenge.openNextChallengePage()
    # challenge.getPageSource()
    # print challenge.getMess()
    # challenge.getMessCharacters()
    # print challenge.getSingleAppearanceCharsInOrder()
    challenge.openNextChallengePage()
