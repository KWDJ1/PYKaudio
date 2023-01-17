from aqt import mw
from aqt.qt import *
from aqt.sound import *
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
from playsound import playsound




class audio:







    def Upload(self):
        fname = QFileDialog.getOpenFileName(mw, "Open Audio", filter="Audio (*.wav)")

        def music(getfile):

           name = str(getfile[0])
           playsound(name)

        music(fname)



def setupMenus(self):

    menu = QMenu("Pykaudio", mw)
    
    menu.addSeparator()

    getfilee = QAction("Upload/Play Audio", menu)
    qconnect(getfilee.triggered, audio.Upload)
    menu.addSeparator()
    menu.addAction(getfilee)


    mw.form.menubar.addMenu(menu)

setupMenus(mw)


audio()
