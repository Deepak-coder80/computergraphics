from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from playsound import playsound
import math
import sys
import random

WINDOW_SIZE=200

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)


def glutFunct():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("MOVE THE CAR")
    init()


def polarCircle(r, xc, yc):

    xPoints = []
    yPoints = []
    pi = math.pi

    # The code for polar circle algorithm begins here
    for i in range(45):
        x = r * math.cos(pi/180*i)
        y = r * math.sin(pi/180*i)

        xPoints = xPoints + [x+xc, -x+xc, y +
                             xc, -y+xc, -y+xc, y+xc, -x+xc, x+xc]
        yPoints = yPoints + [y+yc, -y+yc, x +
                             yc, -x+yc, x+yc, -x+yc, y+yc, -y+yc]

    # The code for polar circle algorithm end here

    points = list(list())
    for i in range(len(xPoints)):
        points += [[xPoints[i], yPoints[i]]]

    return points


class Car:
    def __init__(self, point):
        self.refPoint = point       # the bottom left point of the car
        self.length = 75
        self.height = 45
        self.radius = self.length * 0.2
        self.angle = 40

    def drawCar(self):
        # Vertices of car body
        vertices = [
            [self.refPoint[0], self.refPoint[1]],
            [self.refPoint[0], self.refPoint[1] + self.height],
            [self.refPoint[0] + self.length*0.75, self.refPoint[1] + self.height],
            [self.refPoint[0] + self.length, self.refPoint[1] + self.height * 0.40],
            [self.refPoint[0] + self.length, self.refPoint[1]]
        ]

        # Centres of car tyres
        tyres = [
            [self.refPoint[0] + self.length * 0.20, self.refPoint[1]],
            [self.refPoint[0] + self.length * 0.80, self.refPoint[1]]
        ]

        glClear(GL_COLOR_BUFFER_BIT)
        glLineWidth(2.0)

        # Car body
        glBegin(GL_POLYGON)
        glColor3f(1,1,0)
        for i in vertices:
            glVertex2fv(i)

        glEnd()

        # Car tyres
        glBegin(GL_LINES)
        glColor3f(1,0,1)
        for i in tyres:
            points = polarCircle(self.radius, i[0], i[1])
            for p in points:
                glVertex2fv(p)

        glEnd()

        # inside line 
        x = self.radius * math.cos(math.pi/180*self.angle)+tyres[0][0]
        y = self.radius * math.sin(math.pi/180*self.angle)+tyres[0][1]
        glColor(1,0,0)
        glBegin(GL_LINES)
        glVertex2f(tyres[0][0],tyres[0][1])
        glVertex2f(x,y)
        glEnd()

        x = self.radius * math.cos(math.pi/180*self.angle)+tyres[1][0]
        y = self.radius * math.sin(math.pi/180*self.angle)+tyres[1][1]
        glColor(1,0,0)
        glBegin(GL_LINES)
        glVertex2f(tyres[1][0],tyres[1][1])
        glVertex2f(x,y)
        glEnd()
       


        glutSwapBuffers()

    def update(self, value,key,hor):

        self.movement(value,hor,key)
        self.updateSpark(key)
        glutPostRedisplay()

    def movement(self,value,hor,key):
        if key=='a':
            if self.refPoint[0]>-WINDOW_SIZE:
                if hor == 1:
                    self.refPoint[0] += value
                else:
                    self.refPoint[1] += value
            else: 
                self.refPoint[0]=100
        if key=='d' or key=='t':
            if self.refPoint[0]<=WINDOW_SIZE-100:
                if hor == 1:
                    self.refPoint[0] += value
                else:
                    self.refPoint[1] += value
            else: 
                self.refPoint[0]=-200
        if key=='w':
            if self.refPoint[1]<=WINDOW_SIZE-100:
                if hor == 1:
                    self.refPoint[0] += value
                else:
                    self.refPoint[1] += value
            else: 
                self.refPoint[1]=-150
        if key=='s':
            if self.refPoint[1]>-WINDOW_SIZE+30:
                if hor == 1:
                    self.refPoint[0] += value
                else:
                    self.refPoint[1] += value
            else: 
                self.refPoint[1]=150

    def updateSpark(self,key):
        if key == 'a':
            self.angle+=10
        elif key == 'd':
            self.angle -=10
        elif key == 't':
            self.angle -=30
        elif key == 'w':
            self.angle -= 50
        else :
            self.angle += 50

   

    def keyboard(self, key, x, y):

        key = key.decode()
        if key == 'd':
            self.update(1,'d',1)
        elif key == 'a':
            self.update(-1,'a',1)
        elif key == 'w':
            self.update(1,'w',0)
        elif key == 's':
            self.update(-1,'s',0)
        elif key == 't':
            self.update(3,'t',1)
        elif key == 'h':
            playsound('horn.mp3')
        elif key=='j':
            playsound('CarHorn.mp3')


def main():
    print("press:\n D to move forward ,\n A to move backward,\n W to move up ,\n S to move down ,\n T to move fast forward,\n H to Horn")
    car = Car([-200, -50])
    glutFunct()
    glutDisplayFunc(car.drawCar)
    glutKeyboardFunc(car.keyboard)
    glutIdleFunc(car.drawCar)
    glutMainLoop()


main()
