from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QLabel, QBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

class BookDiary(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize bookDB database
#        self.bookDB = BookDB('bookdb.txt')

        # BookDiary logo label
        self.bookdiaryLabel = QLabel("DOKU")
        self.bookdiaryLabel.setAlignment(Qt.AlignCenter)
        font = self.bookdiaryLabel.font()
        font.setFamily('Courier New')
        font.setPointSize(font.pointSize() + 8)
        self.bookdiaryLabel.setFont(font)

        # Layout
        bookdiaryLayout = QGridLayout()
        bookdiaryLayout.addWidget(self.bookdiaryLabel, 0, 0)

        # Record Layout creation
        recordLayout = QGridLayout()

        # Input title widget for user
        self.title = QLabel('Title:')
        self.titleInput = QLineEdit()
        self.titleInput.setAlignment(Qt.AlignLeft)
        font = self.title.font()
        font.setPointSize(font.pointSize() + 2)
        self.title.setFont(font)
        self.titleInput.setFont(font)
        recordLayout.addWidget(self.title, 0, 0)
        recordLayout.addWidget(self.titleInput, 0, 1)

        # Input author widget for user
        self.author = QLabel('Author:')
        self.authorInput = QLineEdit()
        self.authorInput.setAlignment(Qt.AlignLeft)
        font = self.author.font()
        font.setPointSize(font.pointSize() + 2)
        self.author.setFont(font)
        self.authorInput.setFont(font)
        recordLayout.addWidget(self.author, 0, 2)
        recordLayout.addWidget(self.authorInput, 0, 3)

        # Input publisher widget for user
        self.publisher = QLabel('Publisher:')
        self.publisherInput = QLineEdit()
        self.publisherInput.setAlignment(Qt.AlignLeft)
        font = self.publisher.font()
        font.setPointSize(font.pointSize() + 2)
        self.publisher.setFont(font)
        self.publisherInput.setFont(font)
        recordLayout.addWidget(self.publisher, 0, 4)
        recordLayout.addWidget(self.publisherInput, 0, 5)

        # Button for reading Barcode
        self.barcodeButton = QToolButton()
        self.barcodeButton.setText('Barcode')
        font = self.barcodeButton.font()
        font.setPointSize(font.pointSize() + 3)
        self.barcodeButton.setFont(font)
#        self.barcodeButton.clicked.connect(self.readBarcode)
        recordLayout.addWidget(self.barcodeButton, 0, 6)

        # Button for add records
        self.addButton = QToolButton()
        self.addButton.setText('Add')
        font = self.addButton.font()
        font.setPointSize(font.pointSize() + 3)
        self.addButton.setFont(font)
#        self.addButton.clicked.connect(self.readBarcode)
        recordLayout.addWidget(self.addButton, 3, 6)

        # Button for show records
        self.showButton = QToolButton()
        self.showButton.setText('Show')
        font = self.showButton.font()
        font.setPointSize(font.pointSize() + 3)
        self.showButton.setFont(font)
#        self.showButton.clicked.connect(self.readBarcode)
        recordLayout.addWidget(self.showButton, 1, 5)

        # Input memo widget for user
        self.memo = QLabel('Memo:')
        self.memoInput = QTextEdit()
        self.memoInput.setAlignment(Qt.AlignLeft)
        font = self.memo.font()
        font.setPointSize(font.pointSize() + 2)
        self.memo.setFont(font)
        self.memoInput.setFont(font)
        recordLayout.addWidget(self.memo, 2, 0, 1, 6)
        recordLayout.addWidget(self.memoInput, 3, 0, 1, 6)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(bookdiaryLayout, 0, 0)
        mainLayout.addLayout(recordLayout, 1, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle('DOKU - Book Diary')

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    bookdiary = BookDiary()
    bookdiary.show()
    sys.exit(app.exec_())