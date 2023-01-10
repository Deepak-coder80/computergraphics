from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title = "Draw Line"
width,height = 500,400
window =0

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2D(width,height)
    glColor3f(1,1,1)
    glLineWidth(12)
    glPointSize(12)
    ploat_line()
    glutSwapBuffers()

def ploat_line():
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glVertex2f(100,100)
    glVertex2f(200,300)
    glEnd()

def draw_rect(x,y,width,height):
    glBegin(GL_POLYGON)
    glVertex2f(x,y)
    glVertex2f(x+width,y)
    glVertex2f(x+width,y+height)
    glVertex2f(x,y+height)
    glVertex2f(x+width+50,y)
    glEnd()

def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(100,100)
    window = glutCreateWindow(title)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
main()