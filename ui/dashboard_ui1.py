from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 600)
        MainWindow.setStyleSheet("""*{background:none;border:none;margin:0;padding:0;}
                                 QDateEdit, QLineEdit{border-radius:10px;padding:2px;margin:1px 6px;}
                                 #IconMenu, #SideMenu{background-color:#221402;padding:0px;margin:0px;}
                                 #IconMenu QPushButton, #IconMenu QLabel, #SideMenu QPushButton, #SideMenu QLabel{
                                    background-color:#221402;
                                    color:#C6CDCA;
                                    text-align: left;
                                    padding:14px 12px;
                                    }
                                 #IconMenuItems QPushButton, #MenuItems QPushButton{border-radius:10px;}
                                 #IconMenuItems QPushButton:checked, #MenuItems QPushButton:checked,#IconMenuItems QPushButton:hover, #MenuItems QPushButton:hover {
                                    background-color: #010905;
                                    }
                                 #header{background-color:#2D221B}
                                 #header QLabel, #header QPushButton{color:#C6CDCA;font-size:16px;}
                                 #header #userBtn{margin-right:20px;}
                                 #body{background-color:#F0F0F0}
                                 """)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget_Layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.centralwidget_Layout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget_Layout.setSpacing(0)
        self.centralwidget_Layout.setObjectName("centralwidget_Layout")

        # *************************** Icon Menu *********************************
        self.IconMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.IconMenu.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.IconMenu.setFont(font)
        self.IconMenu.setObjectName("IconMenu")
        self.IconMenu.setHidden(True)

        self.IconMenu_Layout = QtWidgets.QVBoxLayout(self.IconMenu)
        self.IconMenu_Layout.setContentsMargins(0, 0, 0, 0)
        self.IconMenu_Layout.setSpacing(0)
        self.IconMenu_Layout.setObjectName("IconMenu_Layout")
        self.IconMenuToggle = QtWidgets.QFrame(parent=self.IconMenu)
        self.IconMenuToggle.setMinimumSize(QtCore.QSize(0, 50))
        self.IconMenuToggle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.IconMenuToggle.setFont(font)
        self.IconMenuToggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.IconMenuToggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.IconMenuToggle.setObjectName("IconMenuToggle")
        self.IconMenuToggle_Layout = QtWidgets.QVBoxLayout(self.IconMenuToggle)
        self.IconMenuToggle_Layout.setContentsMargins(9, -1, -1, -1)
        self.IconMenuToggle_Layout.setObjectName("IconMenuToggle_Layout")
        self.IconToggleBtn = QtWidgets.QPushButton(parent=self.IconMenuToggle)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.IconToggleBtn.setFont(font)
        self.IconToggleBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.IconToggleBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.IconToggleBtn.setIcon(icon)
        self.IconToggleBtn.setIconSize(QtCore.QSize(28, 28))
        self.IconToggleBtn.setCheckable(True)
        self.IconToggleBtn.setAutoRepeat(False)
        self.IconToggleBtn.setAutoExclusive(True)
        self.IconToggleBtn.setObjectName("IconToggleBtn")
        self.IconMenuToggle_Layout.addWidget(self.IconToggleBtn)
        self.IconMenu_Layout.addWidget(self.IconMenuToggle)
        self.IconMenuItems = QtWidgets.QFrame(parent=self.IconMenu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.IconMenuItems.setFont(font)
        self.IconMenuItems.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.IconMenuItems.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.IconMenuItems.setObjectName("IconMenuItems")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.IconMenuItems)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # *** Home Icon Button ****
        self.homeIconBtn = QtWidgets.QPushButton(parent=self.IconMenuItems)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.homeIconBtn.setFont(font)
        self.homeIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.homeIconBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeIconBtn.setIcon(icon1)
        self.homeIconBtn.setIconSize(QtCore.QSize(28, 28))
        self.homeIconBtn.setCheckable(True)
        self.homeIconBtn.setChecked(True)
        self.homeIconBtn.setAutoExclusive(True)
        self.homeIconBtn.setAutoRepeatDelay(100)
        self.homeIconBtn.setAutoDefault(False)
        self.homeIconBtn.setFlat(False)
        self.homeIconBtn.setObjectName("homeIconBtn")
        self.verticalLayout_2.addWidget(self.homeIconBtn)


        # *** space ****
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        # *** settings Icon Button ****
        self.settingsIconBtn = QtWidgets.QPushButton(parent=self.IconMenuItems)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.settingsIconBtn.setFont(font)
        self.settingsIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.settingsIconBtn.setText("")
        settingIcon = QtGui.QIcon()
        settingIcon.addPixmap(QtGui.QPixmap("./icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingsIconBtn.setIcon(settingIcon)
        self.settingsIconBtn.setIconSize(QtCore.QSize(28, 28))
        self.settingsIconBtn.setCheckable(True)
        self.settingsIconBtn.setAutoExclusive(True)
        self.settingsIconBtn.setAutoRepeatDelay(100)
        self.settingsIconBtn.setAutoDefault(False)
        self.settingsIconBtn.setFlat(False)
        self.settingsIconBtn.setObjectName("settingsIconBtn")
        self.verticalLayout_2.addWidget(self.settingsIconBtn)

        # *** Logout Icon Button ****
        self.logoutIconBtn = QtWidgets.QPushButton(parent=self.IconMenuItems)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.logoutIconBtn.setFont(font)
        self.logoutIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logoutIconBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./icons/log-out.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logoutIconBtn.setIcon(icon6)
        self.logoutIconBtn.setIconSize(QtCore.QSize(28, 28))
        self.logoutIconBtn.setCheckable(True)
        self.logoutIconBtn.setAutoExclusive(True)
        self.logoutIconBtn.setAutoRepeatDelay(100)
        self.logoutIconBtn.setAutoDefault(False)
        self.logoutIconBtn.setFlat(False)
        self.logoutIconBtn.setObjectName("logoutIconBtn")
        self.verticalLayout_2.addWidget(self.logoutIconBtn)
        self.IconMenu_Layout.addWidget(self.IconMenuItems)
        self.centralwidget_Layout.addWidget(self.IconMenu)

        # *************************** end Icon Menu **********************************************
        self.SideMenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.SideMenu.setMinimumSize(QtCore.QSize(200, 0))
        self.SideMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.SideMenu.setFont(font)
        self.SideMenu.setObjectName("SideMenu")
        self.SideMenu_Layout = QtWidgets.QVBoxLayout(self.SideMenu)
        self.SideMenu_Layout.setContentsMargins(0, 0, 0, 0)
        self.SideMenu_Layout.setSpacing(0)
        self.SideMenu_Layout.setObjectName("SideMenu_Layout")
        self.MenuToggle = QtWidgets.QFrame(parent=self.SideMenu)
        self.MenuToggle.setMinimumSize(QtCore.QSize(0, 50))
        self.MenuToggle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.MenuToggle.setFont(font)
        self.MenuToggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MenuToggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MenuToggle.setObjectName("MenuToggle")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MenuToggle)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ToggleBtn = QtWidgets.QPushButton(parent=self.MenuToggle)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ToggleBtn.setFont(font)
        self.ToggleBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ToggleBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./icons/chevrons-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ToggleBtn.setIcon(icon7)
        self.ToggleBtn.setIconSize(QtCore.QSize(28, 28))
        self.ToggleBtn.setCheckable(True)
        self.ToggleBtn.setAutoExclusive(True)
        self.ToggleBtn.setObjectName("ToggleBtn")
        self.verticalLayout.addWidget(self.ToggleBtn)
        self.SideMenu_Layout.addWidget(self.MenuToggle)
        self.MenuItems = QtWidgets.QFrame(parent=self.SideMenu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.MenuItems.setFont(font)
        self.MenuItems.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MenuItems.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MenuItems.setObjectName("MenuItems")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MenuItems)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # *************************** Menu Item ************************************************
        # *** home button ***
        self.homeBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(28, 28))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setChecked(True)
        self.homeBtn.setAutoExclusive(True)
        self.homeBtn.setAutoRepeatDelay(100)
        self.homeBtn.setAutoDefault(False)
        self.homeBtn.setFlat(False)
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)


        # *** space ***
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        # *** settings button ***
        self.settingsBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.settingsBtn.setFont(font)
        self.settingsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.settingsBtn.setIcon(settingIcon)
        self.settingsBtn.setIconSize(QtCore.QSize(28, 28))
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setAutoExclusive(True)
        self.settingsBtn.setAutoRepeatDelay(100)
        self.settingsBtn.setAutoDefault(False)
        self.settingsBtn.setFlat(False)
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_3.addWidget(self.settingsBtn)

        # *** Logout button ***
        self.logoutBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.logoutBtn.setFont(font)
        self.logoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logoutBtn.setIcon(icon6)
        self.logoutBtn.setIconSize(QtCore.QSize(28, 28))
        self.logoutBtn.setCheckable(True)
        self.logoutBtn.setAutoExclusive(True)
        self.logoutBtn.setAutoRepeatDelay(100)
        self.logoutBtn.setAutoDefault(False)
        self.logoutBtn.setFlat(False)
        self.logoutBtn.setObjectName("logoutBtn")
        self.verticalLayout_3.addWidget(self.logoutBtn)

        # *************************** Menu Item end *********************************
        self.SideMenu_Layout.addWidget(self.MenuItems)
        self.centralwidget_Layout.addWidget(self.SideMenu)
        self.MainBody = QtWidgets.QWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.MainBody.setFont(font)
        self.MainBody.setObjectName("MainBody")
        self.MainBody_Layout = QtWidgets.QVBoxLayout(self.MainBody)
        self.MainBody_Layout.setContentsMargins(0, 0, 0, 0)
        self.MainBody_Layout.setSpacing(0)
        self.MainBody_Layout.setObjectName("MainBody_Layout")
        self.Header = QtWidgets.QWidget(parent=self.MainBody)
        self.Header.setMinimumSize(QtCore.QSize(0, 60))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Header.setFont(font)
        self.Header.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Header.setObjectName("Header")
        self.Header_Layout = QtWidgets.QHBoxLayout(self.Header)
        self.Header_Layout.setObjectName("Header_Layout")
        self.LeftHeader = QtWidgets.QWidget(parent=self.Header)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.LeftHeader.setFont(font)
        self.LeftHeader.setObjectName("LeftHeader")
        self.LeftHeader_Layout = QtWidgets.QHBoxLayout(self.LeftHeader)
        self.LeftHeader_Layout.setContentsMargins(-1, 0, -1, -1)
        self.LeftHeader_Layout.setObjectName("LeftHeader_Layout")
        self.logo = QtWidgets.QLabel(parent=self.LeftHeader)
        self.logo.setMinimumSize(QtCore.QSize(30, 30))
        self.logo.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.logo.setFont(font)
        self.logo.setText("")

        # ****** Logo Icon *****
        self.logo.setPixmap(QtGui.QPixmap("./images/logo.png"))

        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.LeftHeader_Layout.addWidget(self.logo)
        self.tag = QtWidgets.QLabel(parent=self.LeftHeader)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.tag.setFont(font)
        self.tag.setObjectName("tag")
        self.LeftHeader_Layout.addWidget(self.tag)
        self.Header_Layout.addWidget(self.LeftHeader, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.Header_Layout.addItem(spacerItem2)
        self.RightHeader = QtWidgets.QWidget(parent=self.Header)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.RightHeader.setFont(font)
        self.RightHeader.setStyleSheet("*{background-color: rgb(0, 0, 0);\n"
                                       " border-radius:20px;\n"
                                       "margin-right:10px;\n"
                                       "}")
        self.RightHeader.setObjectName("RightHeader")
        self.RightHeader_Layout = QtWidgets.QHBoxLayout(self.RightHeader)
        self.RightHeader_Layout.setContentsMargins(-1, 9, -1, 9)
        self.RightHeader_Layout.setObjectName("RightHeader_Layout")
        self.userBtn = QtWidgets.QPushButton(parent=self.RightHeader)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.userBtn.setFont(font)
        self.userBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.userBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./icons/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.userBtn.setIcon(icon8)
        self.userBtn.setIconSize(QtCore.QSize(28, 28))
        self.userBtn.setCheckable(True)
        self.userBtn.setAutoExclusive(True)
        self.userBtn.setObjectName("userBtn")
        self.RightHeader_Layout.addWidget(self.userBtn)
        self.Header_Layout.addWidget(self.RightHeader)
        self.MainBody_Layout.addWidget(self.Header)
        self.Body = QtWidgets.QWidget(parent=self.MainBody)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Body.setFont(font)
        self.Body.setObjectName("Body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # *********** StackWidget *******************
        print("debug 1")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.Body)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")

        ## ************* Pages will add here *****************

        self.horizontalLayout.addWidget(self.stackedWidget)
        self.MainBody_Layout.addWidget(self.Body)
        self.centralwidget_Layout.addWidget(self.MainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ToggleBtn.clicked.connect(self.IconMenu.show)  # type: ignore
        self.ToggleBtn.clicked.connect(self.SideMenu.hide)  # type: ignore
        self.IconToggleBtn.clicked.connect(self.SideMenu.show)  # type: ignore
        self.IconToggleBtn.clicked.connect(self.IconMenu.hide)  # type: ignore

        self.homeBtn.toggled['bool'].connect(self.homeIconBtn.setChecked)  # type: ignore
        self.homeIconBtn.toggled['bool'].connect(self.homeBtn.setChecked)  # type: ignore

        self.settingsBtn.toggled['bool'].connect(self.settingsBtn.setChecked)  # type: ignore
        self.settingsIconBtn.toggled['bool'].connect(self.settingsBtn.setChecked)  # type: ignore

        self.logoutBtn.toggled['bool'].connect(self.logoutIconBtn.setChecked)  # type: ignore
        self.logoutIconBtn.toggled['bool'].connect(self.logoutBtn.setChecked)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IconToggleBtn.setToolTip(_translate("MainWindow", "Expand Menu"))

        self.homeIconBtn.setToolTip(_translate("MainWindow", "Home"))


        self.settingsIconBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.logoutIconBtn.setToolTip(_translate("MainWindow", "Logout"))
        self.ToggleBtn.setToolTip(_translate("MainWindow", "Narrow"))

        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))


        self.settingsBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))

        self.logoutBtn.setToolTip(_translate("MainWindow", "Logout"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))
        self.tag.setText(_translate("MainWindow", "Sofmark"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
