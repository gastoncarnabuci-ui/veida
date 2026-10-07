import sys
import threading
from pathlib import Path

import uvicorn
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from server.api import app as fastapi_app


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("V.E.I.D.A. · Arquitecta de Sueños")
        self.resize(1400, 900)

        self.view = QWebEngineView()
        self.setCentralWidget(self.view)

        html = ROOT / "ui" / "index.html"
        self.view.load(QUrl.fromLocalFile(str(html)))


def run_server():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8765, log_level="warning")


def main():
    threading.Thread(target=run_server, daemon=True).start()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
