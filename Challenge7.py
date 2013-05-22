# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import re
import os
import zipfile


class Challenge7(ChallengeBase):

    def __init__(self):
        super(Challenge7, self).__init__(
            'http://www.pythonchallenge.com/pc/def/channel.html')
        self.regex = re.compile('Next nothing is ([\d]*)')

    def getZipFile(self):
        response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
        print response.getcode()
        print response.info()
        return 'channel.zip'

    def unzipContent(self, fileName):
        f = zipfile.ZipFile(fileName)
        commentList = []
        nextNothing = '90052'

        while nextNothing:
            fileName = nextNothing + '.txt'
            txtFile = f.open(fileName)
            commentList.append(f.getinfo(fileName).comment)
            match = self.regex.search(txtFile.read())

            if match:
                nextNothing = match.group(1)
            else:
                nextNothing = None

        print ''.join(commentList)




        # for fileInfo in f.infolist():
        #    if fileInfo.comment:
        #        commentList.append(fileInfo.comment)
        #print ''.join(commentList)
        # for fileName in f.namelist():
        #    content = f.open(fileName).read()
        #    print fileName
        #    print content


    def getNextNothing(self):
        nextNothing = '90052'

        while nextNothing:
            previousNothing = nextNothing
            nextNothing = self.readFile(nextNothing)
            if not nextNothing.isdigit():
                previousNothing = nextNothing
                nextNothing = None

        print previousNothing

    def readFile(self, nextNothing):
        currentPath = os.getcwd() + "\\channel\\" + nextNothing + '.txt'
        f = open(currentPath)
        text = f.readline()
        print text
        match = self.regex.search(text)
        if match:
            return match.group(1)

        return None


if __name__ == '__main__':
    challenge = Challenge7()
    # challenge.openNextChallengePage()
    # challenge.getNextNothing()
    challenge.unzipContent(os.getcwd() + "\\channel.zip")
