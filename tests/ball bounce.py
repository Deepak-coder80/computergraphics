import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_SIZE = 500
TITLE = "BALL BOUNCE"
CENTER_X = 100
CENTER_Y = 100
REACHED = False

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
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(-100,450)
    glVertex2f(300,450)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-100, 50)
    glVertex2f(300, 50)
    glEnd()
    glBegin(GL_POINTS)
    glVertex2f(CENTER_X, CENTER_Y)
    glEnd()
    points = polarCircle(50,CENTER_X,CENTER_Y)
    glColor3f(1,0,0)
    for p in points:
        glBegin(GL_LINE_LOOP)
        glVertex2f(CENTER_X,CENTER_Y)
        glVertex2f(p[0],p[1])
        glEnd()
    if REACHED == False:
        if CENTER_Y ==400:
            REACHED=True
        elif CENTER_Y<400:
            CENTER_Y+=.5
    else:
        if CENTER_Y == 100:
            REACHED = False
        elif CENTER_Y>100:
            CENTER_Y-=0.5

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
