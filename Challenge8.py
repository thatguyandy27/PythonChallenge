# -*- coding: utf-8 *-*
from ChallengeBase import ChallengeBase
import urllib2
import urllib
import Image


class Challenge8(ChallengeBase):

    def __init__(self):
        super(Challenge8, self).__init__(
            'http://www.pythonchallenge.com/pc/def/oxygen.html')

    def readImage(self):
        # so I know the image is 95 pixels high, and about half of that is
        # 47 so I started with that and printed out the first column's pixels
        # the ones near there that match were from 45 - 53.  That is how
        # I came up with grabbing the pixles from 45 - 53
        img = Image.open('oxygen.png')
        #print img.size
        #print img.info
        #print img.tostring()
        i = 45
        characters = []

        while (i < 52):
            x = 0
            previousChar = None
            while x < img.size[0]:
                pixel = img.getpixel((x, i))
                r = pixel[0]
                # if not r == previousChar:
                characters.append(chr(r))
                # previousChar = r


                #print chr(pixel[0])
                # print str(pixel) + ' => ' + chr(pixel[0]) + chr(pixel[1]) + char(pixel[2])
                x += 7
            i += 1

        #print ''.join(characters)
        # Result here smart guy, you made it. the next level is
        # [105, 10, 16, 101, 103, 14, 105, 16, 121]{v}
        print ''.join(characters)

    def downloadImage(self):
        imageUrl = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
        response1 = urllib.urlopen(imageUrl)
        f = open('oxygen.png', 'wb')
        f.write(''.join(response1.readlines()))
        f.close()


        # request = urllib2.Request(imageUrl,None, {'Connection': 'keep-alive',
        #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        #    'Accept-Encoding': 'gzip,deflate,sdch'})
        # response = urllib2.urlopen(request)
        # print response.getcode()
        # print response.info()
        # responseData = ""
        # while 1:
        #    data = response.read()
        #    if not data:
        #        break
        #    responseData += data

        # print responseData

if __name__ == '__main__':
    challenge = Challenge8()
    # challenge.downloadImage()
    challenge.readImage()
    # characters = [105, 10, 16, 101, 103, 14, 105, 16, 121]
    # i = 0
    # while i < len(characters):
    #    characters[i] = chr(characters[i])
    #    i += 1

    # print ''.join(characters)


