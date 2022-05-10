from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QHBoxLayout
from PyQt5.QtCore import QPoint, QTimer
from View.CardWidget import CardWidget
from UseCases.General.DefaultCard import DefaultCard
import sys
import numpy as np
import moderngl
from Infrastructure.DataAccess.FileFolders import shadersFolder



class glWidget(QOpenGLWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        #self.setMinimumSize(310, 470)

        self.time = 0
        #self.setAttribute(Qt.WA_AlwaysStackOnTop, True)

        self.mousePosition = QPoint(int(self.geometry().width()/2), int(self.geometry().height()/2))
        self.setMouseTracking(True)



    def initializeGL(self):

        self.ctx = moderngl.create_context()
        self.ctx.enable(self.ctx.BLEND)
        self.ctx.blend_func = self.ctx.SRC_ALPHA, self.ctx.ONE_MINUS_SRC_ALPHA
        self.prog = self.ctx.program(vertex_shader=read_shader("vertex_shader.glsl"),
                           fragment_shader=read_shader("fragment_shader.glsl"))

        vertices = np.array([
            -1, -1,
            1, -1,
            1, 1,
            -1, 1,
        ], dtype='float32')
        vbo = self.ctx.buffer(vertices)
        self.vao = self.ctx.simple_vertex_array(self.prog, vbo, 'in_vert')
        fbo = self.ctx.framebuffer(color_attachments=[self.ctx.texture((200, 200), 4)])
        fbo.use()
        self.sampler2D = self.ctx.sampler()
        self.sampler2D.use()

        self.ctx.clear()

        self.timer = QTimer()
        self.timer.timeout.connect(self.paintGL)
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

    def mousePressEvent(self, QMouseEvent):
        QOpenGLWidget.mousePressEvent(self, QMouseEvent)


    def mouseMoveEvent(self, QMouseEvent):
        self.mousePosition = QMouseEvent.pos()
        QOpenGLWidget.mouseMoveEvent(self, QMouseEvent)

    def leaveEvent(self, a0):
        self.mousePosition = QPoint(int(self.geometry().width()/2), int(self.geometry().height()/2))
        QOpenGLWidget.leaveEvent(self, a0)


    def resizeEvent(self, e):
        self.mousePosition = QPoint(int(self.geometry().width() / 2), int(self.geometry().height() / 2))
        QOpenGLWidget.resizeEvent(self, e)

    def paintGL(self):
        self.time += 0.01
        self.set_uniform('u_resolution',np.array((self.geometry().width(),
                                                self.geometry().height()), dtype='float32'))
        self.set_uniform('u_time',np.array(self.time, dtype='float32'))
        #self.set_uniform('mouse',np.array((self.mousePosition.x(),
        #                                   self.mousePosition.y()), dtype='float32'))
        self.vao.render(moderngl.TRIANGLE_FAN)


    def set_uniform(self, u_name, u_value):
        try:
            self.prog[u_name].write(u_value)
        except KeyError:
            print(f"Key error. {u_name}, {u_value}")


def read_shader(shader_name):
    tmp = ""
    with open(f"{shadersFolder}/{shader_name}") as file:
        tmp = file.read()
    return tmp


class BackGround(glWidget):
    def __init__(self, w, parent=None):
        super().__init__(parent)

        self.l = QHBoxLayout()
        self.l.addWidget(w)

        self.setLayout(self.l)

        self.l.setContentsMargins(5, 4, 5, 4)
        self.setMinimumSize(w.minimumSize())
        self.setMaximumSize(w.maximumSize())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testCard = DefaultCard()
    w = CardWidget(testCard)
    window = BackGround(w)
    window.show()
    sys.exit(app.exec_())