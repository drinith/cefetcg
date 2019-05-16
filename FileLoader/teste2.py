from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


def MTL(filename):
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise ValueError("mtl file doesn't start with newmtl stmt")
        elif values[0] == 'map_Kd':
            pass
        else:
            mtl[values[0]] = list(map(float, values[1:]))
    return contents
  
class PLY:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.quantidadeVertices=1
        self.quantidadeFaces=1
        countVertices=0
        countFaces=0
        cComecoVertices=False
        cComecoFaces=False
        material = None
        
        for line in open(filename, "r"):
            if line.startswith('PLY'): continue
            values = line.split()
            if not values: continue
            
            if(values[0]=="element" and values[1]=="vertex" ):
                self.quantidadeVertices=int(values[2])-1
            if(values[0]=="element" and values[1]=="face" ):
                self.quantidadeFaces=int(values[2])-1
            
            if(values[0]=="end_header"):
                cComecoVertices=True
            #preenchendo os valores do vertices
            if(values[0]!="end_header" and cComecoVertices==True and countVertices <= self.quantidadeVertices):
                countVertices+=1
                v = list(map(float, values[0:3]))
                
                if swapyz:
                    v = v[0], v[2], v[1]
                    
                self.vertices.append(v)
            
            if (self.quantidadeVertices<=countVertices):
                cComecoFaces=True

            if(values[0]=="3" and cComecoFaces==True and countFaces<=self.quantidadeFaces):
                countFaces+=1
                face = []
               
                self.faces.append([int(values[1]),int(values[2]),int(values[3])])
  
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glFrontFace(GL_CCW)
        glBegin(GL_POLYGON)
        for face in self.faces:
            #vertices, normals, texture_coords, material = face
       
            glNormal3fv(self.calculaNormalFace(face))
                
            for vertex in face:
                glVertex3fv(self.vertices[vertex])
  
        glEnd()    
        glDisable(GL_TEXTURE_2D)
        glEndList()

    def calculaNormalFace(self,face):
        x = 0
        y = 1
        z = 2
        v0 = self.vertices[face[0]]
        v1 = self.vertices[face[1]]
        v2 = self.vertices[face[2]]
        U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
        V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
        N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
        NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
        return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def display():
    global ply
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    glCallList(ply.gl_list)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,1,0,0,0,0,1,0)

def init():
    global ply

    glLightfv(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.4, 0.4, 0.4, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.6, 0.6, 0.6, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(1.0,1.0,1.0,0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
    ply = PLY("bun_zipper_res4.ply")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("PLY")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()


