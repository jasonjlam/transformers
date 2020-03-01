from graphics import *
from matrix import *
import math

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parseFile( fname, points, transform, screen, color ):
    fd = open(fname, "r")
    lines = fd.readlines()
    lines = list(map(str.rstrip,lines))
    print(lines)
    for i in range(0, len(lines)):
        if lines[i] == "line":
            print("line")
            args = lines[i+1].split(" ")
            addEdge(points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]))
        elif lines[i] == "ident":
            print ("ident")
            transform = identity(transform)
        elif lines[i] == "scale":
            args = lines[i+1].split(" ")
            print ("scale")
            print(args)
            printMatrix(transform)
            printMatrix(scaleMatrix(float(args[0]), float(args[1]), float(args[2])))
            matrixMulti(scaleMatrix(float(args[0]), float(args[1]), float(args[2])), transform)
        elif lines[i] == "move":
            print ("move")
            args = lines[i+1].split(" ")
            matrixMulti(translateMatrix(float(args[0]), float(args[1]), float(args[2])),transform)
        elif lines[i] == "rotate":
            args = lines[i+1].split(" ")
            matrixMulti(rotateMatrix(args[0], float(args[1])), transform)
        elif lines[i] == "apply":
            print("apply")
            clearpixels()
            printMatrix(transform)
            printMatrix(points)
            matrixMulti(transform, points)
            for i in range(0, len(points)):
                for x in range(0, len(points[i])):
                    points[i][x] = int(points[i][x])
            printMatrix(points)
            drawEdges(points, color)
        elif lines[i] == "display":
            display()
        elif lines[i] == "save":
            args = lines[i+1].split(" ")
            saveExtension(args[0])
        elif lines[i] == "quit":
            return
