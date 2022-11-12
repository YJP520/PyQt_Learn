#
# Project : Learning PyQt
# Time : 2022/11/12
# Author : YU.J.P
#

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

app = QApplication([])

window = QMainWindow()  # 创建主窗口对象
window.resize(500, 400)  # 窗口大小
window.move(300, 310)  # 窗口位置
window.setWindowTitle('薪资统计')  # 窗口名称

textEdit = QPlainTextEdit(window)  # 文本编辑框
textEdit.setPlaceholderText("请输入薪资表")  # 提示文本
textEdit.move(10, 25)  # 编辑框位置
textEdit.resize(300, 350)  # 编辑框大小

button = QPushButton('统计', window)  # 按钮对象
button.move(380, 80)  # 按钮位置

window.show()  # 展现

app.exec_()  # 事件处理循环
