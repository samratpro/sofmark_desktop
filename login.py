import sys
import os
import re
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from ui.login_ui import Ui_LoginForm
import webbrowser
from models import UserData, Session, Notification
from datetime import datetime

domain = 'http://127.0.0.1:8000'  # Update to your actual API endpoint
software_id = 1  # Hardcoded


class LoginPage(QWidget):
    login_success_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        # Initialize session first
        self.session = Session()
        self.setup_ui()

    def setup_ui(self):
        # Login handle
        self.ui.login_btn.clicked.connect(self.handle_login)
        self.ui.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.ui.contact_support_btn.clicked.connect(lambda: webbrowser.open(f"{domain}/login"))
        self.ui.forgot_link.mousePressEvent = self.open_forgot_password
        self.autofill_user()

    def autofill_user(self):
        try:
            user = self.session.query(UserData).first()
            print("user : ", user)
            if user:
                self.ui.email_input.setText(user.email)
                self.ui.password_input.setText(user.password)
        except Exception as e:
            print(f"Error in autofill_user: {e}")
            self.session.rollback()

    def open_forgot_password(self, event):
        webbrowser.open(f"{domain}/forget_password")
        event.accept()

    def get_ip_and_location(self):
        try:
            ip = requests.get("https://api.ipify.org?format=json", timeout=5).json().get("ip")
            if ip:
                info = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5).json()
                location = info.get("city", "") + ", " + info.get("country", "")
            else:
                ip = None
                location = None
            return ip, location
        except Exception:
            return None, None

    def handle_login(self):
        try:
            username = self.ui.email_input.text()
            password = self.ui.password_input.text()
            mac_address = self.get_mac_address()

            device_name = QtCore.QSysInfo.machineHostName() or "Unknown Device"
            device_type = sys.platform
            os_version = QtCore.QSysInfo.prettyProductName()
            ip, location = self.get_ip_and_location()
            payload = {
                "device_name": device_name,
                "device_type": device_type,
                "os_version": os_version,
                "ip_address": ip,
                "location": location
            }

            if username and password:
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', username):
                    try:
                        user = self.session.query(UserData).filter_by(email=username, password=password).first()
                        if user and user.mac_address == mac_address and user.email == username and user.password == password:
                            # Local login
                            print("Local login")
                            self.ui.error_message.setText('')
                            url = f"{domain}/api/read-credits/{username}/{software_id}/{mac_address}/"
                        else:
                            print("MAC mismatch, or new user..")
                            url = f"{domain}/api/verify-license/{username}/{password}/{software_id}/{mac_address}/"

                        response = requests.post(url, json=payload)
                        try:
                            data = response.json()
                        except Exception:
                            data = {"status": "error",
                                    "message": f"HTTP {response.status_code}: {response.text.strip()}"}

                        if response.status_code == 200 and data.get('status') == 'success':
                            self.ui.error_message.setText('')
                            self.ui.contact_support_btn.hide()
                            print("Login successful, emitting signal")


                            print("response.json() : ", response.json())

                            response_data = response.json().get("data", {})
                            software_name = response_data.get("software_name")
                            software_version = response_data.get("software_version")
                            credit_data = response_data.get("total_credits", {})
                            remaining_credit = credit_data.get("remaining")

                            print(f"software_name: {software_name}")
                            print(f"software_version: {software_version}")
                            print(f"remaining_credit: {remaining_credit}")

                            try:
                                user = self.session.query(UserData).filter_by(email=username).first()
                                if not user:
                                    user = UserData(
                                        email=username,
                                        password=password,
                                        mac_address=mac_address,
                                        ip_address=ip,
                                        location=location,
                                        credits=remaining_credit
                                    )
                                    self.session.add(user)
                                else:
                                    user.password = password
                                    user.mac_address = mac_address
                                    user.credits = remaining_credit

                                Notification.add_notification(
                                    self.session,
                                    f"Successful login from {device_name} ({ip})"
                                )
                                self.session.commit()
                            except Exception as e:
                                print(f"Database error: {e}")
                                self.session.rollback()
                                raise

                            self.login_success_signal.emit(username)
                        else:
                            print(f"response.status_code: {response.status_code}")
                            error_message = data.get('message', 'Login failed')
                            self.ui.error_message.setText(error_message)
                            print(f"Invalid login: {error_message}")
                            self.retry_login()
                    except Exception as e:
                        print(f"Database query error: {e}")
                        self.ui.error_message.setText("Login error occurred")
                else:
                    self.ui.error_message.setText("Please input a valid email")
            else:
                self.ui.error_message.setText("Please input email and password")

        except Exception as e:
            print(f"Error in handle_login: {e}")
            self.ui.error_message.setText("Server Connection Fail...")
            if hasattr(self, 'session'):
                self.session.rollback()

    def validate_mac(self, mac):
        return bool(re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac or ""))

    def get_mac_address(self):
        import uuid
        mac = uuid.getnode()
        mac_str = ':'.join(('%012X' % mac)[i:i + 2] for i in range(0, 12, 2))
        return mac_str

    def retry_login(self):
        try:
            self.ui.login_btn.setEnabled(True)
        except Exception as e:
            print(f"Error in retry_login: {e}")

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.ui.login_btn.setText(_translate("LoginForm", "Login"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec())
