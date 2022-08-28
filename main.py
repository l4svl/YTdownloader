import sys
import time
from PyQt5 import QtCore, QtWidgets, QtGui
from pytube import YouTube
from des import Ui_MainWindow


class work(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(work, self).__init__(parent)

    def run(self):
        for i in range(100):
            self.mysignal.emit(i)
            time.sleep(0.1)


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_3.setText('Вставьте сюда ссылку на видео')
        self.resize(550, 600)
        self.mythread = work()
        self.folder_path = None
        self.mythread.mysignal.connect(self.add)
        self.ui.open_folder.clicked.connect(self.open)
        self.ui.download_button.clicked.connect(self.download)

    def start(self):
        self.mythread.start()

    def add(self, value):
        self.ui.progressBar.setValue(value)

    def open(self):
        self.folder_path = QtWidgets.QFileDialog.getExistingDirectory(self)

    def download(self):
        try:
            yt = YouTube(self.ui.lineEdit_3.text())
            self.ui.plainTextEdit.appendPlainText(f'Название видео - {yt.title}\nКоличество просмотров - {yt.views}\n'
                                                  f'Автор видео - {yt.author}\n'
                                                  f'Описание видео - {yt.description}')
            self.start()
            video = yt.streams.get_by_resolution(self.ui.comboBox.currentText())
            video.download(self.folder_path)
            QtWidgets.QMessageBox.information(self, 'Успешно!', 'Видео успешно загружено!')
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(self, 'Кажется возникла ошибка',
                                           'Проверьте ссылку на видео либо папку загрузки или доступные разрешения')
            pass
        finally:
            self.ui.progressBar.setValue(100)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = GUI()
    mywin.show()
    app.exec_()
