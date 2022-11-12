#
# Project : Learning PyQt
# Time : 2022/11/12
# Author : YU.J.P
#

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


def handleCalc():
    info = textEdit.toPlainText()

    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
    \n薪资20000 以下的有：\n{salary_below_20k}''')  # 弹出对话框


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
button.clicked.connect(handleCalc)

window.show()  # 展现

app.exec_()  # 事件处理循环
