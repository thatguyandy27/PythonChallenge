# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import re


class Challenge6(ChallengeBase):

    def __init__(self):
        super(Challenge6, self).__init__(
            'http://www.pythonchallenge.com/pc/def/peak.html')

if __name__ == '__main__':
    challenge = Challenge6()
    challenge.openNextChallengePage()
