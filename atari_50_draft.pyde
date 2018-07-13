xCoord = 450
yCoord = 150
speed=2
ySpeed=2
sizeEllipse= 50
sizeRectX= 125
sizeRectY= 100
inBox0 = (xCoord >= 0 and yCoord <= 100 and xCoord <= 125) == True
inBox1 = (xCoord >= 125 and yCoord <= 100 and xCoord <= 250) == True
inBox2 = (xCoord >= 250 and yCoord <= 100 and xCoord <= 375) == True
inBox3 = (xCoord >= 375 and yCoord <= 100 and xCoord <= 500) == True
inBox4 = (xCoord >= 500 and yCoord <= 100 and xCoord <= 125) == True
inBox0 = False 
def setup():
    size(625, 600)
    background(0)

def draw():
    background(0, 255, 160)
    global xCoord, speed, ellipseSize, yCoord, ySpeed, inBox0
    leftTopBoundary  = sizeEllipse /2
    rightBottomBoundary = 600 - sizeEllipse / 2
    if xCoord >= rightBottomBoundary or xCoord <= leftTopBoundary:
        speed = -speed
    if yCoord >= rightBottomBoundary or yCoord <= leftTopBoundary:
       ySpeed = -ySpeed
    xCoord += speed
    yCoord += ySpeed
    fill(255, 255, 0)
    ellipse(xCoord, yCoord, sizeEllipse, sizeEllipse)
    
    fill(0)
    if inBox0 == True:
        if inBox0 == False:
            noStroke()
            fill(0, 255, 160)
    rect(0, 0, sizeRectX, sizeRectY)
    
    fill(255)
    if inBox1 == False:
        if inBox1 == True:
            noStroke()
            fill(0, 255, 160)
    rect(125, 0, sizeRectX, sizeRectY)
    fill(0)
    
    rect(250, 0, sizeRectX, sizeRectY)
    fill(255)
    
    rect(375, 0, sizeRectX, sizeRectY)
    fill(0)
    
    rect(500, 0, sizeRectX, sizeRectY)
    
    if inBox0 == True:
        if inBox0 == False:
            noStroke()
            fill(0)
    if inBox1 == True:
        if inBox1 == False:
            noStroke()
            fill(0)
    if inBox2 == True:
        if inBox2 == False:
            noStroke()
            fill(0)
    if inBox3 == True:
        if inBox3 == False:
            noStroke()
            fill(0)
    if inBox4 == True:
        if inBox4 == False:
            noStroke()
            fill(0)
