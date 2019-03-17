from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 0, 0)  
    glTranslate(-.3,-0.02,0)
    
    #FACE
    glColor3f(0, 0, 0) 
    glBegin(GL_QUADS)
    glVertex(0,.2,0)
    glVertex(0,.55,0)
    glVertex(.6,.55,0)
    glVertex(.6,.2,0)
    glEnd()

    #LEFT EAR
    glColor(0.0, 0.0, 0.0) 
    glBegin(GL_TRIANGLES)
    glVertex(0, .55, 0)
    glVertex(.15,.8,0)
    glVertex(.3, .55, 0)
    glEnd()

    #RIGHT EAR
    glColor(0.0, 0.0, 0.0) 
    glBegin(GL_TRIANGLES)
    glVertex(.3, .55, 0)
    glVertex(.45, .8, 0)
    glVertex(.6,.55,0)
    glEnd()

    #RIGHT EYE
    glColor(1, 1, 1) 
    glBegin(GL_TRIANGLES)
    glVertex(.35, .35, 0)
    glVertex(.5, .5, 0)
    glVertex(.55,.35,0)
    glEnd()

    #RIGHT EYE
    glColor(1, 1, 1) 
    glBegin(GL_TRIANGLES)
    glVertex(.05, .35, 0)
    glVertex(.1, .5, 0)
    glVertex(.25,.35,0)
    glEnd()

    #chin
    glScalef(.9,.5,1)
    glTranslatef(0.03,-.15,0)
    glColor3f(212/255, 212/255, 146/255)
    glBegin(GL_QUADS)
    glVertex(0,.2,0)
    glVertex(0,.55,0)
    glVertex(.6,.55,0)
    glVertex(.6,.2,0)
    glEnd()

    #RIGHT EYE
    glRotatef(-10,0,0,1)
    glTranslatef(-.09,.3,0)
    glColor(1, 1, 1) 
    glBegin(GL_POLYGON)
    glVertex(.45, .20, 0)
    glVertex(.15, .15, 0)
    glVertex(.15,.11,0)
    glVertex(.45,.08,0)
    glEnd()
    
    glLoadIdentity()

    #WINGS
    glColor(60/255,78/255,78/255)
    glBegin(GL_POLYGON)
    glVertex(.3,-0.1,0)
    glVertex(-.3,-.1,0)
    glVertex(-1,-1,0)
    glVertex(1,-1,0)
    glEnd()

    glLoadIdentity()# NECk
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(.15,0,0)
    glVertex(.15,-.08,0)
    glVertex(-.15,-.08,0)
    glVertex(-.15,.0,0)
    glEnd()
    

    glColor(0,0,0) #shirt
    glBegin(GL_POLYGON)
    glVertex(-.3,-.08,0)
    glVertex(.3,-.08,0)
    glVertex(.3,-1,0)
    glVertex(-.3,-1,0)
    glEnd()

    glPointSize(5) #BUTTONS
    glColor(1,1,0)
    glBegin(GL_POINTS)
    glVertex(0,-.2,0)
    glVertex(0,-.3,0)
    glVertex(0,-.4,0)
    glEnd()
    
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Lab2 - Equation Program")
glutDisplayFunc(draw)
glutMainLoop()
