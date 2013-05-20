# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import re


class Challenge5(ChallengeBase):

    def __init__(self):
        super(Challenge5, self).__init__('http://www.pythonchallenge.com/pc/def/linkedlist.php')
        self.baseUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
        self.regex = re.compile('and the next nothing is ([\d]*)')

    def getNextChallengeUrl(self):
        previousNothing = '12345'
        nextNothing = self.retrievePage(previousNothing)

        while nextNothing:
            previousNothing = nextNothing
            nextNothing = self.retrievePage(nextNothing)
            if not nextNothing.isdigit():
                previousNothing = nextNothing
                nextNothing = None

        return 'http://www.pythonchallenge.com/pc/def/' + previousNothing

    def retrievePage(self, nextNothing):
        response = urllib2.urlopen(self.baseUrl + nextNothing)
        content = response.read()
        print content
        match = self.regex.search(content)
        if match:
            return match.group(1)
        elif content == 'Yes. Divide by two and keep going.':
            return str(int(nextNothing) / 2)
        else:
            return content


if __name__ == '__main__':
    challenge = Challenge5()
    challenge.openNextChallengePage()
    #challenge.findNextChallengeURL()

