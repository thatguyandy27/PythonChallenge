# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import re
import pickle


class Challenge6(ChallengeBase):

    def __init__(self):
        super(Challenge6, self).__init__(
            'http://www.pythonchallenge.com/pc/def/peak.html')
        self.bannerPage = 'http://www.pythonchallenge.com/pc/def/banner.p'

    def getNextChallengeUrl(self):
        return 'http://www.pythonchallenge.com/pc/def/channel.html'

    def getBannerPage(self):
        response = urllib2.urlopen(self.bannerPage)
        content = response.read()

        pickleList = pickle.loads(content)
        for l in pickleList:
            listString = ''
            # print l
            # for t in l:
            print ''.join(map(lambda pair: pair[0] * pair[1], l))
                # listString += t[0] + str(t[1])
                # if t[0] == ' ':
                    # listString += chr(t[1])
                # else:
                    # listString += str(t[1])

            print listString


if __name__ == '__main__':
    challenge = Challenge6()
    challenge.openNextChallengePage()
    # challenge.getBannerPage()
