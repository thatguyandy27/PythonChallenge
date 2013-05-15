# -*- coding: utf-8 *-*
import webbrowser


baseUrl = 'http://www.pythonchallenge.com/pc/def/'


def challenge1():
    challenge2Url = baseUrl
    nextPage = 2 ** 38  # math.pow(2, 38)

    challenge2Url += str(nextPage) + '.html'
    print challenge2Url

    webbrowser.open(challenge2Url)


if __name__ == '__main__':
    challenge1()
