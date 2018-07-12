xCoordinate = 150
yCoordinate = 50
speed=2
ySpeed=2
ellipseSize= 50
def setup():
    size(600, 600)
    background(0)

def draw():
    background(0, 255, 160)
    global xCoordinate, speed, ellipseSize, yCoordinate, ySpeed
    leftTopBoundary  = ellipseSize /2
    rightBottomBoundary = 600 - ellipseSize / 2
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
       ySpeed = -ySpeed
    xCoordinate += speed
    yCoordinate += ySpeed
    fill(255, 255, 0)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
    
    
