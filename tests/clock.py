import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_SIZE = 500
TITLE = "BALL BOUNCE"
CENTER_X = 100
CENTER_Y = 100
REACHED = False
ANGLE = math.pi/2
HOUR_ANGLE = math.pi/2
MIN_ANGLE = math.pi/2


def init(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200,width,-200,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def polarCircle(r,xc,yc):
    points=[]
    theta=0
    while theta<=6.28:
        x = xc+r*math.cos(theta)
        y = yc+r*math.sin(theta)
        points.append([x,y])
        theta += (1/r)
    return  points

    return points

def draw():
    global CENTER_X
    global CENTER_Y
    global REACHED
    global ANGLE
    global HOUR_ANGLE
    global MIN_ANGLE
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    points = polarCircle(150,CENTER_X,CENTER_Y)
    glColor3f(1,0,1)
    for p in points:
        glBegin(GL_POINTS)
        glVertex2f(p[0],p[1])
        glEnd()

    glPointSize(5)
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(CENTER_X, CENTER_Y)
    glEnd()

    # second handle
    x = CENTER_X + 150 * math.cos(-ANGLE)
    y = CENTER_Y + 150 * math.sin(-ANGLE)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(CENTER_X, CENTER_Y)
    glVertex2f(x,y)
    glEnd()

    # min handle
    x = CENTER_X + 150 * math.cos(-MIN_ANGLE)
    y = CENTER_Y + 150 * math.sin(-MIN_ANGLE)
    glColor3f(0, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(CENTER_X, CENTER_Y)
    glVertex2f(x, y)
    glEnd()

    # hour handle
    x = CENTER_X + 150 * math.cos(-HOUR_ANGLE)
    y = CENTER_Y + 150 * math.sin(-HOUR_ANGLE)
    glColor3f(1, 1, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(CENTER_X, CENTER_Y)
    glVertex2f(x+50, y+50)
    glEnd()

    ANGLE +=( 6*(math.pi)/180)*(1/150)


    MIN_ANGLE+=(1/60)*(1/60)*(1/60)

    # if math.cos(-MIN_ANGLE)==math.cos(math.pi/2):
    #     HOUR_ANGLE +=(1/150)





    glutSwapBuffers()
def update(value):
    glutPostRedisplay()
    glutTimerFunc(500,update,0)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(TITLE)
    glutDisplayFunc(draw)
    init(WINDOW_SIZE, WINDOW_SIZE)
    glutIdleFunc(draw)
    glutTimerFunc(4000,update,0)
    glutMainLoop()



main()
