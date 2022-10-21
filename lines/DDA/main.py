from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title="DDA algorithm"
window =0
width , height = 500,400

def init(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw(x1,y1,x2,y2):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    init(width,height)
    glColor3f(1,1,0)
    glPointSize(12)
    ploat_line(x1,y1,x2,y2)
    glutSwapBuffers()




def ploat_line(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1

    steps = 0
    if(abs(dx)>abs(dy)):
        steps = dx
    else:
        steps = dy

    Xinc = dx/steps
    Yinc = dy/steps
    glBegin(GL_POINTS)   
    for step in range(1,steps):
        glVertex2f(x1,y1)
        x1=x1+Xinc
        y1=y1+Yinc 
    glEnd()

def main():
    print("Enter the first coordinate")
    x1 = int(input("Enter x1 here : "))
    y1 = int(input("Enter y1 here : "))
    print("Enter the last point coordinate")
    x2 = int(input("Enter x2 here : "))    
    y2 = int(input("Enter y2 here : "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    window = glutCreateWindow(title)
    glutDisplayFunc(lambda:draw(x1,y1,x2,y2))
    glutIdleFunc(lambda:draw(x1,y1,x2,y2))
    glutMainLoop()

main()

