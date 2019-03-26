from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)
    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)
    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()
    
def drawCircle(r=.1,xc=0,yc=0,zc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange (0,2*pi,.001):
        xx=r*cos(theta)
        yy=r*sin(theta)
        glColor3f(1, 1,0)
        glVertex3f(xx+xc,yy+yc,zc)

    glEnd()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 50)
    gluLookAt(8, 16, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(1, 1, 1, 1)


angle = 0
x = 0
forward = True
car_z=0


def arrows(key,x,y):
    global car_z
    if (key==GLUT_KEY_LEFT):
        car_z+=.5
    elif (key==GLUT_KEY_RIGHT):
        car_z -=.5
    draw()
def draw():
    global angle
    global x
    global forward
    global car_z

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

     ###ROAD####
    glColor(.3, .3, .3)
    glBegin(GL_POLYGON)
    glVertex(35, 0, 5)
    glVertex(35, 0, -5)
    glVertex(-35, 0, -5)
    glVertex(-35, 0, 5)
    glEnd()
    glLoadIdentity()

    #grass
    glColor(138/255, 229/255, 25/255)
    glBegin(GL_QUADS)
    
    glVertex(35, 0, 5)
    glVertex(-35, 0, 5)
    glVertex(-35, 0, 35)
    glVertex(-35, 0, 35)

    glVertex(35, 0, -5)
    glVertex(-35, 0, -5)
    glVertex(-35, 0, -70)
    glVertex(35, 0, -70)
    glEnd()

    #Pine Trees
    
    glTranslate(-1,3,-15)
    glRotate(180,1,0,0)
    glScale(.015,.02,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()
#################
    glTranslate(-12,3,-15)
    glRotate(180,1,0,0)
    glScale(.015,.02,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()
##########
    glTranslate(-23,3,-15)
    glRotate(180,1,0,0)
    glScale(.015,.02,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()
##########
    glTranslate(-36,3,-15)
    glRotate(180,1,0,0)
    glScale(.015,.02,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()
#######
    glTranslate(-1,3,5)
    glRotate(180,1,0,0)
    glScale(.015,.05,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()
    ##########
    glTranslate(-6,3,5)
    glRotate(170,1,0,0)
    glScale(.013,.02,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()

#########
    glTranslate(-16,2,4.5)
    glRotate(170,1,0,0)
    glScale(.014,.022,.02)
    glColor(58/255,181/255,74/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(300,0,0)
    glVertex(180,120,0)
    glVertex(240,120,0)
    glVertex(120,240,0)
    glVertex(180,240,0)
    glVertex(60,360,0)
    glVertex(120,360,0)
    glVertex(0,480,0)
    glVertex(600,480,0)
    glVertex(480,360,0)
    glVertex(540,360,0)
    glVertex(420,240,0)
    glVertex(480,240,0)
    glVertex(350,120,0)
    glVertex(420,120,0)
    glVertex(300,0,0)
    glEnd()
    
    glColor(163/255,95/255,44/255)
    glBegin(GL_QUADS)
    glVertex(240,480,0)
    glVertex(360,480,0)
    glVertex(360,600,0)
    glVertex(240,600,0)
    glEnd()
    glLoadIdentity()
 
    #draw_XYZ()
    
    #Car Body
    glColor3f(1, 0, 0)
    glTranslate(x, 0, car_z)
    glScale(1, 0.25, 0.5)
    glutWireCube(5)
    glLoadIdentity()
    
    glTranslate(x, 5*0.25, car_z)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)
    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)
    glLoadIdentity()
    
    glTranslate(x+0.5*5, -0.5 * 0.25*5, - 0.5 * 0.5*5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)
    glLoadIdentity()
    
    glTranslate(x-0.5*5, -0.5 * 0.25*5, -0.5 * 0.5*5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)
    glLoadIdentity()
    
    glTranslate(x-0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)
    glLoadIdentity()

    #Head Lights#
    glColor(1,1,0)
    glTranslate(x+2.5,0,.8+car_z)
    glutSolidSphere(.15,100,100)
    glLoadIdentity()
    glTranslate(x+2.5,0,-.8+car_z)
    glutSolidSphere(.15,100,100)
    glLoadIdentity()

    glutSwapBuffers()

    if forward:
        angle -= 0.1
        x += 0.005
        if x > 5:
            forward = False
    else:
        
        angle += 0.1
        x -= 0.005
        if x < -5:
            forward = True


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutSpecialFunc(arrows)
glutIdleFunc(draw)
glutMainLoop()
