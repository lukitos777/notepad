from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Text redactor')
        self.setGeometry(500, 350, 500, 350)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.text_edit.setStyleSheet(
            'QTextEdit {\n'
            '    border-style: solid;\n'
            '    border-color: rgb(192, 192, 192);\n'
            '    border-width: 2px;\n'
            '    border-radius: 5px;\n'
            '    font-family: "Consolas", monospace;\n'
            '    font-size: 22px;'
            '}'
        )

        self.createMenuBar()

    def createMenuBar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        fileMenu = QMenu('&file', self)
        self.menu_bar.addMenu(fileMenu)

        fileMenu.addAction('Open', self.action_clicked)
        fileMenu.addAction('Save', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()

        if action.text() == 'Open':
            f_name = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(f_name, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                pass

        elif action.text() == 'Save':
            f_name = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(f_name, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                pass


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()