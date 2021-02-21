
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage as QWebPage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
时间久，代码更改较大
我试图从QWebEnginePage对象获取html代码。根据Qt引用，QWebEnginePage对象的'toHtml'是如下所示的异步方法
然后书中方法无法实现
"""

url = 'http://example.python-scraping.com/dynamic'

class Widget(QWidget):
    toHtmlFinished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.web_view = QWebEngineView(self)
        self.web_view.load(QUrl(url))
        btn = QPushButton("Get HTML", self)
        self.layout().addWidget(self.web_view)
        self.layout().addWidget(btn)
        btn.clicked.connect(self.get_html)
        self.html = ""
        # self.from_loopback, self.to_loopback = Pipe(False)

    def store_html(self, html):
        self.html = html
        self.toHtmlFinished.emit()

    def get_html(self):
        current_page = self.web_view.page()
        current_page.toHtml(self.store_html)
        loop = QEventLoop()
        self.toHtmlFinished.connect(loop.quit)
        loop.exec_()
        print(self.html)
        # return self.from_loopback.recv()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
