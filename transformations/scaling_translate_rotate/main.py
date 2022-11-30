from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

title = "2D transfomation"
width, height = 1000, 900
window = 0

# make window to perform 2d operations
def refresh2D(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, width, -300, height, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
# draw the x axis


def plot_x_axis():
    glBegin(GL_LINES)
    glVertex2f(-250, 0)
    glVertex2f(600, 0)
    glEnd()
    display_text(620, 0, 'X axis')
# draw the y axis


def plot_y_axis():
    glBegin(GL_LINES)
    glVertex2f(0, -250)
    glVertex2f(0, 600)
    glEnd()
    display_text(0, 620, 'Y axis')
# display text to screen


def display_text(x, y, text):
    glRasterPos2f(x, y)
    glColor3f(1, 1, 1)
    for i in range(len(text)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))
# display initialization


def init_display():
    glutInit(sys.argv)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(width, height)
    glutCreateWindow(title)
# triangle drawing function


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
# to clear the screen


def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    refresh2D(width, height)
# scaling


def new_scale(x, sx, xr):
    return (((x-xr)*sx)+xr)
# to draw orginal and scaled triangle


def scale_triangle(x1, y1, x2, y2, x3, y3, sx, sy, xr, yr):
    screen()
    glColor3f(1, 1, 1)
    plot_x_axis()
    glColor3f(1, 1, 1)
    plot_y_axis()
    glColor3f(1, 0, 0)
    draw_triangle(x1, y1, x2, y2, x3, y3)
    glColor3f(0, 1, 0)
    draw_triangle(new_scale(x1, sx, xr), new_scale(y1, sy, yr), new_scale(
        x2, sx, xr), new_scale(y2, sy, yr), new_scale(x3, sx, xr), new_scale(y3, sy, yr))
    glutSwapBuffers()

# Translating


def translate(x, t):
    return x+t

# draw original and translate function
def translate_triangle(x1, y1, x2, y2, x3, y3, tx, ty):
    screen()
    glColor3f(1, 1, 1)
    plot_x_axis()
    glColor3f(1, 1, 1)
    plot_y_axis()
    glColor3f(1, 0, 0)
    draw_triangle(x1, y1, x2, y2, x3, y3)
    glColor3f(0, 1, 0)
    draw_triangle(translate(x1, tx), translate(y1, ty), translate(
        x2, tx), translate(y2, ty), translate(x3, tx), translate(y3, ty))
    glutSwapBuffers()

# rotation new x
def rot_new_x(x,y,theta):
    theta = theta*(3.14/180)
    return (x*math.cos(theta)-y*math.sin(theta))
# rotation new y
def rot_new_y(x,y,theta):
    theta = theta*(3.14/180)
    return (x*math.sin(theta)+y*math.cos(theta))
# draw rotate new and old triangle
def rotate_triangle(x1,y1,x2,y2,x3,y3,theta,xr,yr):
    screen()
    glLineWidth(5)
    glColor3f(1, 1, 1)
    plot_x_axis()
    glColor3f(1, 1, 1)
    plot_y_axis()
    glColor3f(1, 0, 0)
    draw_triangle(x1, y1, x2, y2, x3, y3)
    glColor3f(0, 1, 0)
    draw_triangle(rot_new_x(x1-xr,y1-yr,theta)+xr,rot_new_y(x1-xr,y1-yr,theta)+yr,
                rot_new_x(x2-xr,y2-yr,theta)+xr,rot_new_y(x2-xr,y2-yr,theta)+yr,
                rot_new_x(x3-xr,y3-yr,theta)+xr,rot_new_y(x3-xr,y3-yr,theta)+yr)
    glutSwapBuffers()
# main function
def main():
    x1 = int(input("Enter x1 coordinate : "))
    y1 = int(input("Enter y1 coordinate : "))
    x2 = int(input("Enter x2 coordinate : "))
    y2 = int(input("Enter y2 coordinate : "))
    x3 = int(input("Enter x3 coordinate : "))
    y3 = int(input("Enter y3 coordinate : "))
    print("\nSelect one option to continue : ")
    choice = int(input(
        "\n\tEnter 1 for scaling\n\tEnter 2 for translate\n\tEnter 3 for rotation\nEnter your option here : "))
    if choice == 1:
        sx = float(input("Enter sx : "))
        sy = float(input("Enter sy : "))
        xr = int(input("Enter xr coordinate : "))
        yr = int(input("Enter yr coordinate : "))
        init_display()
        glutDisplayFunc(lambda: scale_triangle(
            x1, y1, x2, y2, x3, y3, sx, sy, xr, yr))
        glutMainLoop()
    elif choice == 2:
        tx = float(input("Enter tx : "))
        ty = int(input("Enter ty : "))
        init_display()
        glutDisplayFunc(lambda: translate_triangle(x1, y1, x2, y2, x3, y3, tx, ty))
        glutMainLoop()
    elif choice == 3:
        theta = float(input("Enter angle : "))
        xr = int(input("Enter xr coordinate : "))
        yr = int(input("Enter yr coordinate : "))
        init_display()
        glutDisplayFunc(lambda: rotate_triangle(x1,y1,x2,y2,x3,y3,theta,xr,yr))
        glutMainLoop()
    else:
        print("INVALID OPTION")


main()
