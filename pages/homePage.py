from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QDesktopServices, QFont
from PyQt6.QtCore import QUrl, pyqtSignal, QDateTime
from ui.home_ui import Ui_Form
from models import UserData, Session, Notification
import socket
import uuid
import requests
from datetime import datetime, timedelta

domain = "http://127.0.0.1:8000"


class homepage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.session = Session()

        # Setup fonts
        self.setup_fonts()

        # Initialize UI
        self.setup_ui()

        # Load user data
        self.load_user_data()

        # Setup connections
        self.setup_connections()

    def setup_fonts(self):
        font_mid = QFont()
        font_mid.setFamily("./font/Poppins-Black.ttf")
        self.setFont(font_mid)

    def setup_ui(self):
        # Initialize notification list with proper label mapping
        self.notification_frames = [
            (self.ui.notice_1, self.ui.notice_leb_1, self.ui.notice_time_1),
            (self.ui.notice_2, self.ui.notice_leb_2, self.ui.notice_time_2),
            (self.ui.notice_3, self.ui.notice_leb_3, self.ui.notice_time_3),
            (self.ui.notice_4, self.ui.notice_leb_4, self.ui.notice_time_4),
            (self.ui.notice_5, self.ui.notice_leb_5, self.ui.notice_time_5),
            (self.ui.notice_6, self.ui.notice_leb_6, self.ui.notice_time_6),
            (self.ui.notice_7, self.ui.notice_leb_7, self.ui.notice_time_7),
            (self.ui.notice_8, self.ui.notice_leb_8, self.ui.notice_time_8)
        ]

        # Get MAC address
        self.mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                                     for elements in range(0, 2 * 6, 2)][::-1]).upper()

        # Get IP address (simplified - gets local IP)
        hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(hostname)

        # Set default values
        self.ui.mac.setText(self.mac_address)
        self.ui.ip.setText(self.ip_address)

        # Update mock location
        self.get_location()

        # Load notifications
        self.load_notifications()

    def setup_connections(self):
        # Dashboard
        self.ui.dashboard.mousePressEvent = lambda event: self.open_url(f"{domain}/dashboard")

        # Browse Software
        self.ui.browse_software.mousePressEvent = lambda event: self.open_url(f"{domain}/browse-software")

        # Purchase Credit
        self.ui.purchase_credit.mousePressEvent = lambda event: self.open_url(f"{domain}/buy_credits/")

        # My Software
        self.ui.my_software.mousePressEvent = lambda event: self.open_url(f"{domain}/my-software")

        # My Device
        self.ui.manage_device.mousePressEvent = lambda event: self.open_url(f"{domain}/my-devices")

        # Browse Coupon
        self.ui.browse_coupon.mousePressEvent = lambda event: self.open_url(f"{domain}/coupons/")

    def open_url(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def load_user_data(self):
        user = self.session.query(UserData).first()
        if user:
            # Update user data with current IP and MAC if needed
            if not user.mac_address:
                user.mac_address = self.mac_address
            if not user.ip_address:
                user.ip_address = self.ip_address

            # Update the UI with user data
            self.ui.credit.setText(f"{user.credits:.2f}")
            self.ui.mac.setText(user.mac_address)
            self.ui.ip.setText(user.ip_address)

            if user.location:
                self.ui.location.setText(user.location)

            self.session.commit()

    def get_location(self):
        # Simplified location lookup - in a real app you'd use a geolocation API
        try:
            # This is a mock - replace with actual geolocation API
            response = requests.get(f"http://ip-api.com/json/{self.ip_address}").json()
            if response['status'] == 'success':
                location = f"{response.get('city', '')}, {response.get('countryCode', '')}"
                self.ui.location.setText(location)

                # Save to database
                user = self.session.query(UserData).first()
                if user:
                    user.location = location
                    user.ip_address = self.ip_address
                    self.session.commit()
        except:
            # Fallback to default location
            self.ui.location.setText("Unknown Location")

    def load_notifications(self):
        # Get notifications from database - now ordered ascending (oldest first)
        notifications = self.session.query(Notification).order_by(Notification.time.asc()).limit(8).all()

        # Reverse to show newest at top but maintain serial order
        notifications = list(reversed(notifications))

        for i, (frame, title_label, time_label) in enumerate(self.notification_frames):
            if i < len(notifications):
                notification = notifications[i]

                print("title_label : ", title_label.objectName())

                # Set notification message
                title_label.setText(f"⮞ {notification.message}")

                # Format time (keeping your existing time formatting code)
                notification_time = notification.time
                current_time = datetime.now()
                time_diff = current_time - notification_time

                days = time_diff.days
                hours, remainder = divmod(time_diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)

                time_str = ""
                if days > 0:
                    time_str += f"{days} day{'s' if days > 1 else ''}"
                    if hours > 0:
                        time_str += f", {hours} hour{'s' if hours > 1 else ''}"
                elif hours > 0:
                    time_str += f"{hours} hour{'s' if hours > 1 else ''}"
                    if minutes > 0:
                        time_str += f", {minutes} minute{'s' if minutes > 1 else ''}"
                elif minutes > 0:
                    time_str += f"{minutes} minute{'s' if minutes > 1 else ''}"
                else:
                    time_str = "Just now"

                time_str += " ago" if time_str != "Just now" else ""
                time_label.setText(time_str)

                # Show the frame
                frame.show()
            else:
                # Hide unused frames
                frame.hide()

    def update_credits(self, amount):
        """Update the credits display and database"""
        user = self.session.query(UserData).first()
        if user:
            user.credits = amount
            self.session.commit()
            self.ui.credit.setText(f"{amount:.2f}")

    def closeEvent(self, event):
        self.session.close()
        super().closeEvent(event)
