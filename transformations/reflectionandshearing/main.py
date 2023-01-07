from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

title = "Shearing and Reflection"
width,height=1000,900

#refersh screen to 2d
def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-450,width,-450,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def screen():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    refresh2D(width,height)
    glLoadIdentity()

def initDisplay():
    glutInit(sys.argv)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(title)


def plot_x_axis():
    glBegin(GL_LINES)
    glVertex2f(-250,0)
    glVertex2f(790,0)
    glEnd()
    display_text(820,0,'X AXIS')

def plot_y_axis():
    glBegin(GL_LINES)
    glVertex2f(0,-250)
    glVertex2f(0,790)
    glEnd()
    display_text(0,820,'Y AXIS')


def display_text(x,y,text):
    glRasterPos(x,y)
    for i in range(len(text)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(text[i]))

def draw():
    screen()   
    glColor3f(1,1,1)
    glLineWidth(6)
    plot_x_axis()
    plot_y_axis()
    glutSwapBuffers()


def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()


def shear(x,y,sh,ref):
    return (x+sh*(y-ref))

def neg_value(x):
    return (-x)

def reflect_x_axis(x1, y1, x2, y2, x3, y3):
    screen()   
    glColor3f(1,1,1)
    glLineWidth(6)
    plot_x_axis()
    glColor3f(1,1,1)
    plot_y_axis()
    glColor3f(1,0,0)
    draw_triangle(x1, y1, x2, y2, x3, y3)
    glColor3f(0,1,0)
    # #about x axis
    # draw_triangle(x1,neg_value(y1),x2,neg_value(y2),x3,neg_value(y3))
    # glColor3f(0,0,1)
    # #about y axis
    # draw_triangle(neg_value(x1),y1,neg_value(x2),y2,neg_value(x3),y3)
    # glColor3f(1,1,0)
    # #about orgin
    # draw_triangle(neg_value(x1),neg_value(y1),neg_value(x2),neg_value(y2),neg_value(x3),neg_value(y3))
    # #about y = x
    # glColor3f(1,1,1)
    # draw_triangle(y1,x1,y2,x2,y3,x3)

    # x shearing
    draw_triangle(shear(x1,y1,0.5,0),y1,shear(x2,y2,0.5,0),y2,shear(x2,y2,0.5,0),y3)
    glColor3f(0,0,1)
    draw_triangle(x1,shear(y1,x1,0.5,0),x2,shear(y2,x2,0.5,0),x3,shear(y3,x3,0.5,0))
    glutSwapBuffers()

def main():
    initDisplay()
    glutDisplayFunc(lambda:reflect_x_axis(100,100,400,100,250,300))
    glutMainLoop()

main()