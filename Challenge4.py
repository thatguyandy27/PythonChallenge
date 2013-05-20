# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import re


class Challenge4(ChallengeBase):

    def __init__(self):
        super(Challenge4, self).__init__(
            'http://www.pythonchallenge.com/pc/def/equality.html')

    def getPageSource(self):
        response = urllib2.urlopen(self.challengeUrl)
        content = response.read()
        return content

    def getMess(self):
        content = self.getPageSource()
        regex = re.compile('<!--([\S\s]*?)-->')
        return regex.search(content).group(1)

    def getLetters(self, text):
        regex = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
        return regex.findall(text)

    def getNextChallengeUrl(self):
        mess = self.getMess()
        letters = self.getLetters(mess)
        return 'http://www.pythonchallenge.com/pc/def/' + ''.join(letters) + '.php'


if __name__ == '__main__':
    challenge = Challenge4()
    # mess = challenge.getMess()
    # letter = challenge.getLetters(mess)
    # print letter
    # print ''.join(letter)
    challenge.openNextChallengePage()
