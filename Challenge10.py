# -*- coding: utf-8 -*-
from ChallengeBase import ChallengeBase


class Challenge10(ChallengeBase):

    def __init__(self):
        super(Challenge10, self).__init__(
            'http://www.pythonchallenge.com/pc/return/good.html')


if __name__ == '__main__':
    challenge = Challenge10()
    challenge.openNextChallengePage()
