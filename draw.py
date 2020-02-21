"""
    Draw module
"""

# External imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Internal imports
from bresenham import bresenham


class Draw:
    """
        The draw class implements simple draw methods that makes a point, plot a line
        and draw a triangle. the last draw funtcions uses the bresenham algorithm as
        base to draw lines.
    """

    w, h = 500, 500
    x0, y0, x1, y1 = 0, 0, 0, 0
    triangle_points = []
    func = None

    def draw_line(self, *args):
        if args:
            x0, y0, x1, y1 = args
        else:
            x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1

        glBegin(GL_LINES)
        for point in bresenham(x0=x0, y0=y0, x1=x1, y1=y1):
            glVertex2f(*point)
        glEnd()

    def iterate(self):
        glViewport(0, 0, 500, 500)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()

    def showScreen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.iterate()
        glColor3f(1.0, 0.0, 3.0)
        self.func()

        glutSwapBuffers()

    def draw_triangle(self):
        _x0, _y0 = self.triangle_points[0]
        _x1, _y1 = self.triangle_points[1]
        _x2, _y2 = self.triangle_points[2]
        self.draw_line(_x0, _y0, _x1, _y1)
        self.draw_line(_x1, _y1, _x2, _y2)
        self.draw_line(_x2, _y2, _x0, _y0)

    def print_point(self):
        glBegin(GL_POINTS)
        point = self.x0, self.y0
        print(point)
        glVertex2f(*point)
        glEnd()

    def read_triangle_points(self):
        for i in range(3):
            print('ponto {0}'.format(i + 1))
            x, y = map(int, input().split())
            self.triangle_points.append(
                (x, y)
            )

    def read_line_points(self):
        print('ponto {0}'.format(1))
        self.x0, self.y0 = map(int, input().split())

        print('ponto {0}'.format(2))
        self.x1, self.y1 = map(int, input().split())

    def read_point(self):
        print('digite x e y do ponto')
        self.x0, self.y0 = map(int, input().split())

    def run(self):
        menu_txt = (
            '1: desenhar um ponto na tela\n',
            '2: plotar uma reta\n'
            '3: desenhar um triângulo'
        )
        menu_functions = {
            1: (self.read_point, self.print_point),
            2: (self.read_line_points, self.draw_line),
            3: (self.read_triangle_points, self.draw_triangle)
        }

        print(menu_txt)
        option = int(input())
        data_function = menu_functions.get(option)

        while not data_function:
            print('opção inválida')
            option = map(int, input().split())
            data_function = menu_functions.get(option)

        read_func, self.func = menu_functions[option]
        read_func()

        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        wind = glutCreateWindow("OpenGL Coding Practice")
        glutDisplayFunc(self.showScreen)
        glutIdleFunc(self.showScreen)
        glutMainLoop()

if __name__ == '__main__':
    draw = Draw()
    draw.run()
