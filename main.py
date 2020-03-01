from parse import *
from matrix import *
from graphics import *
import random

s = scaleMatrix(1,2,3)
print(len(s))
printMatrix(s)
points = newMatrix(4,0)
printMatrix(translateMatrix(100,200,300))
transform = identity(newMatrix())
color = [255, 0, 255]
createPixels(1000, 1000, 255)
printMatrix(transform)
parseFile( "script", points, transform, pixels, color )
