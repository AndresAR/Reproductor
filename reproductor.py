# -*- coding: utf-8 -*-
import os

from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL
from PyQt4.phonon import Phonon


class Reproductor(QWidget):

    def __init__(self):
        super(Reproductor, self).__init__()
        self.setWindowTitle(self.tr("Reproductor"))
        self.setMinimumSize(400, 100)

        vbox = QVBoxLayout(self)
        self.re = Phonon.createPlayer(Phonon.MusicCategory)
        self.slide = Phonon.SeekSlider(self.re, self)
        vbox.addWidget(self.slide)

        # Botones
        self.rep = QPushButton(self.style().standardIcon(QStyle.SP_MediaPlay), '')
        self.pausar = QPushButton(self.style().standardIcon(QStyle.SP_MediaPause), '')
        self.parar = QPushButton(self.style().standardIcon(QStyle.SP_MediaStop), '')
        self.volumen = QPushButton(self.style().standardIcon(QStyle.SP_MediaVolume), '')
        self.mute = QPushButton(self.style().standardIcon(QStyle.SP_MediaVolumeMuted), '')

        self.seleccionar = QPushButton('....')
        self.nombre = QLabel('')

        hbox = QHBoxLayout()
        hbox.addWidget(self.rep)
        hbox.addWidget(self.pausar)
        hbox.addWidget(self.parar)
        hbox.addWidget(self.seleccionar)
        hbox.addWidget(self.volumen)
        hbox.addWidget(self.mute)
        vbox.addLayout(hbox)
        vbox.addWidget(self.nombre)

        # Conexiones
        self.connect(self.rep, SIGNAL("clicked()"), self.__play)
        self.connect(self.pausar, SIGNAL("clicked()"), self.__pausar)
        self.connect(self.parar, SIGNAL("clicked()"), self.__parar)
        self.connect(self.seleccionar, SIGNAL("clicked()"), self.__seleccionar)
        self.connect(self.volumen, SIGNAL("clicked()"), self.__volumen)

    def __play(self):
        self.re.play()

    def __pausar(self):
        self.re.pause()

    def __parar(self):
        self.re.stop()

    def __seleccionar(self):
        path = unicode(QFileDialog.getOpenFileName(self, "Cancion"))
        indice = path.rfind('/')
        self.re.setCurrentSource(Phonon.MediaSource(path))
        self.nombre.setText(path[indice + 1 if indice > -1 else 0:])

    def __volumen(self):
        self.ui.volumeSlider.setAudioOutput(self.ui.videoPlayer.audioOutput())
if __name__ == '__main__':
    import sys
    app = QApplication([])
    w = Reproductor()
    w.show()

    sys.exit(app.exec_())


