import sys
import json
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class ExamKiosk(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistem Ujian')

        # Setup UI
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Browser widget
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        # Password dialog
        self.password_dialog = None

        # Load settings
        self.load_settings()

        # Setup fullscreen
        self.showFullScreen()

        # Disable alt+f4
        self.shortcut = QShortcut(QKeySequence('Alt+F4'), self)
        self.shortcut.activated.connect(lambda: None)

    def load_settings(self):
        try:
            response = requests.get('https://ujian.pages.dev/password.json')
            self.settings = response.json()
            self.current_password = self.settings.get('exit_password', '1234')
            self.login_password = self.settings.get('login_password', '5678')
        except:
            # Fallback jika tidak bisa mengakses remote settings
            self.settings = {
                'exit_password': '1234',
                'login_password': '5678'
            }
            self.current_password = '1234'
            self.login_password = '5678'

    def check_login(self):
        text, ok = QInputDialog.getText(
            self, 'Login', 'Masukkan password:',
            QLineEdit.Password
        )
        if ok:
            if text == self.login_password:
                self.browser.setUrl(QUrl('https://ujian.pages.dev/h0'))
                return True
            else:
                QMessageBox.warning(self, 'Error', 'Password salah!')
                self.check_login()
        else:
            sys.exit()

    def keyPressEvent(self, event):
        # Mendeteksi Ctrl+Alt+Del atau Win+L
        if event.key() == Qt.Key_L and event.modifiers() == Qt.MetaModifier:
            self.check_exit()
        if event.key() == Qt.Key_Delete and \
           event.modifiers() == (Qt.ControlModifier | Qt.AltModifier):
            self.check_exit()

    def check_exit(self):
        # Refresh password dari remote
        self.load_settings()

        text, ok = QInputDialog.getText(
            self, 'Exit', 'Masukkan password untuk keluar:',
            QLineEdit.Password
        )
        if ok and text == self.current_password:
            sys.exit()
        else:
            QMessageBox.warning(self, 'Error', 'Password salah!')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ExamKiosk()
    window.show()

    # Check login first
    if not window.check_login():
        sys.exit()

    sys.exit(app.exec_())
