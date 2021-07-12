import sys

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip

from ui_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.animation = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # define class variables
        self.clickPosition = None

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 90, 157, 550))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/github.svg"))
        self.setWindowTitle(self.ui.label.text())
        QSizeGrip(self.ui.size_grip)

        def drag_window(e):
            if not self.isMaximized():
                try:
                    if e.buttons() == QtCore.Qt.LeftButton and self.clickPosition:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                except AttributeError:
                    pass

                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.header_frame.mouseMoveEvent = drag_window

        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.maximize_window_button.clicked.connect(self.maximize_restore)
        self.ui.side_menu_button.clicked.connect(self.show_hide_menu)

    def show_hide_menu(self):
        width = self.ui.side_menu_container.width()

        if width == 0:
            new_width = 200
            self.ui.side_menu_button.setIcon(QtGui.QIcon(":/icons/icons/align-left.svg"))
            animation_type = QtCore.QEasingCurve.OutBack
            animation_duration = 250
        else:
            new_width = 0
            self.ui.side_menu_button.setIcon(QtGui.QIcon(":/icons/icons/menu.svg"))
            animation_type = QtCore.QEasingCurve.OutExpo
            animation_duration = 350

        self.animation = QtCore.QPropertyAnimation(self.ui.side_menu_container, b'maximumWidth')
        self.animation.setDuration(animation_duration)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(animation_type)
        self.animation.start()

    def maximize_restore(self):
        if not self.isMaximized():
            self.showMaximized()
            self.ui.maximize_window_button.setIcon(QtGui.QIcon(":/icons/icons/maximize.svg"))
        else:
            self.showNormal()
            self.ui.maximize_window_button.setIcon(QtGui.QIcon(":/icons/icons/maximize-2.svg"))

    def mouseMoveEvent(self, event):
        self.clickPosition = event.globalPos()

    def mouseReleaseEvent(self, event):
        # reset the last mouse click and hold position, to prevent the slight jump of window while
        # dragging and moving from a different point on header_frame
        try:
            del self.clickPosition
        except AttributeError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
