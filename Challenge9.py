# -*- coding: utf-8 -*-
from ChallengeBase import ChallengeBase
import bz2


class Challenge9(ChallengeBase):

    def __init__(self):
        super(Challenge9, self).__init__(
            'http://www.pythonchallenge.com/pc/def/integrity.html')

    def decompress(self):
        compressedUserName = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
        compressedPassword = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
        print self.decompressString(compressedUserName)
        print self.decompressString(compressedPassword)

    def decompressString(self, compressedString):
        return bz2.decompress(compressedString)

    def getNextChallengeUrl(self):
        return 'http://www.pythonchallenge.com/pc/return/good.html'

if __name__ == '__main__':
    challenge = Challenge9()
    challenge.decompress()
    # challenge.openNextChallengePage()
