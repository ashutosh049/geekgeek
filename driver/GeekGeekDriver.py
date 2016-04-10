from ui.uiWidgets import GeekGeekQMainWindow
from PyQt4 import QtGui,QtCore
from feedParser.feedparsing import *
import sys

FEEDS_FROM_DB = {}
def start_ui():
    app = QtGui.QApplication([])
    app.connect(app,QtCore.SIGNAL("aboutToQuit()"),myExitHandler)
    global WINDOW
    WINDOW = GeekGeekQMainWindow()
    WINDOW.setWindowTitle("GeekGeek")
    WINDOW.setGeometry(300, 300, 750, 500)
    WINDOW.showMaximized()
    populate_window()
    WINDOW.show()
    sys.exit(app.exec_())

def myExitHandler():
    CURRENT_FEEDS_FROM_DB = get_feeds_from_db()
    winow_data_store = WINDOW.get_data_store()
    CURRENT_FEEDS_FROM_DB.update(winow_data_store)
    write_feeds_to_db(CURRENT_FEEDS_FROM_DB)
    print "Close button clicked"


def populate_window():
    FEEDS_FROM_DB = get_feeds_from_db()
    WINDOW.set_data_store(FEEDS_FROM_DB)
if __name__=="__main__":
    start_ui()
