# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DependencyViewer.ui'
#
# Created: Wed Dec  5 00:42:13 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlg_DependencyViewer(object):
    def setupUi(self, dlg_DependencyViewer):
        dlg_DependencyViewer.setObjectName("dlg_DependencyViewer")
        dlg_DependencyViewer.resize(1555, 412)
        self.verticalLayout = QtGui.QVBoxLayout(dlg_DependencyViewer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtGui.QWidget(dlg_DependencyViewer)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.widget_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.e_search = QtGui.QLineEdit(self.widget)
        self.e_search.setObjectName("e_search")
        self.horizontalLayout.addWidget(self.e_search)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_2)
        self.l_root = QtGui.QLabel(dlg_DependencyViewer)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_root.setFont(font)
        self.l_root.setText("")
        self.l_root.setObjectName("l_root")
        self.verticalLayout.addWidget(self.l_root)
        self.tw_dependencies = QtGui.QTreeWidget(dlg_DependencyViewer)
        self.tw_dependencies.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_dependencies.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tw_dependencies.setObjectName("tw_dependencies")
        self.tw_dependencies.headerItem().setText(0, "1")
        self.tw_dependencies.header().setVisible(True)
        self.verticalLayout.addWidget(self.tw_dependencies)

        self.retranslateUi(dlg_DependencyViewer)
        QtCore.QMetaObject.connectSlotsByName(dlg_DependencyViewer)

    def retranslateUi(self, dlg_DependencyViewer):
        dlg_DependencyViewer.setWindowTitle(QtGui.QApplication.translate("dlg_DependencyViewer", "Dependency Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlg_DependencyViewer", "The asets in the list were used to create:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlg_DependencyViewer", "Search:", None, QtGui.QApplication.UnicodeUTF8))

