from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
import webbrowser

domain = 'http://127.0.0.1:8000'
software_name = "Sofmark - AI Writer"

class Ui_LoginForm(QWidget):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(921, 563)

        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(LoginForm)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Centering container
        self.container = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QHBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)

        # Card widget (500x600)
        self.card = QtWidgets.QWidget()
        self.card.setMinimumSize(500, 600)
        self.card.setMaximumSize(500, 600)
        self.card.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 15px;
            }
        """)

        # Add shadow effect
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0, 25))
        self.card.setGraphicsEffect(shadow)

        self.card_layout = QtWidgets.QVBoxLayout(self.card)
        self.card_layout.setContentsMargins(50, 40, 50, 40)
        self.card_layout.setSpacing(20)

        # Logo section
        self.logo_section = QtWidgets.QWidget()
        self.logo_section_layout = QtWidgets.QVBoxLayout(self.logo_section)
        self.logo_section_layout.setContentsMargins(0, 0, 0, 20)

        self.logo = QtWidgets.QLabel()
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo.setPixmap(QtGui.QPixmap("./images/logo.png").scaled(50, 50,
                                                                      QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                                                      QtCore.Qt.TransformationMode.SmoothTransformation))

        self.brand_name = QtWidgets.QLabel()
        self.brand_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.brand_name.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.logo_section_layout.addWidget(self.logo)
        self.logo_section_layout.addWidget(self.brand_name)
        self.card_layout.addWidget(self.logo_section)

        # Form elements
        self.form_layout = QtWidgets.QVBoxLayout()
        self.form_layout.setSpacing(20)

        # Email field
        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("name@example.com")
        self.email_input.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #5b5bff;
            }
        """)

        # Password field
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #5b5bff;
            }
        """)

        # Forgot password link
        self.forgot_link = QtWidgets.QLabel("Forgot Password?")
        self.forgot_link.setStyleSheet("""
            QLabel {
                font-size: 13px;
                color: #5b5bff;
                text-align: right;
            }
        """)
        self.forgot_link.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # Login button
        self.login_btn = QtWidgets.QPushButton("Sign In")
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                padding: 12px;
                border-radius: 6px;
                font-size: 15px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #333333;
            }
        """)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # Divider
        self.divider = QtWidgets.QWidget()
        self.divider.setStyleSheet("""
            QWidget {
                border-top: 1px solid #eee;
                margin: 10px 0;
            }
        """)

        # Alternative buttons
        self.alt_buttons = QtWidgets.QWidget()
        self.alt_buttons_layout = QtWidgets.QHBoxLayout(self.alt_buttons)
        self.alt_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.alt_buttons_layout.setSpacing(10)

        self.reset_btn = QtWidgets.QPushButton("Reset Password")
        self.reset_btn.setStyleSheet("""
            QPushButton {
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
                border: 1px solid #000000;
                background-color: white;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #f5f5f5;
            }
        """)
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reset_btn.clicked.connect(lambda: webbrowser.open(f"{domain}/forget_password"))

        self.create_btn = QtWidgets.QPushButton("Create Account")
        self.create_btn.setStyleSheet("""
            QPushButton {
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
                border: 1px solid #000000;
                background-color: white;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #f5f5f5;
            }
        """)
        self.create_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.create_btn.clicked.connect(lambda: webbrowser.open(f"{domain}/register"))

        self.alt_buttons_layout.addWidget(self.reset_btn)
        self.alt_buttons_layout.addWidget(self.create_btn)

        # Error message
        self.error_message = QtWidgets.QLabel()
        self.error_message.setStyleSheet("color: #3E0768; font-size: 14px;font-weight:bold;")
        self.error_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_message.setWordWrap(True)

        # Contact support button (initially hidden)
        self.contact_support_btn = QtWidgets.QPushButton("Login Web Dashboard")
        self.contact_support_btn.setStyleSheet("""
            QPushButton {
                background-color: #5b5bff;
                color: white;
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
                border: none;
            }
            QPushButton:hover {
                background-color: #4a4aff;
            }
        """)
        self.contact_support_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # Assemble form
        self.form_layout.addWidget(self.email_input)
        self.form_layout.addWidget(self.password_input)
        self.form_layout.addWidget(self.forgot_link)
        self.form_layout.addWidget(self.login_btn)
        self.form_layout.addWidget(self.divider)
        self.form_layout.addWidget(self.alt_buttons)
        self.form_layout.addWidget(self.error_message)
        self.form_layout.addWidget(self.contact_support_btn)

        self.card_layout.addLayout(self.form_layout)
        self.container_layout.addWidget(self.card, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.container, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

        # Create the font object
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(22)  # Set a more reasonable base size
        self.font.setBold(True)

        # Apply this font to widgets where you want it
        self.email_input.setFont(self.font)
        self.password_input.setFont(self.font)
        # self.forgot_link.setFont(self.font)
        self.login_btn.setFont(self.font)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.brand_name.setText(_translate("LoginForm", software_name))
        self.login_btn.setText(_translate("LoginForm", "Sign In"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec())
