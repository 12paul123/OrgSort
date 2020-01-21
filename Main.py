# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from multiprocessing import Queue, Process
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from directory_class import Directory
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setEnabled(True)
		MainWindow.resize(625, 437)
		MainWindow.setDockNestingEnabled(False)

		self.queue = Queue()

		self.Dirs = Directory(self.queue)
		self.Dirs.scan_work_path()
		self.Dirs.scan_inner_work_path()
		self.Dirs.scan_file_path()
		
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.Directorys = QtWidgets.QTreeView(self.centralwidget)
		self.Directorys.setGeometry(QtCore.QRect(40, 30, 161, 281))
		self.Directorys.setObjectName("Directorys")
		self.file_directory(True)

		self.FileCheck = QtWidgets.QCheckBox(self.centralwidget)
		self.FileCheck.setGeometry(QtCore.QRect(40, 320, 81, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.FileCheck.setFont(font)
		self.FileCheck.setObjectName("FileCheck")
		self.FileCheck.stateChanged.connect(self.file_box)

		self.ProgressOrganize = QtWidgets.QProgressBar(self.centralwidget)
		self.ProgressOrganize.setGeometry(QtCore.QRect(40, 350, 591, 31))
		self.ProgressOrganize.setProperty("value", 0)
		self.ProgressOrganize.setObjectName("ProgressOrganize")

		self.FileDir = QtWidgets.QLineEdit(self.centralwidget)
		self.FileDir.setEnabled(True)
		self.FileDir.setGeometry(QtCore.QRect(230, 40, 271, 20))
		self.FileDir.setText(self.Dirs.file_path)
		self.FileDir.setMaxLength(100)
		self.FileDir.setObjectName("FileDir")
		self.ChangeFileDir = QtWidgets.QPushButton(self.centralwidget)
		self.ChangeFileDir.setGeometry(QtCore.QRect(520, 40, 75, 23))
		self.ChangeFileDir.setObjectName("ChangeFileDir")
		self.ChangeFileDir.clicked.connect(self.change_file_path)

		self.WorkDir = QtWidgets.QLineEdit(self.centralwidget)
		self.WorkDir.setGeometry(QtCore.QRect(230, 100, 271, 20))
		self.WorkDir.setText(self.Dirs.work_path)
		self.WorkDir.setMaxLength(100)
		self.WorkDir.setObjectName("WorkDir")
		self.ChangeWorkDir = QtWidgets.QPushButton(self.centralwidget)
		self.ChangeWorkDir.setGeometry(QtCore.QRect(520, 100, 75, 21))
		self.ChangeWorkDir.setObjectName("ChangeWorkDir")
		self.ChangeWorkDir.clicked.connect(self.change_work_path)

		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(230, 80, 111, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_2.setFont(font)
		self.label_2.setMidLineWidth(0)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(230, 20, 111, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(40, 10, 91, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label.setFont(font)
		self.label.setObjectName("label")

		self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.stackedWidget.setGeometry(QtCore.QRect(220, 200, 371, 121))
		self.stackedWidget.setObjectName("stackedWidget")
		self.page = QtWidgets.QWidget()
		self.page.setObjectName("page")

		self.PrefixType = QtWidgets.QComboBox(self.page)
		self.PrefixType.setEnabled(True)
		self.PrefixType.setGeometry(QtCore.QRect(290, 30, 81, 21))
		self.PrefixType.setObjectName("PrefixType")
		self.PrefixType.addItem("")
		self.PrefixType.addItem("")
		self.PrefixType.addItem("")
		self.PrefixName = QtWidgets.QLineEdit(self.page)
		self.PrefixName.setGeometry(QtCore.QRect(170, 30, 101, 20))
		self.PrefixName.setObjectName("PrefixName")

		self.DirName = QtWidgets.QLineEdit(self.page)
		self.DirName.setEnabled(False)
		self.DirName.setGeometry(QtCore.QRect(10, 30, 141, 20))
		self.DirName.setMaxLength(16)
		self.DirName.setClearButtonEnabled(False)
		self.DirName.setObjectName("DirName")
		self.DirName_Radio = QtWidgets.QRadioButton(self.page)
		self.DirName_Radio.setEnabled(True)
		self.DirName_Radio.setGeometry(QtCore.QRect(10, 10, 121, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.DirName_Radio.setFont(font)
		self.DirName_Radio.setAutoFillBackground(False)
		self.DirName_Radio.setCheckable(True)
		self.DirName_Radio.setChecked(False)
		self.DirName_Radio.setAutoExclusive(False)
		self.DirName_Radio.setObjectName("DirName_Radio")
		self.DirName_Radio.toggled.connect(self.dir_name)

		self.label_6 = QtWidgets.QLabel(self.page)
		self.label_6.setGeometry(QtCore.QRect(170, 10, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")

		self.CreateDir = QtWidgets.QPushButton(self.page)
		self.CreateDir.setGeometry(QtCore.QRect(180, 90, 151, 21))
		font = QtGui.QFont()
		font.setPointSize(8)
		self.CreateDir.setFont(font)
		self.CreateDir.setObjectName("CreateDir")
		self.CreateDir.clicked.connect(self.create_dir)

		self.DeleteDir = QtWidgets.QPushButton(self.page)
		self.DeleteDir.setGeometry(QtCore.QRect(10, 90, 151, 21))
		self.DeleteDir.setObjectName("DeleteDir")
		self.DeleteDir.clicked.connect(self.delete_dir)

		self.label_5 = QtWidgets.QLabel(self.page)
		self.label_5.setGeometry(QtCore.QRect(290, 10, 71, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")

		self.DestroyCheck = QtWidgets.QCheckBox(self.page)
		self.DestroyCheck.setGeometry(QtCore.QRect(10, 60, 91, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.DestroyCheck.setFont(font)
		self.DestroyCheck.setObjectName("DestroyCheck")

		self.OrganizeCheck = QtWidgets.QCheckBox(self.page)
		self.OrganizeCheck.setGeometry(QtCore.QRect(180, 60, 101, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.OrganizeCheck.setFont(font)
		self.OrganizeCheck.setObjectName("OrganizeCheck")


		self.stackedWidget.addWidget(self.page)
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setObjectName("page_2")
		self.PrefixName_3 = QtWidgets.QLineEdit(self.page_2)
		self.PrefixName_3.setGeometry(QtCore.QRect(170, 30, 101, 20))
		self.PrefixName_3.setObjectName("PrefixName_3")
		self.label_8 = QtWidgets.QLabel(self.page_2)
		self.label_8.setGeometry(QtCore.QRect(170, 10, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")

		self.DirName_3 = QtWidgets.QLineEdit(self.page_2)
		self.DirName_3.setEnabled(False)
		self.DirName_3.setGeometry(QtCore.QRect(10, 30, 141, 20))
		self.DirName_3.setMaxLength(16)
		self.DirName_3.setClearButtonEnabled(False)
		self.DirName_3.setObjectName("DirName_3")
		self.DirName_Radio_3 = QtWidgets.QRadioButton(self.page_2)
		self.DirName_Radio_3.setEnabled(True)
		self.DirName_Radio_3.setGeometry(QtCore.QRect(10, 10, 121, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.DirName_Radio_3.setFont(font)
		self.DirName_Radio_3.setAutoFillBackground(False)
		self.DirName_Radio_3.setCheckable(True)
		self.DirName_Radio_3.setChecked(False)
		self.DirName_Radio_3.setAutoExclusive(False)
		self.DirName_Radio_3.setObjectName("DirName_Radio_3")
		self.DirName_Radio_3.toggled.connect(self.dir_name_3)

		self.PrefixType_3 = QtWidgets.QComboBox(self.page_2)
		self.PrefixType_3.setEnabled(True)
		self.PrefixType_3.setGeometry(QtCore.QRect(290, 30, 81, 21))
		self.PrefixType_3.setObjectName("PrefixType_3")
		self.PrefixType_3.addItem("")
		self.PrefixType_3.addItem("")
		self.PrefixType_3.addItem("")

		self.label_9 = QtWidgets.QLabel(self.page_2)
		self.label_9.setGeometry(QtCore.QRect(290, 10, 71, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_9.setFont(font)
		self.label_9.setObjectName("label_9")

		self.Search = QtWidgets.QPushButton(self.page_2)
		self.Search.setGeometry(QtCore.QRect(10, 70, 361, 41))
		self.Search.setObjectName("Search")
		self.Search.clicked.connect(self.search)

		self.stackedWidget.addWidget(self.page_2)
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")

		self.PrefixType_2 = QtWidgets.QComboBox(self.page_3)
		self.PrefixType_2.setEnabled(False)
		self.PrefixType_2.setGeometry(QtCore.QRect(290, 30, 81, 21))
		self.PrefixType_2.setObjectName("PrefixType_2")
		self.PrefixType_2.addItem("")
		self.PrefixType_2.addItem("")
		self.PrefixType_2.addItem("")
		self.PrefixType_Radio_2 = QtWidgets.QRadioButton(self.page_3)
		self.PrefixType_Radio_2.setGeometry(QtCore.QRect(290, 10, 81, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.PrefixType_Radio_2.setFont(font)
		self.PrefixType_Radio_2.setAutoRepeat(False)
		self.PrefixType_Radio_2.setAutoExclusive(False)
		self.PrefixType_Radio_2.setObjectName("PrefixType_Radio_2")
		self.PrefixType_Radio_2.toggled.connect(self.prefix_type_2)

		self.PrefixName_2 = QtWidgets.QLineEdit(self.page_3)
		self.PrefixName_2.setEnabled(False)
		self.PrefixName_2.setGeometry(QtCore.QRect(170, 30, 101, 20))
		self.PrefixName_2.setObjectName("PrefixName_2")
		self.PrefixName_Radio_2 = QtWidgets.QRadioButton(self.page_3)
		self.PrefixName_Radio_2.setGeometry(QtCore.QRect(170, 10, 51, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.PrefixName_Radio_2.setFont(font)
		self.PrefixName_Radio_2.setAutoExclusive(False)
		self.PrefixName_Radio_2.setObjectName("PrefixName_Radio_2")
		self.PrefixName_Radio_2.toggled.connect(self.prefix_name_2)

		self.FileName_2 = QtWidgets.QLineEdit(self.page_3)
		self.FileName_2.setEnabled(False)
		self.FileName_2.setGeometry(QtCore.QRect(10, 30, 141, 20))
		self.FileName_2.setObjectName("FileName_2")
		self.FileName_Radio_2 = QtWidgets.QRadioButton(self.page_3)
		self.FileName_Radio_2.setGeometry(QtCore.QRect(10, 10, 81, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.FileName_Radio_2.setFont(font)
		self.FileName_Radio_2.setAutoExclusive(False)
		self.FileName_Radio_2.setObjectName("FileName_Radio_2")
		self.FileName_Radio_2.toggled.connect(self.file_name_2)

		self.Organize = QtWidgets.QPushButton(self.page_3)
		self.Organize.setGeometry(QtCore.QRect(10, 70, 361, 41))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.Organize.setFont(font)
		self.Organize.setObjectName("Organize")
		self.Organize.clicked.connect(self.organize)

		self.stackedWidget.addWidget(self.page_3)
		self.Dir_folder_radio = QtWidgets.QRadioButton(self.centralwidget)
		self.Dir_folder_radio.setGeometry(QtCore.QRect(230, 140, 71, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.Dir_folder_radio.setFont(font)
		self.Dir_folder_radio.setAutoExclusive(False)
		self.Dir_folder_radio.setObjectName("Dir_folder_radio")
		self.Dir_folder = QtWidgets.QLineEdit(self.centralwidget)
		self.Dir_folder.setEnabled(False)
		self.Dir_folder.setGeometry(QtCore.QRect(230, 160, 141, 20))
		self.Dir_folder.setObjectName("Dir_folder")
		self.Dir_folder_radio.toggled.connect(self.dir_folder)

		self.Func = QtWidgets.QComboBox(self.centralwidget)
		self.Func.setGeometry(QtCore.QRect(390, 160, 69, 22))
		self.Func.setObjectName("Func")
		self.Func.addItem("")
		self.Func.addItem("")
		self.Func.addItem("")
		self.Func.activated[str].connect(self.page_change)

		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 21))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuHelp = QtWidgets.QMenu(self.menubar)
		self.menuHelp.setObjectName("menuHelp")
		self.menuHelp.triggered.connect(self.help)
		self.menuTools = QtWidgets.QMenu(self.menubar)
		self.menuTools.setObjectName("menuTools")
		MainWindow.setMenuBar(self.menubar)

		self.actionWork_Path = QtWidgets.QAction(MainWindow)
		self.actionWork_Path.setObjectName("actionWork_Path")
		self.actionWork_Path.triggered.connect(self.change_work_path)

		self.actionFile_Path = QtWidgets.QAction(MainWindow)
		self.actionFile_Path.setObjectName("actionFile_Path")
		self.actionFile_Path.triggered.connect(self.change_file_path)

		self.actionPrefix = QtWidgets.QAction(MainWindow)
		self.actionPrefix.setObjectName("actionPrefix")
		self.actionPrefix.triggered.connect(self.combo_prefix)

		self.actionSearch = QtWidgets.QAction(MainWindow)
		self.actionSearch.setObjectName("actionSearch")
		self.actionSearch.triggered.connect(self.combo_search)

		self.actionOrganize = QtWidgets.QAction(MainWindow)
		self.actionOrganize.setObjectName("actionOrganize")
		self.actionOrganize.triggered.connect(self.combo_organize)

		self.actionShow_FIles = QtWidgets.QAction(MainWindow)
		self.actionShow_FIles.setObjectName("actionShow_FIles")
		self.actionShow_FIles.triggered.connect(self.file_box)

		self.menuFile.addAction(self.actionWork_Path)
		self.menuFile.addAction(self.actionFile_Path)
		self.menuTools.addAction(self.actionPrefix)
		self.menuTools.addAction(self.actionOrganize)
		self.menuTools.addAction(self.actionSearch)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuTools.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.retranslateUi(MainWindow)
		self.stackedWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def help(self):
		print("Help")

	def combo_prefix(self):
		self.Func.setCurrentText("Prefix")
		self.page_change("Prefix")

	def combo_search(self):
		self.Func.setCurrentText("Search")
		self.page_change("Search")

	def combo_organize(self):
		self.Func.setCurrentText("Organize")
		self.page_change("Organize")

	def dir_name(self, state):
		if state == True:
			self.DirName.setEnabled(True)
		else: self.DirName.setEnabled(False)

	def dir_name_2(self, state):
		if state == True:
			self.DirName_2.setEnabled(True)
		else: self.DirName_2.setEnabled(False)

	def dir_name_3(self, state):
		if state == True:
			self.DirName_3.setEnabled(True)
		else: self.DirName_3.setEnabled(False)

	def prefix_name_2(self, state):
		if state == True:
			self.PrefixName_2.setEnabled(True)
		else: self.PrefixName_2.setEnabled(False)

	def prefix_type_2(self, state):
		if state == True:
			self.PrefixType_2.setEnabled(True)
		else: self.PrefixType_2.setEnabled(False)

	def dir_folder(self, state):
		if state == True:
			self.Dir_folder.setEnabled(True)
		else: self.Dir_folder.setEnabled(False)

	def file_name_2(self, state):
		if state == True:
			self.FileName_2.setEnabled(True)
		else: self.FileName_2.setEnabled(False)

	def file_box(self, state):
		if state == QtCore.Qt.Checked:
			self.file_directory(False)
		else: self.file_directory(True)

	def page_change(self, text):
		if text == "Prefix":
			self.stackedWidget.setCurrentIndex(0)
		elif text == "Organize":
			self.stackedWidget.setCurrentIndex(2)
		elif text == "Search":
			self.stackedWidget.setCurrentIndex(1)

	def create_dir(self):
		name = self.DirName.text()
		pref = self.PrefixName.text()
		pref_type = self.PrefixType.currentText()
		dir_name = self.Dir_folder.text()

		if not pref or not pref_type: return

		if not self.Dir_folder.isEnabled():
			if self.DirName.isEnabled():
				if pref_type == "End Prefix":
					self.Dirs.create_end_pref("", name, pref)
				elif pref_type == "Start Prefix":
					self.Dirs.create_start_pref("", name, pref)
				elif pref_type == "File Prefix":
					self.Dirs.create_file_pref("", name, pref)
			else:
				if pref_type == "End Prefix":
					self.Dirs.create_end_pref("", "", pref)
				elif pref_type == "Start Prefix":
					self.Dirs.create_start_pref("", "", pref)
				elif pref_type == "File Prefix":
					self.Dirs.create_file_pref("", "", pref)
		else:
			if self.DirName.isEnabled():
				if pref_type == "End Prefix":
					self.Dirs.create_end_pref(dir_name, name, pref)
				elif pref_type == "Start Prefix":
					self.Dirs.create_start_pref(dir_name, name, pref)
				elif pref_type == "File Prefix":
					self.Dirs.create_file_pref(dir_name, name, pref)
			else:
				if pref_type == "End Prefix":
					self.Dirs.create_end_pref(dir_name, "", pref)
				elif pref_type == "Start Prefix":
					self.Dirs.create_start_pref(dir_name, "", pref)
				elif pref_type == "File Prefix":
					self.Dirs.create_file_pref(dir_name, "", pref)

		self.Dirs.save_state()
		if self.OrganizeCheck.isChecked():
			self.Dirs.organize_prefix_type(pref, pref_type)

	def delete_dir(self):
		name = self.DirName.text()
		pref = self.PrefixName.text()
		pref_type = self.PrefixType.currentText()
		folder_2 = self.Dir_folder.text()

		if not pref or not pref_type: return

		if not self.DestroyCheck.isChecked():
			if self.Dir_folder.isEnabled():
				if self.DirName.isEnabled():
					self.Dirs.move_deep_files(folder_2, name)
				else: self.Dirs.move_deep_files(folder_2, name)
			else:
				if self.DirName.isEnabled():
					self.Dirs.move_inner_files(pref, pref_type)
				else: self.Dirs.move_inner_files(pref, pref_type)

		if self.DirName.isEnabled():
			if pref_type == "End Prefix":
				self.Dirs.delete_end_pref(name, pref)
			elif pref_type == "Start Prefix":
				self.Dirs.delete_start_pref(name, pref)
			elif pref_type == "File Prefix":
				self.Dirs.delete_file_pref(name, pref)
		else:
			if pref_type == "End Prefix":
				self.Dirs.delete_end_pref("", pref)
			elif pref_type == "Start Prefix":
				self.Dirs.delete_start_pref("", pref)
			elif pref_type == "File Prefix":
				self.Dirs.delete_file_pref("", pref)

		self.Dirs.save_state()

	def progress(self):
		path = ""
		while True:
			try:
				data = self.queue.get(timeout=0.01)
			except:
				if data == 0:
					print(data)
					self.ProgressOrganize.setProperty("value", 0)
					break
				elif str(data) == data:
					path = data
					msg = QMessageBox()
					msg.setIcon(QMessageBox.Information)
					msg.setText("Path: " + path)
					msg.setWindowTitle("Search")
					msg.show()
					msg.exec_()
					self.ProgressOrganize.setProperty("value", 0)
					break

			if not data >= 100:
				self.ProgressOrganize.setProperty("value", data)
				time.sleep(0.05)

	def organize(self):
		prefix = self.PrefixName_2.text()
		prefix_type = self.PrefixType_2.currentText()
		file_name = self.FileName_2.text()

		if not self.FileName_2.isEnabled() and self.PrefixName_2.isEnabled() \
				and self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_prefix_type, args=(prefix, prefix_type,)).start()

		elif not self.FileName_2.isEnabled() and not self.PrefixName_2.isEnabled() \
				and self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_type, args=(prefix_type,)).start()

		elif not self.FileName_2.isEnabled() and self.PrefixName_2.isEnabled() \
				and not self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_prefix, args=(prefix,)).start()

		elif self.FileName_2.isEnabled() and not self.PrefixName_2.isEnabled() \
				and not self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_file, args=(file_name,)).start()

		elif self.FileName_2.isEnabled() and self.PrefixName_2.isEnabled() \
				and not self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_file_prefix, args=(file_name, prefix,)).start()

		elif self.FileName_2.isEnabled() and not self.PrefixName_2.isEnabled() \
				and self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_file_type, args=(file_name, prefix_type,)).start()

		elif self.FileName_2.isEnabled() and self.PrefixName_2.isEnabled() \
				and self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_file_prefix_type, args=(file_name, prefix, prefix_type,)).start()

		elif not self.FileName_2.isEnabled() and not self.PrefixName_2.isEnabled() \
				and not self.PrefixType_2.isEnabled():
			Process(target=self.Dirs.organize_files).start()
		
		self.progress()
		self.progress()

	def search(self):
		name = self.DirName_3.text()
		pref = self.PrefixName_3.text()
		pref_type = self.PrefixType_3.currentText()
		
		if self.DirName_Radio_3.isChecked() == False:
			print("Search files")
			p = Process(target=self.Dirs.search_files, args=(pref,)).start()
			# Get folder path
		elif self.DirName_Radio_3.isChecked() == True:
			print("Search file")
			p = Process(target=self.Dirs.search_file, args=(name,)).start()
			# Get file path
		
		self.progress()

	def change_work_path(self):
		path = self.WorkDir.text()
		self.Dirs.work_new_path(path)

	def change_file_path(self):
		path = self.FileDir.text()
		self.Dirs.file_new_path(path)

	def file_directory(self, check):
		path = self.Dirs.work_path
		model = QtWidgets.QFileSystemModel()
		model.setRootPath(QtCore.QDir.rootPath())
		if check == True:
			model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
		else: model.setFilter(QDir.NoDotAndDotDot |  QDir.Files | QDir.AllDirs)
		self.Directorys.setModel(model)
		self.Directorys.setRootIndex(model.index(path))
		self.Directorys.hideColumn(1)
		self.Directorys.hideColumn(2)
		self.Directorys.hideColumn(3)
		self.Directorys.setSortingEnabled(True)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.FileCheck.setText(_translate("MainWindow", "Show Files"))
		self.ChangeFileDir.setText(_translate("MainWindow", "Change"))
		self.ChangeWorkDir.setText(_translate("MainWindow", "Change"))
		self.label_2.setText(_translate("MainWindow", "Work Directory"))
		self.label_3.setText(_translate("MainWindow", "File Directory"))
		self.label.setText(_translate("MainWindow", "Work Directory"))
		self.PrefixType.setItemText(0, _translate("MainWindow", "End Prefix"))
		self.PrefixType.setItemText(1, _translate("MainWindow", "File Prefix"))
		self.PrefixType.setItemText(2, _translate("MainWindow", "Start Prefix"))
		self.label_6.setText(_translate("MainWindow", "Prefix"))
		self.DirName_Radio.setText(_translate("MainWindow", "Directory Name"))
		self.CreateDir.setText(_translate("MainWindow", "Create"))
		self.DeleteDir.setText(_translate("MainWindow", "Delete"))
		self.label_5.setText(_translate("MainWindow", "Prefix Type"))
		self.DestroyCheck.setText(_translate("MainWindow", "Destroy Files"))
		self.OrganizeCheck.setText(_translate("MainWindow", "Organize Files"))
		self.label_8.setText(_translate("MainWindow", "Prefix"))
		self.DirName_Radio_3.setText(_translate("MainWindow", "File Name"))
		self.PrefixType_3.setItemText(0, _translate("MainWindow", "End Prefix"))
		self.PrefixType_3.setItemText(1, _translate("MainWindow", "File Prefix"))
		self.PrefixType_3.setItemText(2, _translate("MainWindow", "Start Prefix"))
		self.label_9.setText(_translate("MainWindow", "Prefix Type"))
		self.Search.setText(_translate("MainWindow", "Search"))
		self.PrefixName_Radio_2.setText(_translate("MainWindow", "Prefix"))
		self.PrefixType_2.setItemText(0, _translate("MainWindow", "End Prefix"))
		self.PrefixType_2.setItemText(1, _translate("MainWindow", "File Prefix"))
		self.PrefixType_2.setItemText(2, _translate("MainWindow", "Start Prefix"))
		self.PrefixType_Radio_2.setText(_translate("MainWindow", "Prefix Type"))
		self.FileName_Radio_2.setText(_translate("MainWindow", "File Name"))
		self.Organize.setText(_translate("MainWindow", "Organize"))
		self.Dir_folder_radio.setText(_translate("MainWindow", "Directory"))
		self.Func.setItemText(0, _translate("MainWindow", "Prefix"))
		self.Func.setItemText(1, _translate("MainWindow", "Organize"))
		self.Func.setItemText(2, _translate("MainWindow", "Search"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuHelp.setTitle(_translate("MainWindow", "Help"))
		self.menuTools.setTitle(_translate("MainWindow", "Tools"))
		self.actionWork_Path.setText(_translate("MainWindow", "Work Path"))
		self.actionWork_Path.setStatusTip(_translate("MainWindow", "Change Working Directory"))
		self.actionWork_Path.setShortcut(_translate("MainWindow", "Ctrl+W"))
		self.actionFile_Path.setText(_translate("MainWindow", "File Path"))
		self.actionFile_Path.setStatusTip(_translate("MainWindow", "Change File Directory"))
		self.actionFile_Path.setShortcut(_translate("MainWindow", "Ctrl+F"))
		self.actionPrefix.setText(_translate("MainWindow", "Prefix"))
		self.actionPrefix.setShortcut(_translate("MainWindow", "Ctrl+P"))
		self.actionSearch.setText(_translate("MainWindow", "Search"))
		self.actionSearch.setShortcut(_translate("MainWindow", "Ctrl+I"))
		self.actionOrganize.setText(_translate("MainWindow", "Organize"))
		self.actionOrganize.setShortcut(_translate("MainWindow", "Ctrl+O"))
		self.actionShow_FIles.setText(_translate("MainWindow", "Show FIles"))
		self.actionShow_FIles.setShortcut(_translate("MainWindow", "Ctrl+Z"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.setWindowTitle("OrgSort")
	MainWindow.show()
	sys.exit(app.exec_())
