# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prachecker.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PRAChecker(object):
    def setupUi(self, PRAChecker):
        PRAChecker.setObjectName("PRAChecker")
        PRAChecker.resize(501, 507)
        self.centralwidget = QtWidgets.QWidget(PRAChecker)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_status = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_status.setGeometry(QtCore.QRect(20, 70, 411, 23))
        self.pb_status.setProperty("value", 24)
        self.pb_status.setObjectName("pb_status")
        self.btn_check_sample = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check_sample.setGeometry(QtCore.QRect(150, 10, 181, 23))
        self.btn_check_sample.setObjectName("btn_check_sample")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 120, 417, 112))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 3, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 5, 3, 1)
        self.spin_box_min_ad_class1 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_min_ad_class1.setObjectName("spin_box_min_ad_class1")
        self.gridLayout.addWidget(self.spin_box_min_ad_class1, 0, 7, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.spin_box_ad_class1 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_ad_class1.setObjectName("spin_box_ad_class1")
        self.verticalLayout_5.addWidget(self.spin_box_ad_class1)
        self.spin_box_ad_control = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_ad_control.setObjectName("spin_box_ad_control")
        self.verticalLayout_5.addWidget(self.spin_box_ad_control)
        self.spin_box_ad_class2 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_ad_class2.setObjectName("spin_box_ad_class2")
        self.verticalLayout_5.addWidget(self.spin_box_ad_class2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 4, 3, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 6, 3, 1)
        self.spin_box_min_ad_control = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_min_ad_control.setObjectName("spin_box_min_ad_control")
        self.gridLayout.addWidget(self.spin_box_min_ad_control, 1, 7, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 3, 1)
        self.spin_box_min_ad_class2 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_min_ad_class2.setObjectName("spin_box_min_ad_class2")
        self.gridLayout.addWidget(self.spin_box_min_ad_class2, 2, 7, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spin_box_mean_class1 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_mean_class1.setObjectName("spin_box_mean_class1")
        self.verticalLayout.addWidget(self.spin_box_mean_class1)
        self.spin_box_mean_control = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_mean_control.setObjectName("spin_box_mean_control")
        self.verticalLayout.addWidget(self.spin_box_mean_control)
        self.spin_box_mean_class2 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_box_mean_class2.setObjectName("spin_box_mean_class2")
        self.verticalLayout.addWidget(self.spin_box_mean_class2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 3, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 240, 421, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkbox_ks_testing = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_ks_testing.setGeometry(QtCore.QRect(20, 70, 221, 16))
        self.checkbox_ks_testing.setObjectName("checkbox_ks_testing")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 40, 42, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 40, 41, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.spin_box_min_ad_ks_class1 = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spin_box_min_ad_ks_class1.setObjectName("spin_box_min_ad_ks_class1")
        self.verticalLayout_9.addWidget(self.spin_box_min_ad_ks_class1)
        self.spin_box_min_ad_ks_control = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spin_box_min_ad_ks_control.setObjectName("spin_box_min_ad_ks_control")
        self.verticalLayout_9.addWidget(self.spin_box_min_ad_ks_control)
        self.spin_box_min_ad_ks_class2 = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spin_box_min_ad_ks_class2.setObjectName("spin_box_min_ad_ks_class2")
        self.verticalLayout_9.addWidget(self.spin_box_min_ad_ks_class2)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(350, 20, 47, 13))
        self.label_19.setObjectName("label_19")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(390, 40, 21, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_10.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_10.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_10.addWidget(self.label_22)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 40, 41, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spin_box_ks_class1 = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spin_box_ks_class1.setObjectName("spin_box_ks_class1")
        self.gridLayout_2.addWidget(self.spin_box_ks_class1, 0, 0, 1, 1)
        self.spin_box_ks_control = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spin_box_ks_control.setObjectName("spin_box_ks_control")
        self.gridLayout_2.addWidget(self.spin_box_ks_control, 1, 0, 1, 1)
        self.spin_box_ks_class2 = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spin_box_ks_class2.setObjectName("spin_box_ks_class2")
        self.gridLayout_2.addWidget(self.spin_box_ks_class2, 2, 0, 1, 1)
        PRAChecker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PRAChecker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        PRAChecker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PRAChecker)
        self.statusbar.setObjectName("statusbar")
        PRAChecker.setStatusBar(self.statusbar)
        self.menu_folder_monitor = QtWidgets.QAction(PRAChecker)
        self.menu_folder_monitor.setObjectName("menu_folder_monitor")
        self.menu_database_rebuilder = QtWidgets.QAction(PRAChecker)
        self.menu_database_rebuilder.setObjectName("menu_database_rebuilder")
        self.menu_ouput_folder = QtWidgets.QAction(PRAChecker)
        self.menu_ouput_folder.setObjectName("menu_ouput_folder")
        self.menu_acquire_FCS_Files = QtWidgets.QAction(PRAChecker)
        self.menu_acquire_FCS_Files.setObjectName("menu_acquire_FCS_Files")
        self.menuSettings.addAction(self.menu_folder_monitor)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menu_database_rebuilder)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menu_ouput_folder)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menu_acquire_FCS_Files)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(PRAChecker)
        QtCore.QMetaObject.connectSlotsByName(PRAChecker)

    def retranslateUi(self, PRAChecker):
        _translate = QtCore.QCoreApplication.translate
        PRAChecker.setWindowTitle(_translate("PRAChecker", "PRAChecker"))
        self.btn_check_sample.setText(_translate("PRAChecker", "Check New Samples"))
        self.groupBox.setTitle(_translate("PRAChecker", "Delta Check Setting"))
        self.label_2.setText(_translate("PRAChecker", "%"))
        self.label_6.setText(_translate("PRAChecker", "%"))
        self.label_10.setText(_translate("PRAChecker", "%"))
        self.label_4.setText(_translate("PRAChecker", "Fold"))
        self.label_8.setText(_translate("PRAChecker", "Fold"))
        self.label_12.setText(_translate("PRAChecker", "Fold"))
        self.label_13.setText(_translate("PRAChecker", "Minimum AD:"))
        self.label_14.setText(_translate("PRAChecker", "Minimum AD:"))
        self.label_15.setText(_translate("PRAChecker", "Minimum AD:"))
        self.label.setText(_translate("PRAChecker", "Mean Class I MFI:"))
        self.label_5.setText(_translate("PRAChecker", "Mean  Control MFI:"))
        self.label_9.setText(_translate("PRAChecker", "Mean  Class II MFI:"))
        self.label_3.setText(_translate("PRAChecker", "Class I AD:"))
        self.label_7.setText(_translate("PRAChecker", "Control AD:"))
        self.label_11.setText(_translate("PRAChecker", "Class II AD:"))
        self.groupBox_2.setTitle(_translate("PRAChecker", "advanced settings"))
        self.checkbox_ks_testing.setText(_translate("PRAChecker", "Kolmogorov???Smirnov test  if AD exceed"))
        self.label_16.setText(_translate("PRAChecker", "Class I:"))
        self.label_18.setText(_translate("PRAChecker", "Control:"))
        self.label_17.setText(_translate("PRAChecker", "Class II:"))
        self.label_19.setText(_translate("PRAChecker", "k-S test"))
        self.label_20.setText(_translate("PRAChecker", "%"))
        self.label_21.setText(_translate("PRAChecker", "%"))
        self.label_22.setText(_translate("PRAChecker", "%"))
        self.menuSettings.setTitle(_translate("PRAChecker", "Settings"))
        self.menu_folder_monitor.setText(_translate("PRAChecker", "Folder To Monitor"))
        self.menu_database_rebuilder.setText(_translate("PRAChecker", "Database Rebuild"))
        self.menu_ouput_folder.setText(_translate("PRAChecker", "Output Folder"))
        self.menu_acquire_FCS_Files.setText(_translate("PRAChecker", "Acquire FCS Files"))

