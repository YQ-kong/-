import sys
import os
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QScreen

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.file_path = ''
        self.processed_content = ''
        self.saved_file_path = ''

    def initUI(self):
        self.setWindowTitle('文本处理程序')
        self.setLayout(QVBoxLayout())

        self.open_button = QPushButton('选择文件', self)
        self.open_button.clicked.connect(self.open_file)
        self.layout().addWidget(self.open_button)

        self.save_source_button = QPushButton('保存至源文件目录', self)
        self.save_source_button.clicked.connect(self.save_to_source)
        self.layout().addWidget(self.save_source_button)

        self.save_custom_button = QPushButton('保存到指定目录', self)
        self.save_custom_button.clicked.connect(self.save_to_custom)
        self.layout().addWidget(self.save_custom_button)

        self.open_saved_file_button = QPushButton('打开保存的文件', self)
        self.open_saved_file_button.clicked.connect(self.open_saved_file)
        self.layout().addWidget(self.open_saved_file_button)

        self.status_label = QLabel('', self)
        self.layout().addWidget(self.status_label)

        self.center_window()

    def center_window(self):
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        window_width = int(screen.width() * 0.25)
        window_height = int(screen.height() * 0.25)
        self.setGeometry((screen.width() - window_width) // 2, (screen.height() - window_height) // 2, window_width, window_height)

    def process_text(self, text):
        text = text.replace(" ", "").replace("\n", "")
        sentences = re.split(r'([。？！])', text)
        processed_text = ""
        for i in range(0, len(sentences) - 1, 2):
            processed_text += sentences[i] + sentences[i + 1] + "\n"
        return processed_text

    def read_file(self, file_path, encodings=['utf-8', 'gbk', 'gb2312', 'gb18030']):
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                continue
        raise ValueError("无法确定文件的编码。")

    def save_file(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        self.saved_file_path = file_path

    def open_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if self.file_path:
            content = self.read_file(self.file_path)
            self.processed_content = self.process_text(content)
            self.status_label.setText("文件已处理，选择保存位置。")

    def save_to_source(self):
        if self.file_path and self.processed_content:
            directory, filename = os.path.split(self.file_path)
            new_filename = "修改后" + filename
            new_filepath = os.path.join(directory, new_filename)
            self.save_file(new_filepath, self.processed_content)
            self.status_label.setText(f"文件已保存至: {new_filepath}")

    def save_to_custom(self):
        if self.file_path and self.processed_content:
            directory = QFileDialog.getExistingDirectory(self, "选择目录")
            if directory:
                new_filename = "修改后" + os.path.basename(self.file_path)
                new_filepath = os.path.join(directory, new_filename)
                self.save_file(new_filepath, self.processed_content)
                self.status_label.setText(f"文件已保存至: {new_filepath}")

    def open_saved_file(self):
        if self.saved_file_path:
            os.startfile(self.saved_file_path)
        else:
            self.status_label.setText("没有已保存的文件可打开。")

if __name__ == '__main__':
    # 高DPI支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())
