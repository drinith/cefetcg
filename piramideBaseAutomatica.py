#!/usr/bin/python
# -*- coding: "UTF-8" -*-

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

def pirameaCone():
    
    lado = 20
    
    glBegin(GL_LINE_LOOP)#Desenhado a base quadrado
        
    glColor3f(1,1,0)
    #glColor3fv(cores[vertex])
    #Desenhar cada vertice
    for i in range(lado):
        glVertex3f(cos(2*pi*i/lado) ,-1,sin(2*pi*i/lado))
        
      
    glEnd()

    
    for i in range(lado):#numero de lados
            
        glBegin(GL_LINE_LOOP)
            
        glColor3f(1,1,0)
        #glColor3fv(cores[vertex])
        #Desenhar cada vertice
        glVertex3f(0,1,0)#não muda
        glVertex3f(cos(2*pi*i/lado) ,-1,sin(2*pi*i/lado))# será i 
        glVertex3f(cos(2*pi*(i+1)/lado), -1,sin(2*pi*(i+1)/lado))#será i +1
        
        glEnd()

        
   

    # glBegin(GL_TRIANGLE_FAN)
        
    # glColor3f(1,1,0)
    # #glColor3fv(cores[vertex])
    # #Desenhar cada vertice
    # glVertex3f(0,1,0)
    # glVertex3f(-1,0,1)
    # glVertex3f(1,0,1)
    # glVertex3f(1,0,-1)
    # glVertex3f(-1,0,-1)
    # glVertex3f(-1,0,1)
      
    #glEnd()

    # glColor3fv((0,0.5,0))
    # glBegin(GL_LINES)
    # for linha in linhas:
    #     for vertice in linha:
    #         glVertex3fv(vertices[vertice])
    # glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    pirameaCone()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
