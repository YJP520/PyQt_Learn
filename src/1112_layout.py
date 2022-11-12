#
# Project : Learning PyQt
# Time : 2022/11/12
# Author : YU.J.P
#

from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class Create_1:

    def __init__(self):
        # 从文件中加载UI定义
        qfile = QFile('../ui/create_1.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile)

        # 搜索按钮绑定
        self.ui.pushButton_search.clicked.connect(self.handle_search)
        # 更新按钮绑定
        self.ui.pushButton_update.clicked.connect(self.handle_update)
        # 删除按钮绑定
        self.ui.pushButton_delete.clicked.connect(self.handle_delete)

    def handle_search(self):
        # 获取输入框的信息
        url = self.ui.lineEdit_input.text()

        # 提示信息
        QMessageBox.about(self.ui, '提示', f'''URL:\n{url}''')

    def handle_update(self):
        # 提示信息
        QMessageBox.about(self.ui, '提示', f'''成功加载文本框信息！''')

    def handle_delete(self):
        # 提示信息
        QMessageBox.about(self.ui, '提示', f'''成功清除文本框信息！''')


# MAIN
if __name__ == '__main__':
    app = QApplication([])
    create = Create_1()
    create.ui.show()
    app.exec_()
