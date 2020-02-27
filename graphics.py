import array
import math
from matrix import *
pixels = [0]
w = 0
h = 0
header = ""

def createPixels(width, height, maxval):
    global pixels
    global w
    global h
    global header
    pixels = array.array('B', [255, 255, 255] * width * height)
    w  = width
    h = height
    header = "P3 " + str(w) + " "+ str(h) + " " + str(maxval) + "\n"

def writeImage(path):
    fd = open(path, 'w')
    print ("Writing image...")
    fd.write(header)
    for pixel in pixels:
        fd.write(str(pixel) + " ")
    fd.close()

def clearpixels():
    global pixels
    for pixel in pixels:
        pixel = 255;

def colorPixel (x, y, color):
    index = (w * y + x) * 3
    global pixels
    pixels[index] = color[0]
    pixels[index + 1] = color[1]
    pixels[index + 2] = color[2]

def getPixel(x,y):
    index = (w * y + x) * 3
    global pixels
    return [pixels[index], pixels[index + 1], pixels[index + 2]]

def drawLine (p0, p1, color):
    x0 = p0[0] % w
    x1 = p1[0] % w
    y0 = p0[1] % h
    y1 = p1[1] % h
    print("plotting line {},{} to {},{}".format(x0, y0, x1, y1))
    a = y1-y0
    b = x1-x0
    if abs(a) < abs (b):
        if x0 > x1:
            drawLine([x1, y1], [x0, y0], color)
            # print ("swapped 1,2")
        else:
            i = 1
            y = y0
            # print ("slope{}".format(slope))
            if a < 0:
                i = -1
                a *= -1
            d = 2 * a - b
            for x in range (x0,x1 + 1):
                colorPixel(x, y, color)
                # print("drew {}, {}".format(x,y))
                if d > 0:
                    d -= 2 * b
                    if a > 0:
                        y +=i
                    else:
                        y -=i
                d += 2 * a
    else:
        if y0 > y1:
            drawLine([x1, y1], [x0, y0], color)
        else:
            x = x0
            # print ("slope{}".format(slope))
            i = 1
            if b < 0:
                i = -1
                b *= -1
            d = 2 * b - a
            for y in range (y0,y1 + 1):
                colorPixel(x, y, color)
                # print("drew {}, {}".format(x,y))
                if d > 0:
                    d -= 2 * a
                    if b > 0:
                        x +=i
                    else :
                        x -=i
                d += 2 * b

def addEdge ( matrix, x0, y0, z0, x1, y1, z1 ):
    addPoint(matrix, x0, y0, z0)
    addPoint(matrix, x1, y1, z1)
# def fillColor(color):
#     for i in range(0, w * h):
#         if getPixel()

def drawEdges(matrix, color):
    for i in range(0, int(math.floor(len(matrix))/2 - 1)):
        drawLine([matrix[i*2][0], matrix[i*2][1]], [matrix[i*2 + 1][0], matrix[i*2 +1][1]], color)

def saveExtension( pixels, fname ):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm_ascii( pixels, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( pixels ):
    ppm_name = 'pic.ppm'
    save_ppm_ascii( pixels, ppm_name )
    p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

# .tofile(fd)
