import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_SIZE = 500
TITLE = "BALL BOUNCE"
CENTER_X = 0
CENTER_Y = 0
REACHED = False
ANGLE = math.pi/2
HOUR_ANGLE = math.pi/2
MIN_ANGLE = math.pi/2
ITERATOR_I=0


def init(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500,width,-500,height,0,1)
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
    global ITERATOR_I
    sun = polarCircle(50,CENTER_X,CENTER_Y)
    glColor3f(1,1,0)
    for s in sun:
        glBegin(GL_LINE_LOOP)
        glVertex2f(CENTER_X,CENTER_Y)
        glVertex2f(s[0],s[1])
        glEnd()

    orbit1 = polarCircle(200,CENTER_X,CENTER_Y)
    glColor3f(1,1,1)
    for r in orbit1:
        glBegin(GL_POINTS)
        glVertex2f(r[0],r[1])
        glEnd()

    earth_center =[orbit1[ITERATOR_I][0],orbit1[ITERATOR_I][1]]

    earth = polarCircle(20,int(earth_center[0]),int(earth_center[1]))
    glColor3f(0,0,1)
    for e in earth:
        glColor3f(0, 0, 1)
        glBegin(GL_LINE_LOOP)
        glVertex2f(earth_center[0],earth_center[1])
        glVertex2f(e[0],e[1])
        glEnd()
        glColor3f(0,1,0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(earth_center[0], earth_center[1])
        glVertex2f(e[0], e[1])
        glEnd()

    if ITERATOR_I < len(orbit1):
        ITERATOR_I += 1
    else:
        ITERATOR_I=0


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
