from ui.uiWidgets import GeekGeekQMainWindow
from PyQt4 import QtGui
from feedParser.feedparsing import *
import sys


def start_ui():
    app = QtGui.QApplication([])
    global WINDOW
    WINDOW = GeekGeekQMainWindow()
    WINDOW.setWindowTitle("GeekGeek")
    WINDOW.setGeometry(300, 300, 750, 500)
    populate_window()
    WINDOW.show()
    sys.exit(app.exec_())
def populate_window():
    feeds = get_feeds()
    for feed in feeds:
        WINDOW.addFeed(feed)

if __name__=="__main__":
    start_ui()
