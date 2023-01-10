from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

sys.setrecursionlimit(10**6)

title = "2D animation"
width,height=500,500

def refresh2d(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

x_pos = 10.0

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(x_pos,x_pos+40)
    glVertex2f(x_pos+40,x_pos+40)
    glVertex2f(x_pos+40,x_pos+70)
    glVertex2f(x_pos,x_pos+70)
    glEnd()
    
    glutSwapBuffers()

def timer(a):
    glutPostRedisplay()
    glutTimerFunc(1000/60,timer(0),a)

    if x_pos<450:
        x_pos += 40


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(title)
    glutDisplayFunc(display)
    glutReshapeFunc(lambda:refresh2d(width,height))
    glutTimerFunc(1000,timer(0),0)
    glutMainLoop()

main()