from pages.homePage import homepage
from ui.dashboard_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from pages.settingsPage import settingsPage

class DashboardPage(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        # ************  Home Page -- top part
        print("debug HomePage")
        self.homePage = homepage()
        self.ui.stackedWidget.addWidget(self.homePage)



        # ************ settings page -- Bottom part
        print("debug settingsPage")
        self.settingsPage = settingsPage(self.username)
        self.ui.stackedWidget.addWidget(self.settingsPage)
        print("debug after settingsPage")
        # End pages ***********************
        # Page switching
        try:
            self.ui.homeIconBtn.clicked.connect(lambda: self.switch_page("home"))
            self.ui.homeBtn.clicked.connect(lambda: self.switch_page("home"))


            self.ui.settingsBtn.clicked.connect(lambda: self.switch_page("settings_page"))
            self.ui.settingsIconBtn.clicked.connect(lambda: self.switch_page("settings_page"))

        except AttributeError as e:
            print(f"Error connecting button: {e}")

    def switch_page(self, page_name):
        try:
            if page_name == "home":
                self.ui.stackedWidget.setCurrentWidget(self.homePage)

            elif page_name == "settings_page":
                self.ui.stackedWidget.setCurrentWidget(self.settingsPage)
            else:
                print(f"Invalid page name: {page_name}")
        except Exception as e:
            print(f"Error switching page: {e}")
