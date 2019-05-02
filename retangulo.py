from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

def retanguloaCilindro():
    
    lado = 200
    
    glBegin(GL_LINE_LOOP)#Desenhando a Base da pilastra
        
    glColor3f(1,1,0)
    #glColor3fv(cores[vertex])
    #Desenhar cada vertice
    
    glVertex3f(0.5 ,-1,0.5)
    glVertex3f(0.5 ,-1,-0.5)
    glVertex3f(-0.5 ,-1,-0.5)
    glVertex3f(-0.5 ,-1,0.5)
       
      
    glEnd()

      
    glBegin(GL_LINE_LOOP)#Desenhando o Topo da pilastra
        
    glColor3f(1,1,0)
    #glColor3fv(cores[vertex])
    #Desenhar cada vertice
    glVertex3f(0.5 ,1,0.5)
    glVertex3f(0.5 ,1,-0.5)
    glVertex3f(-0.5 ,1,-0.5)
    glVertex3f(-0.5 ,1,0.5)
        
      
    glEnd()

    
    
            
    glBegin(GL_LINE_LOOP)
            
    glColor3f(1,1,0)
    glVertex3f(0.5 ,-1,0.5)
    glVertex3f(0.5 ,1,0.5)
    glVertex3f(-0.5 ,1,0.5)
    glVertex3f(-0.5 ,-1,0.5)        
        
        
    glEnd()

    glBegin(GL_LINE_LOOP)
            
    glColor3f(1,1,0)
    glVertex3f(0.5 ,-1,-0.5)
    glVertex3f(0.5 ,1,-0.5)
    glVertex3f(-0.5 ,1,-0.5)
    glVertex3f(-0.5 ,-1,-0.5)        
        
        
    glEnd()

    glBegin(GL_LINE_LOOP)
            
    glColor3f(1,1,0)
    glVertex3f(-0.5 ,-1,-0.5)
    glVertex3f(-0.5 ,1,-0.5)
    glVertex3f(-0.5 ,1,0.5)
    glVertex3f(-0.5 ,-1,0.5)        
        
        
    glEnd()

    glBegin(GL_LINE_LOOP)
            
    glColor3f(1,1,0)
    glVertex3f(0.5 ,-1,0.5)
    glVertex3f(0.5 ,1,0.5)
    glVertex3f(0.5 ,1,-0.5)
    glVertex3f(0.5 ,-1,-0.5)        
        
        
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
    retanguloaCilindro()
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
