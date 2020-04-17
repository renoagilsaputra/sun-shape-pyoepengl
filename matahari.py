from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def plotpoints():
    glColor3f(1.,1.0,0.)
    # digunakan untuk membuar perulangan 0 - 18
    # dimana segitiga akan terbentuk sebanyak 18 kali
    # dengan rotasi sudut kelipatan 20
    # Note : jika ingin membuat looping dari 0 - 18 harus dilebihkan 1 menjadi 0 -19
    for i in range(0,19):
        s = 20
        glRotatef(s, 0.0, 0.0,1.0)
        segitiga()        

    glFlush()

# Fungsi untuk menggambar bentuk segitiga
def segitiga():
    # Jika ingin mengubah ke bentuk segitiga garis
    # ganti dengan glBegin(GL_LINE_LOOP)
    glBegin(GL_TRIANGLES)
    glVertex2f(-50.0,0.0)
    glVertex2f(50.0,0.0)
    glVertex2f(0.0,200.0)
    glEnd()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Matahari")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()
    
main()