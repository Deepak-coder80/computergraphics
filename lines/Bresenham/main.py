from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title="Breseham algorithm"
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
    x = x1;
    y=y1;
    dx = x2-x1
    dy = y2-y1
    p = (2*dy)-dx
    glBegin(GL_POINTS)  
    if dx>dy: 
        while x<=x2:
            glVertex2f(x,y)
            x = x+1
            if p<0:
                p = p+(2*dy)
            else:
                p= p+((2*dy)-2*dx)
                y=y+1
    else:
        while y<=y2:
            glVertex2f(x,y)
            y = y+1
            if p<0:
                p = p+(2*dx)
            else:
                p= p+((2*dx)-2*dy)
                x=x+1
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

