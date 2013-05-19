# -*- coding: utf-8 *-*
import webbrowser


class ChallengeBase(object):

    def __init__(self, url):
        self.challengeUrl = url

    def getNextChallengeUrl(self):
        return self.challengeUrl

    def openNextChallengePage(self):
        webbrowser.open(self.getNextChallengeUrl())
