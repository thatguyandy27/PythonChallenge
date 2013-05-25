# -*- coding: utf-8 -*-
import Image
im = Image.open("oxygen.png")
print "Image info:",im.format, im.size, im.mode

#we'll limit the grey zone
y_begin = 0
while True:
    p = im.getpixel((0, y_begin))
    if p[0] == p[1] == p[2]:
        break
    y_begin += 1
x_end = 0
while True:
    p = im.getpixel((x_end, y_begin))
    if not p[0] == p[1] == p[2]:
        break
    x_end += 1
print "Y first coordinate:", y_begin,"nX last coordinate:",x_end

message=[]
for i in range(0,x_end,7):
    p = im.getpixel((i, y_begin))
    message.append(chr(p[0]))
print ''.join(message),
#First run gives: [105, 110, 116, 101, 103, 114, 105, 116, 121]
message=[105, 110, 116, 101, 103, 114, 105, 116, 121]
print '(',''.join([chr(x) for x in message]),')'