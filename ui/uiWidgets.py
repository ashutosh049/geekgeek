from PyQt4 import QtGui,QtCore
import webbrowser


class QCustomQWidget(QtGui.QWidget):
    def __init__(self, feed,parent=None):
        super(QCustomQWidget, self).__init__(parent)
        self.set_feed(feed)
        self.descriptionQVBoxLayout = QtGui.QVBoxLayout()

        self.titleQLabel = QtGui.QLabel()
        self.titleQLabel.setWordWrap(True)
        self.titleQLabel.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold))

        self.descriptionQLabel = QtGui.QLabel()
        self.descriptionQLabel.setWordWrap(True)

        self.descriptionQVBoxLayout.addWidget(self.titleQLabel)
        self.descriptionQVBoxLayout.addWidget(self.descriptionQLabel)

        # Create a vertical box layout having read and follow buttons
        self.actionsQVBoxLayout = QtGui.QVBoxLayout()
        self.readQPushButton = QtGui.QPushButton("Read")
        self.connect(self.readQPushButton,QtCore.SIGNAL("clicked()"),self.handle_read_button_click)

        self.followQPushButton = QtGui.QPushButton("Follow")
        self.connect(self.followQPushButton, QtCore.SIGNAL("clicked()"), self.handle_follow_button_click)
        self.actionsQVBoxLayout.addWidget(self.readQPushButton)
        self.actionsQVBoxLayout.addWidget(self.followQPushButton)

        self.allQHBoxLayout = QtGui.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.descriptionQVBoxLayout, 1)
        self.allQHBoxLayout.addLayout(self.actionsQVBoxLayout)
        self.setLayout(self.allQHBoxLayout)
        # # setStyleSheet
        # self.textUpQLabel.setStyleSheet('''
        #     color: rgb(0, 0, 255);
        # ''')

    def set_description(self, text):
        self.descriptionQLabel.setText(text)

    def set_title(self, text):
        self.titleQLabel.setText(text)

    def set_feed(self,feed):
        self.feed = feed

    def handle_read_button_click(self):
        """ On clicking Read button, open the feed in browser.
            Set the is_read button to 1 and
            change the background of the description
            which marks as read
        """
        self.descriptionQLabel.setStyleSheet('''
            color: rgb(255,0,0)
        ''')
        webbrowser.open_new(self.feed.url)
        print "read",self.feed.is_read

    def handle_follow_button_click(self):
        """ On clicking the Follow button, set the is_follow variable to True"""
        self.feed.is_follow_on=True
        print "follow",self.feed.is_follow_on

class GeekGeekQMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(GeekGeekQMainWindow, self).__init__()
        # Create QListWidget
        self.myQListWidget = QtGui.QListWidget(self)
        self.setCentralWidget(self.myQListWidget)
    def addFeed(self,feed):
        myCustomWidget = QCustomQWidget(feed)
        myCustomWidget.set_title(feed.title)
        myCustomWidget.set_description(feed.description)

        # Create QListWidgetItem
        myQListWidgetItem = QtGui.QListWidgetItem(self.myQListWidget)
        # Set size hint
        myQListWidgetItem.setSizeHint(myCustomWidget.sizeHint())
        # Add QListWidgetItem into QListWidget
        self.myQListWidget.addItem(myQListWidgetItem)


        self.myQListWidget.setItemWidget(myQListWidgetItem, myCustomWidget)

