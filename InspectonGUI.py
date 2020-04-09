# -*- coding: utf-8 -*-
#Disclaimer:
# Furkan Ülger, Seniha Esen Yüksel
# Department of Electrical and Electronics Engineering
# Hacettepe University
# Ankara, Turkey
# furkan.ulger@outlook.com
#Please give reference to the research paper if you are willing to use.
# https://ieeexplore.ieee.org/abstract/document/8936659

from PyQt4 import QtCore, QtGui
import cv2
import numpy as np
import pytesseract
import imutils
from PIL import Image
from matplotlib import pyplot as plt
import sys
from BoardSelect import Ui_Dialog

import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_mainWindow(object):


    def select_bareboard(self):

        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

        pathway_temp_1 = r'BOARD LIBRARY\Bare\bare_1 Template board image.JPEG'
        pathway_def_1 = r'BOARD LIBRARY\Bare\bare_1 Defective board image.JPEG'
        self.ui.number_1.clicked.connect(self.Dialog.close)
        self.ui.number_1.clicked.connect(lambda: self.CaptureFrame_bare(pathway_temp_1,pathway_def_1))


        pathway_temp_2 = r'BOARD LIBRARY\Bare\bare_2 Template board image.JPEG'
        pathway_def_2 = r'BOARD LIBRARY\Bare\bare_2 Defective board image.JPEG'
        self.ui.number_2.clicked.connect(self.Dialog.close)
        self.ui.number_2.clicked.connect(lambda:self.CaptureFrame_bare(pathway_temp_2,pathway_def_2))

        pathway_temp_3 = r'BOARD LIBRARY\Bare\bare_3 Template board image.JPEG'
        pathway_def_3 = r'BOARD LIBRARY\Bare\bare_3 Defective board image.JPEG'
        self.ui.number_3.clicked.connect(self.Dialog.close)
        self.ui.number_3.clicked.connect(lambda:self.CaptureFrame_bare(pathway_temp_3,pathway_def_3))

    def select_assembledboard(self):

        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        pathway_temp_1 = r'BOARD LIBRARY\Assembled\assemb_1 Template board image.JPEG'
        pathway_def_1 = r'BOARD LIBRARY\Assembled\assemb_1 Defective board image.JPEG'

        self.ui.number_1.clicked.connect(self.Dialog.close)
        self.ui.number_1.clicked.connect(lambda: self.CaptureFrame_assemb(pathway_temp_1,pathway_def_1))

        pathway_temp_2 = r'BOARD LIBRARY\Assembled\assemb_2 Template board image.JPEG'
        pathway_def_2 = r'BOARD LIBRARY\Assembled\assemb_2 Defective board image.JPEG'

        self.ui.number_2.clicked.connect(self.Dialog.close)
        self.ui.number_2.clicked.connect(lambda:self.CaptureFrame_assemb(pathway_temp_2,pathway_def_2))

        pathway_temp_3 = r'BOARD LIBRARY\Assembled\assemb_3 Template board image.JPEG'
        pathway_def_3 = r'BOARD LIBRARY\Assembled\assemb_3 Defective board image.JPEG'

        self.ui.number_3.clicked.connect(self.Dialog.close)
        self.ui.number_3.clicked.connect(lambda:self.CaptureFrame_assemb(pathway_temp_3,pathway_def_3))


    def select_solder(self):

        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


        pathway_temp_1 = r'BOARD LIBRARY\Solder\solder_1 Template board image.JPEG'
        pathway_def_1 = r'BOARD LIBRARY\Solder\solder_1 Defective board image.JPEG'

        self.ui.number_1.clicked.connect(self.Dialog.close)
        self.ui.number_1.clicked.connect(lambda: self.CaptureFrame_solder(pathway_temp_1,pathway_def_1))

        pathway_temp_2 = r'BOARD LIBRARY\Solder\solder_2 Template board image.JPEG'
        pathway_def_2 = r'BOARD LIBRARY\Solder\solder_2 Defective board image.JPEG'

        self.ui.number_2.clicked.connect(self.Dialog.close)
        self.ui.number_2.clicked.connect(lambda:self.CaptureFrame_solder(pathway_temp_2,pathway_def_2))

        pathway_temp_3 = r'BOARD LIBRARY\Solder\solder_3 Template board image.JPEG'
        pathway_def_3 = r'BOARD LIBRARY\Solder\solder_3 Defective board image.JPEG'

        self.ui.number_3.clicked.connect(self.Dialog.close)
        self.ui.number_3.clicked.connect(lambda:self.CaptureFrame_solder(pathway_temp_3,pathway_def_3))


    def inspect_bare(self):

        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

        pathway_temp_lib = r'BOARD LIBRARY\Bare\bare_lib Template board image.JPEG'
        pathway_def_lib = r'BOARD LIBRARY\Bare\bare_lib Defective board image.JPEG'
        self.ui.library.clicked.connect(self.Dialog.close)
        self.ui.library.clicked.connect(lambda: self.bareboard_1(pathway_temp_lib,pathway_def_lib,drows=23,dcolumns=25,trows=30,tcolumns=30,pos_blur=7,neg_blur=7,blur_roi=7,num_iterate1=1,num_iterate2=2,num_iterate3=3))


        pathway_temp_1 = r'BOARD LIBRARY\Bare\bare_1 Template board image.JPEG'
        pathway_def_1 = r'BOARD LIBRARY\Bare\bare_1 Defective board image.JPEG'
        self.ui.number_1.clicked.connect(self.Dialog.close)
        self.ui.number_1.clicked.connect(lambda: self.bareboard_1(pathway_temp_1,pathway_def_1,drows=45,dcolumns=35,trows=45,tcolumns=35,pos_blur=5,neg_blur=7,blur_roi=3,num_iterate1=1,num_iterate2=1,num_iterate3=1))


        pathway_temp_2 = r'BOARD LIBRARY\Bare\bare_2 Template board image.JPEG'
        pathway_def_2 = r'BOARD LIBRARY\Bare\bare_2 Defective board image.JPEG'
        # self.ui.number_2.clicked.connect(lambda: self.bareboard_1(pathway_temp_2,pathway_def_2,drows=37,dcolumns=37,trows=37,tcolumns=37,posneg_blur=9,blur_roi=5))
        self.ui.number_2.clicked.connect(self.Dialog.close)
        self.ui.number_2.clicked.connect(lambda: self.bareboard_1(pathway_temp_2, pathway_def_2, drows=37, dcolumns=37, trows=37, tcolumns=37,pos_blur=7,neg_blur=7, blur_roi=3,num_iterate1=1,num_iterate2=1,num_iterate3=1))


        pathway_temp_3 = r'BOARD LIBRARY\Bare\bare_3 Template board image.JPEG'
        pathway_def_3 = r'BOARD LIBRARY\Bare\bare_3 Defective board image.JPEG'
        self.ui.number_3.clicked.connect(self.Dialog.close)
        self.ui.number_3.clicked.connect(lambda: self.bareboard_1(pathway_temp_3,pathway_def_3,drows=17,dcolumns=17,trows=30,tcolumns=30,pos_blur=9,neg_blur=9,blur_roi=3,num_iterate1=0,num_iterate2=0,num_iterate3=0))


    def inspect_assemb(self):
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

        pathway_temp_lib = r'BOARD LIBRARY\Assembled\assemb_lib Template board image.JPEG'
        pathway_def_lib = r'BOARD LIBRARY\Assembled\assemb_lib Defective board image.JPEG'
        self.ui.library.clicked.connect(self.Dialog.close)
        self.ui.library.clicked.connect(lambda: self.assembledBoard_1(pathway_temp_lib,pathway_def_lib,alignment=alignImages,threshold_mis=25,opening_mis = 2,thresh_fg_temp=170,thresh_fg_def=170,blur_roi=7,a_cspace=125,a_cspace_def=125,b_cspace_temp=100,b_cspace_def=100,open_it=8,close_it=10,pol_minArea = 150))




        pathway_temp_1 = r'BOARD LIBRARY\Assembled\assemb_1 Template board image.JPEG'
        pathway_def_1 = r'BOARD LIBRARY\Assembled\assemb_1 Defective board image.JPEG'
        self.ui.number_1.clicked.connect(self.Dialog.close)
        self.ui.number_1.clicked.connect(lambda: self.assembledBoard_1(pathway_temp_1,pathway_def_1,alignment=align_2,threshold_mis=70,opening_mis = 4,thresh_fg_temp=250,thresh_fg_def = 250,blur_roi=7,a_cspace=1,a_cspace_def=1,b_cspace_temp=123,b_cspace_def=123,open_it=1,close_it=1,pol_minArea = 499))


        pathway_temp_2 = r'BOARD LIBRARY\Assembled\assemb_2 Template board image.JPEG'
        pathway_def_2 = r'BOARD LIBRARY\Assembled\assemb_2 Defective board image.JPEG'
        self.ui.number_2.clicked.connect(self.Dialog.close)
        self.ui.number_2.clicked.connect(lambda: self.assembledBoard_1(pathway_temp_2,pathway_def_2,alignment=align_2,threshold_mis=85,opening_mis = 2,thresh_fg_temp=100,thresh_fg_def = 120,blur_roi=7,a_cspace=137,a_cspace_def=137,b_cspace_temp=131,b_cspace_def=131,open_it=1,close_it=1,pol_minArea=150))


        pathway_temp_3 = r'BOARD LIBRARY\Assembled\assemb_3 Template board image.JPEG'
        pathway_def_3 = r'BOARD LIBRARY\Assembled\assemb_3 Defective board image.JPEG'
        self.ui.number_3.clicked.connect(self.Dialog.close)
        self.ui.number_3.clicked.connect(
            lambda: self.assembledBoard_1(pathway_temp_3, pathway_def_3, alignment=align_2, threshold_mis=93, opening_mis = 2,
                                          thresh_fg_temp=170, thresh_fg_def=180, blur_roi=7, a_cspace=113,
                                          a_cspace_def=113, b_cspace_temp=135,b_cspace_def = 133, open_it=1, close_it=1,pol_minArea=150))


    def inspect_solder(self):
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


        pathway_temp_1 = r'BOARD LIBRARY\Solder\solder_1 Template board image.JPEG'
        pathway_def_1 = r'BOARD LIBRARY\Solder\solder_1 Defective board image.JPEG'
        self.ui.number_1.clicked.connect(self.Dialog.close)
        self.ui.number_1.clicked.connect(lambda: self.solderjoint_1(pathway_temp_1,pathway_def_1))

        pathway_temp_2 = r'BOARD LIBRARY\Solder\solder_2 Template board image.JPEG'
        pathway_def_2 = r'BOARD LIBRARY\Solder\solder_2 Defective board image.JPEG'
        self.ui.number_2.clicked.connect(self.Dialog.close)
        self.ui.number_2.clicked.connect(lambda: self.solderjoint_1(pathway_temp_2,pathway_def_2))

        pathway_temp_3 = r'BOARD LIBRARY\Solder\solder_3 Template board image.JPEG'
        pathway_def_3 = r'BOARD LIBRARY\Solder\solder_3 Defective board image.JPEG'
        self.ui.number_3.clicked.connect(self.Dialog.close)
        self.ui.number_3.clicked.connect(lambda: self.solderjoint_1(pathway_temp_3,pathway_def_3))



    def setupUi(self, mainWindow ):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1920, 1080)
        mainWindow.setStyleSheet(_fromUtf8("QPushButton#inspectbtn{\n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "border:None\n"
                                           "}\n"
                                           "QPushButton#imLoadbtn{\n"
                                           "    background-color: rgb(0, 255, 127);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "border:None\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#inspectbtn_2{\n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "border:None\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#imLoadbtn_2{\n"
                                           "    background-color: rgb(0, 255, 127);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "border:None\n"
                                           "}\n"
                                           "\n"
                                           ""))
        ####################


        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 201, 821))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Plain = QtGui.QWidget()
        self.Plain.setStyleSheet(_fromUtf8(""))
        self.Plain.setObjectName(_fromUtf8("Plain"))



        self.imLoadbtn = QtGui.QPushButton(self.Plain)
        self.imLoadbtn.setGeometry(QtCore.QRect(10, 660, 171, 34))
        self.imLoadbtn.setAutoDefault(False)
        self.imLoadbtn.setDefault(False)
        self.imLoadbtn.setFlat(False)
        self.imLoadbtn.setObjectName(_fromUtf8("imLoadbtn"))
        ###################BUTTON EVENT#########################
        self.imLoadbtn.clicked.connect(self.select_bareboard)
        ################################################

        self.inspectbtn = QtGui.QPushButton(self.Plain)
        self.inspectbtn.setGeometry(QtCore.QRect(10, 720, 171, 34))
        self.inspectbtn.setObjectName(_fromUtf8("inspectbtn"))
        #######################
        self.inspectbtn.clicked.connect(self.inspect_bare)
        ################################################

        self.tabWidget.addTab(self.Plain, _fromUtf8(""))
        self.Assembled = QtGui.QWidget()
        self.Assembled.setObjectName(_fromUtf8("Assembled"))
        self.imLoadbtn_2 = QtGui.QPushButton(self.Assembled)
        self.imLoadbtn_2.setGeometry(QtCore.QRect(10, 660, 171, 34))
        self.imLoadbtn_2.setAutoDefault(False)
        self.imLoadbtn_2.setDefault(False)
        self.imLoadbtn_2.setFlat(False)
        self.imLoadbtn_2.setObjectName(_fromUtf8("imLoadbtn_2"))
        ###################BUTTON EVENT#########################
        self.imLoadbtn_2.clicked.connect(self.select_assembledboard)
        ################################################
        self.inspectbtn_2 = QtGui.QPushButton(self.Assembled)
        self.inspectbtn_2.setGeometry(QtCore.QRect(10, 720, 171, 34))
        self.inspectbtn_2.setObjectName(_fromUtf8("inspectbtn_2"))
        ##############################
        self.inspectbtn_2.clicked.connect(self.inspect_assemb)


        self.tabWidget.addTab(self.Assembled, _fromUtf8(""))
        ##################
        self.solderjoint = QtGui.QWidget()
        self.solderjoint.setObjectName(_fromUtf8("Solder Joint"))
        self.imLoadbtn_3 = QtGui.QPushButton(self.solderjoint)
        self.imLoadbtn_3.setGeometry(QtCore.QRect(10, 660, 171, 34))
        self.imLoadbtn_3.setAutoDefault(False)
        self.imLoadbtn_3.setDefault(False)
        self.imLoadbtn_3.setFlat(False)
        self.imLoadbtn_3.setObjectName(_fromUtf8("imLoadbtn_3"))
        ###################BUTTON EVENT#########################
        self.imLoadbtn_3.clicked.connect(self.select_solder)
        ################################################
        self.inspectbtn_3 = QtGui.QPushButton(self.solderjoint)
        self.inspectbtn_3.setGeometry(QtCore.QRect(10, 720, 171, 34))
        self.inspectbtn_3.setObjectName(_fromUtf8("inspectbtn_3"))
        ##############################
        self.inspectbtn_3.clicked.connect(self.inspect_solder)

        self.tabWidget.addTab(self.solderjoint, _fromUtf8(""))


        self.BareBoardLbl = QtGui.QLabel(self.centralwidget)
        self.BareBoardLbl.setGeometry(QtCore.QRect(540, 0, 191, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.BareBoardLbl.setFont(font)
        self.BareBoardLbl.setObjectName(_fromUtf8("BareBoardLbl"))
        self.AssembledBoardLbl = QtGui.QLabel(self.centralwidget)
        self.AssembledBoardLbl.setGeometry(QtCore.QRect(1230, 0, 246, 21))
        self.AssembledBoardLbl_2 = QtGui.QLabel(self.centralwidget)
        self.AssembledBoardLbl_2.setGeometry(QtCore.QRect(1700, 0, 246, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.AssembledBoardLbl.setFont(font)
        self.AssembledBoardLbl.setObjectName(_fromUtf8("AssembledBoardLbl"))
        self.AssembledBoardLbl_2.setFont(font)
        self.AssembledBoardLbl_2.setObjectName(_fromUtf8("AssembledBoardLbl_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(240, 30, 1591, 238))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1589, 183))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

#######################3
        self.scrollArea_2 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(239, 266, 1591, 621))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))

        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1589, 619))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout.setSpacing(55)
        self.BoardImage = QtGui.QLabel(self.centralwidget)
        self.BoardImage.setText(_fromUtf8(""))
        self.BoardImage.setObjectName(_fromUtf8("BoardImage"))
        self.BoardImage.setFixedSize(QtCore.QSize(728, 576))
        self.BoardImage.setScaledContents(True)
        self.gridLayout.addWidget(self.BoardImage, 0, 0, 1, 1)
        self.BoardImage_2 = QtGui.QLabel(self.centralwidget)
        self.BoardImage_2.setText(_fromUtf8(""))
        self.BoardImage_2.setObjectName(_fromUtf8("BoardImage_2"))
        self.BoardImage_2.setFixedSize(QtCore.QSize(728, 576))
        self.BoardImage_2.setScaledContents(True)
        self.gridLayout.addWidget(self.BoardImage_2, 0, 1, 1, 1)
        self.BoardImage_3 = QtGui.QLabel(self.centralwidget)
        self.BoardImage_3.setObjectName(_fromUtf8("BoardImage_3"))
        self.BoardImage_3.setFixedSize(QtCore.QSize(728, 576))
        self.BoardImage_3.setScaledContents(True)
        self.gridLayout.addWidget(self.BoardImage_3, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
############################


        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainWindow)
        self.toolBar.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.toolBar.setPalette(palette)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setStyleSheet(_fromUtf8("QToolBar{\n"
"    border-color: rgb(85, 255, 255);\n"
"    \n"
"    \n"
"    \n"
"    background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}"))
        self.toolBar.setIconSize(QtCore.QSize(65, 45))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 31))
        self.menuBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuBar.setToolTip(_fromUtf8(""))
        self.menuBar.setAutoFillBackground(True)
        self.menuBar.setStyleSheet(_fromUtf8("QmenuBar{\n"
"    background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}"))
        self.toolBar.setIconSize(QtCore.QSize(65, 45))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCorrect_Type = QtGui.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/CorrectType.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCorrect_Type.setIcon(icon)
        self.actionCorrect_Type.setObjectName(_fromUtf8("actionCorrect_Type"))
        self.actionPolarity_Check = QtGui.QAction(mainWindow)
        self.actionPolarity_Check.setChecked(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/PolarityCheck.jpg")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionPolarity_Check.setIcon(icon1)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionPolarity_Check.setFont(font)
        self.actionPolarity_Check.setObjectName(_fromUtf8("actionPolarity_Check"))
        self.actionMissing_Component = QtGui.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/missingComponent.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMissing_Component.setIcon(icon2)
        self.actionMissing_Component.setObjectName(_fromUtf8("actionMissing_Component"))
        self.actionInspect = QtGui.QAction(mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/Inspect.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInspect.setIcon(icon3)
        self.actionInspect.setObjectName(_fromUtf8("actionInspect"))
        self.actionOCR = QtGui.QAction(mainWindow)
        self.actionOCR.setChecked(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/OCR.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOCR.setIcon(icon4)
        self.actionOCR.setObjectName(_fromUtf8("actionOCR"))
        self.actionShort_Circuit = QtGui.QAction(mainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/ShortCircuit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShort_Circuit.setIcon(icon5)
        self.actionShort_Circuit.setObjectName(_fromUtf8("actionShort_Circuit"))
        self.actionOpen_Circuit = QtGui.QAction(mainWindow)
        self.actionOpen_Circuit.setChecked(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/OpenCircuit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Circuit.setIcon(icon6)
        self.actionOpen_Circuit.setObjectName(_fromUtf8("actionOpen_Circuit"))
        self.actionMissing_Wrong_Size_Hole = QtGui.QAction(mainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/Missing-Wrong size hole.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMissing_Wrong_Size_Hole.setIcon(icon7)
        self.actionMissing_Wrong_Size_Hole.setObjectName(_fromUtf8("actionMissing_Wrong_Size_Hole"))
        self.actionPinhole_Breakout = QtGui.QAction(mainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/pinhole-breakout.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPinhole_Breakout.setIcon(icon8)
        self.actionPinhole_Breakout.setObjectName(_fromUtf8("actionPinhole_Breakout"))
        ##################33
        self.actionShort_Bridging = QtGui.QAction(mainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/short.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShort_Bridging.setIcon(icon9)
        self.actionShort_Bridging.setObjectName(_fromUtf8("actionShort_Bridging"))
        self.actionOpen = QtGui.QAction(mainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI icons/nosolder.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon10)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        #####################
        self.toolBar.addAction(self.actionMissing_Wrong_Size_Hole)
        self.toolBar.addAction(self.actionShort_Circuit)
        self.toolBar.addAction(self.actionOpen_Circuit)
        self.toolBar.addAction(self.actionPinhole_Breakout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMissing_Component)
        self.toolBar.addAction(self.actionPolarity_Check)
        self.toolBar.addAction(self.actionCorrect_Type)
        self.toolBar.addAction(self.actionOCR)
        self.toolBar.addSeparator()
        ############
        self.toolBar.addAction(self.actionShort_Bridging)
        self.toolBar.addAction(self.actionOpen)


        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        ############################MAIN ##############
    global preprocessing, alignImages, colouring, roi ,idx ,def_loc , missing ,watersegment ,pol_check,roi_assembled,preprocessing_assemb,OCR,words,black_im,roi_ocr,after_OCR
    global template_im , defective_im
    global number,num,words_1,sayac,align_2

    number = 0
    sayac = 0
    num = 0



    def bareboard_1(self,pathway_temp,pathway_def,drows,dcolumns,trows,tcolumns,pos_blur,neg_blur,blur_roi,num_iterate1,num_iterate2,num_iterate3):

        print(blur_roi)
        golden_im = cv2.imread(pathway_temp)
        cv2.imshow('template board image',golden_im)

        defective_im = cv2.imread(pathway_def)
        pixmap = QtGui.QPixmap(pathway_def)
        pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage.setPixmap(pixmap)
        self.BoardImage.setAlignment(QtCore.Qt.AlignLeft)

        defective_im = cv2.resize(defective_im, (728, 576))
        golden_im = cv2.resize(golden_im, (728, 576))


        golden_equ = preprocessing(self,golden_im)
        defective_equ = preprocessing(self,defective_im)

        golden_binary = cv2.adaptiveThreshold(golden_equ, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                              cv2.THRESH_BINARY, 25, -7)
        cv2.imshow('golden_binary thresholded',golden_binary)

        kernel_hor = np.ones((1, 3), np.uint8)  # horizontal kernel to merge horizontally broken lines
        kernel_ver = np.ones((3, 1), np.uint8)  # vertical kernel to merge vertically broken lines
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))


        golden_binary = cv2.morphologyEx(golden_binary, cv2.MORPH_CLOSE, kernel_hor, iterations=num_iterate2)
        golden_binary = cv2.morphologyEx(golden_binary, cv2.MORPH_CLOSE, kernel_ver, iterations=num_iterate3)
        golden_binary = cv2.morphologyEx(golden_binary, cv2.MORPH_CLOSE, kernel, iterations=num_iterate1)

        cv2.imshow('Morphologically closed binarized golden board', golden_binary)
        # cv2.waitKey(0)


        defective_binary = cv2.adaptiveThreshold(defective_equ, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                                 cv2.THRESH_BINARY, 25, -7)
        cv2.imshow('defective_binary thresholded', defective_binary)


        defective_binary = cv2.morphologyEx(defective_binary, cv2.MORPH_CLOSE, kernel_hor, iterations=num_iterate1)
        defective_binary = cv2.morphologyEx(defective_binary, cv2.MORPH_CLOSE, kernel_ver, iterations=num_iterate1)
        cv2.imshow('Morphologically closed binarized defective board', defective_binary)
        # cv2.waitKey(0)

        golden_binary = alignImages(self,golden_binary, defective_binary)



        blurred_golden = cv2.GaussianBlur(golden_binary, (1,1),0)
        blurred_defective = cv2.GaussianBlur(defective_binary, (1,1),0)
        cv2.imshow('Overlayed golden board', blurred_golden)
        cv2.imshow('Overlayed defective board', blurred_defective)
        # cv2.waitKey(0)

        #################################### FLOOD FILL FOR SEVERAL CONNECTED COMPONENTS

        ####so that there are many seperately connected components a mask should be used and updated accordingly to get passed the next component
        holes = blurred_defective.copy()
        holes1 = blurred_golden.copy()

        rows1, columns1 = blurred_golden.shape[:2]

        for r1 in range(0, rows1, drows):
                for c1 in range(0, columns1, dcolumns):  # selects seed point at interval of 25 pixels ( can be modified)
                        if holes[r1][c1] == 0:
                                cv2.floodFill(holes, None, (c1, r1), 255)

        for r1 in range(0, rows1, trows):
                for c1 in range(0, columns1, tcolumns):  # selects seed point at interval of 25 pixels ( can be modified)
                        if holes1[r1][c1] == 0:
                                cv2.floodFill(holes1, None, (c1, r1),
                                              255)  # fills the connected components with white starting from the seed points

        cv2.imshow('holes', holes)
        cv2.imshow('holes1', holes1)
        # cv2.waitKey(0)

        holes = cv2.bitwise_not(
                holes)  # inner circles of fiducials are white and the rest is black after taking complement.
        holes1 = cv2.bitwise_not(holes1)

        c_defective_ff = blurred_defective | holes  # once inner white circles are added to the original image, flood fill is done.
        c_golden_ff = blurred_golden | holes1
        cv2.imshow('Flood filled defective board', c_defective_ff)
        # cv2.waitKey(0)
        cv2.imshow('Flood filled golden board', c_golden_ff)
        # cv2.waitKey(0)

        It = blurred_golden.copy()
        Id = blurred_defective.copy()
        cv2.imshow('It', It)
        cv2.imshow('Id', Id)

        # subtracting each pixels of defective image from template image and vice versa.
        # subtracting defective image from template image results in negative image
        # subtracting template image from defective image results in positive image
        In = cv2.subtract(It, Id)
        Ip = cv2.subtract(Id, It)

        In = cv2.medianBlur(In, neg_blur)
        Ip = cv2.medianBlur(Ip, pos_blur)
        cv2.imshow('negative img', In)
        # cv2.waitKey(0)
        cv2.imshow('positive img', Ip)



        _, blurred_In = cv2.threshold(In, 142, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        _, blurred_Ip = cv2.threshold(Ip, 142, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        Ia = cv2.bitwise_or(blurred_In, blurred_Ip)
        cv2.imshow('binarized and blurred negative img', blurred_In)
        # cv2.waitKey(0)
        cv2.imshow('binarized and blurred positive img', blurred_Ip)
        # cv2.waitKey(0)
        cv2.imshow('All defects', Ia)
        # cv2.waitKey(0)

        # in order to xor colourful solely defects that have 3 channels , defective board channels are increased to 3.
        blurred_defective = cv2.cvtColor(blurred_defective, cv2.COLOR_GRAY2BGR)

        # GROUP 1 DEFECTS(MISSING HOLE , WRONG SIZE HOLE)
        Ig1 = cv2.subtract(c_golden_ff, blurred_Ip)
        cv2.imshow('Ig1', Ig1)
        # cv2.waitKey(0)

        # solely missing holes
        Ig1_1 = cv2.bitwise_xor(Ig1, c_golden_ff)
        cv2.imshow('solely group 1 defects', Ig1_1)
        # cv2.waitKey(0)

        i = 0
        contours,i = roi(self, Ig1_1, defective_im,i,blur_roi,lbl_path = _fromUtf8("../GUI icons/Missing-Wrong size hole.jpg"))
        # solely group 1 defects image is converted to 3 channel to display defects in color
        Ig1_1 = cv2.cvtColor(Ig1_1, cv2.COLOR_GRAY2BGR)
        # colouring function takes input image and B,G,R colour values respectively
        counter = 0
        counter=colouring(self,Ig1_1, 125, 0, 200,contours,counter)

        # colourized defects are displayed on defective board image
        Ig1_colourful = cv2.bitwise_xor(Ig1_1, blurred_defective)
        cv2.imshow('Group 1 defects(missing hole , wrong size hole)', Ig1_colourful)
        # cv2.waitKey(0)

        #############GROUP 2 DEFECTS(spur, short, conductor or too close ,underetch, spurious copper ,excessive short)
        Ig2 = cv2.bitwise_xor(blurred_Ip, Ig1)
        cv2.imshow('Group 2 defects on defective board', Ig2)
        # cv2.waitKey(0)
        # solely group 2 defects
        Ig2_1 = cv2.bitwise_xor(Ig2, c_golden_ff)
        cv2.imshow('Solely Group 2', Ig2_1)
        # cv2.waitKey(0)

        contours,i=roi(self, Ig2_1, defective_im,i,blur_roi,lbl_path = _fromUtf8("../GUI icons/ShortCircuit.png"))

        Ig2_1 = cv2.cvtColor(Ig2_1, cv2.COLOR_GRAY2BGR)
        counter= colouring(self,Ig2_1, 0, 255, 255,contours,counter)

        Ig2_colourful = cv2.bitwise_xor(Ig2_1, blurred_defective)
        cv2.imshow('Group 2 defects(Short,Spurious copper , Excessive Short, Under-Etch, Conductor too close',
                   Ig2_colourful)
        # cv2.waitKey(0)

        ##########GROUP 3 DEFECTS(Open circuit, over etch, mouse bite, conductors too close)
        Ide = cv2.subtract(c_defective_ff, blurred_In)
        cv2.imshow('Ide(breakout,pinhole,under etch pos on defective', Ide)
        # cv2.waitKey(0)
        Ide1 = cv2.bitwise_xor(c_defective_ff, Ide)
        cv2.imshow('solely breakout,pinhole,underetch positive', Ide1)
        # cv2.waitKey(0)
        # Ide yields (breakout,pinhole, underetch positive)

        Ig3 = cv2.bitwise_xor(Ide1, blurred_In)
        cv2.imshow('group 3 defects', Ig3)
        # cv2.waitKey(0)
        contours,i = roi(self, Ig3, defective_im, i,blur_roi,lbl_path= QtGui.QPixmap(_fromUtf8("../GUI icons/OpenCircuit.png")))
        Ig3_1 = cv2.cvtColor(Ig3, cv2.COLOR_GRAY2BGR)
        counter=colouring(self,Ig3_1, 255, 0, 255,contours,counter)

        Ig3_colourful = cv2.bitwise_xor(Ig3_1, blurred_defective)

        cv2.imshow('Group 3 Defects(Open circuit, over etch, mouse bite, conductors too close)', Ig3_colourful)
        # cv2.waitKey(0)

        # GROUP 4 DEFECTS ( UNDER ETCH POSITIVE)
        ##########GROUP 4 DEFECTS ( UNDER ETCH)
        A = cv2.bitwise_or(Ig2, Ide)

        holes = A.copy()
        cv2.floodFill(holes, None, (0, 0), 255)
        holes = cv2.bitwise_not(holes)

        A_ff = cv2.bitwise_or(A, holes)


        Ig4 = cv2.bitwise_xor(A, A_ff)


        Ig4_1 = cv2.cvtColor(Ig4.copy(), cv2.COLOR_GRAY2BGR)
        Ig4_colourful = cv2.bitwise_xor(blurred_defective, Ig4_1)


        ######GROUP 5 DEFECTS(PINHOLE, BREAKOUT,under etch)
        # Ide 1 de underetch yok !!(deficient)
        Ig5 = cv2.bitwise_xor(Ig4, Ide1)
        cv2.imshow('Ide1', Ide1)
        cv2.imshow('Ig5', Ig5)

        Ig5 = cv2.bitwise_xor(Ig4, Ig5)
        cv2.imshow('Solely Group 5 defects(breakout,pinhole)', Ig5)
        # cv2.waitKey(0)
        contours,i =roi(self, Ig5, defective_im,i, blur_roi,lbl_path = _fromUtf8("../GUI icons/pinhole-breakout.gif"))

        Ig5 = cv2.cvtColor(Ig5, cv2.COLOR_GRAY2BGR)
        counter= colouring(self,Ig5, 0, 0, 255,contours,counter)
        Ig5_colourful = cv2.bitwise_xor(blurred_defective, Ig5)
        cv2.imshow('Group 5 defects', Ig5_colourful)
        # cv2.waitKey(0)

        background = np.zeros((630, 800, 3), np.uint8)  # black background created for legend

        Ig_colourful = Ig1_colourful ^ Ig2_colourful ^ Ig3_colourful ^ blurred_defective ^ Ig5_colourful

        background[0:576, 0:728] = Ig_colourful  # relevant part of defects are copied onto background image
        background[555:620, 0:728] = np.asarray([255, 255, 255])  # white background for visible texts
        background[0:630, 728:800] = np.asarray([255, 255, 255])
        # group defects are added as legend at the bottom of the all classified defects
        # cv2.putText(background,'Group 1 (Missing hole, wrong size hole)',(50,550),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,197,0),2)
        cv2.putText(background, 'Group 1 (Missing hole, wrong size hole)', (50, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (197, 255, 0), 2)
        cv2.putText(background,
                    'Group 2 defects(Short,Spurious copper , Excessive Short, Under-Etch, Conductor too close)',
                    (50, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(background, 'Group 3 Defects(Open circuit, over etch, mouse bite, conductors too close)', (50, 600),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (139, 0, 139), 2)
        cv2.putText(background, 'Group 4 defects(breakout,pinhole)', (50, 615), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 0, 255), 2)
        # cv2.imshow('Classified defects', background)
        cv2.imwrite(r'bare_classified.JPEG', background)
        ################
        pixmap = QtGui.QPixmap(r'bare_classified.JPEG')
        self.BoardImage_2.setPixmap(pixmap)


        pixmap_temp = QtGui.QPixmap(pathway_temp)
        self.BoardImage_3.setPixmap(pixmap_temp)


        cv2.waitKey(0)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
        return


    def CaptureFrame_bare(self,pathway_temp,pathway_def):
            ############33
            #previously captured frames are removed to prevent overflow
            if os.path.exists(pathway_temp):
                os.remove(pathway_temp)
                os.remove(pathway_def)
            else:
                print("The file does not exist")


            temp = 0
            defect = 0

            cap = cv2.VideoCapture(1)


            while (True):
                    ret, frame = cap.read()

                    cv2.imshow("Captured frame", frame)

                    if not ret:
                            break
                    elif cv2.waitKey(1) == 27:  # ESC is pressed, get out of the loop
                            break
                    elif cv2.waitKey(1) == 32:  # Space is pressed , write the captured template board image

                            for i in range(1, 31):  # loop 30 times

                                    cv2.imwrite(
                                            r'bare Template board image' + str(
                                                    i) + '.JPEG', frame)
                                    a = cv2.imread(
                                            r'bare Template board image' + str(
                                                    i) + '.JPEG').astype('float64')
                                    temp = temp + a  # so as to prevent overflow the image is stored as float64 datatype rather than unsigned 8 bits

                            # print(temp.dtype)
                            temp = temp / 30
                            temp = temp.astype('uint8')

                            cv2.imwrite(pathway_temp,temp)

                            ###########
                            pixmap = QtGui.QPixmap(pathway_temp)

                            pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(),QtCore.Qt.KeepAspectRatio)
                            self.BoardImage.setPixmap(pixmap)
                            self.BoardImage.setAlignment(QtCore.Qt.AlignLeft)
                            ###########
                    elif cv2.waitKey(
                            1) == 8:  # Backspace is pressed once again , write the captured defective board image
                            for i in range(1, 31):
                                    cv2.imwrite(
                                            r'bare Defective board image' + str(
                                                    i) + '.JPEG', frame)
                                    b = cv2.imread(
                                            r'bare Defective board image' + str(i) + '.JPEG').astype('float64')
                                    defect = defect + b

                            defect = defect / 30
                            defect = defect.astype('uint8')
                            cv2.imwrite(pathway_def,defect)
                            # cv2.imshow('averaged defective board image', defect)
                            ###########IMAGE SHOWN IN QLABEL
                            pixmap = QtGui.QPixmap(pathway_def)
                            pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(),QtCore.Qt.KeepAspectRatio)
                            self.BoardImage_2.setPixmap(pixmap)
                            self.BoardImage_2.setAlignment(QtCore.Qt.AlignRight)
                            ###########

            cap.release()
            cv2.destroyAllWindows()
            return temp, defect


    def CaptureFrame_assemb(self,pathway_temp,pathway_def):
            ############33
            #previously captured frames are removed to prevent overflow
            if os.path.exists(pathway_temp):
                os.remove(pathway_temp)
                os.remove(pathway_def)
            else:
                print("The file does not exist")


            temp = 0

            defect = 0

            cap = cv2.VideoCapture(1)

            while (True):
                    ret, frame = cap.read()

                    cv2.imshow("Captured frame", frame)

                    if not ret:
                            break
                    elif cv2.waitKey(1) == 27:  # ESC is pressed, get out of the loop
                            break
                    elif cv2.waitKey(1) == 32:  # Space is pressed , write the captured template board image

                            for i in range(1, 31):  # loop 30 times

                                    cv2.imwrite(
                                            r'assemb Template board image' + str(
                                                    i) + '.JPEG', frame)
                                    a = cv2.imread(
                                            r'assemb Template board image' + str(
                                                    i) + '.JPEG').astype('float32')
                                    temp = temp + a  # so as to prevent overflow the image is stored as float64 datatype rather than unsigned 8 bits

                            temp = temp / 30
                            temp = temp.astype('uint8')
                            cv2.imwrite(pathway_temp,temp)
                            # cv2.imshow('averaged template board image', temp)
                            ###########
                            pixmap = QtGui.QPixmap(pathway_temp)
                            pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(),QtCore.Qt.KeepAspectRatio)
                            self.BoardImage.setPixmap(pixmap)
                            self.BoardImage.setAlignment(QtCore.Qt.AlignLeft)
                            ###########
                    elif cv2.waitKey(1) == 8:  # Backspace is pressed once again , write the captured defective board image
                            for i in range(1, 31):
                                    cv2.imwrite(
                                            r'assemb Defective board image' + str(
                                                    i) + '.JPEG', frame)
                                    b = cv2.imread(
                                            r'assemb Defective board image' + str(i) + '.JPEG').astype('float32')
                                    defect = defect + b

                            defect = defect / 30
                            defect = defect.astype('uint8')
                            cv2.imwrite(pathway_def,defect)
                            # cv2.imshow('averaged defective board image', defect)
                            ###########IMAGE SHOWN IN QLABEL
                            pixmap = QtGui.QPixmap(pathway_def)
                            pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(),QtCore.Qt.KeepAspectRatio)
                            self.BoardImage_2.setPixmap(pixmap)
                            self.BoardImage_2.setAlignment(QtCore.Qt.AlignRight)
                            ###########

            cap.release()
            cv2.destroyAllWindows()
            return temp, defect



    def preprocessing(self,board_im):

            ############GAMMA CORRECTION
            gamma = 0.7
            lookUpTable = np.empty((1, 256), np.uint8)
            for i in range(256):
                    lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

            board_im = cv2.LUT(board_im, lookUpTable)
            # cv2.imshow('Gamma corrected  board image', board_im)

            ##### Converting images to gray scale

            gray = cv2.cvtColor(board_im, cv2.COLOR_BGR2GRAY)


            ############ADAPTIVE HISTOGRAM EQUALIZATION
            clahe = cv2.createCLAHE(clipLimit=2.7, tileGridSize=(25, 45))
            board_equ = clahe.apply(gray)

   # strength of denoising is picked as 23 for powerful denoising
            cv2.fastNlMeansDenoising(board_equ, board_equ, 23.0, 7,
                                     21)  # strength of denoising is picked as 23 for powerful denoising
            # window sizes and pixel lengths are chosen as default
            board_equ = cv2.medianBlur(board_equ, 3)  # slight median filtering is applied for residual noise removal
            #####################################################

            return board_equ

    def alignImages(self,golden_binary, defective_binary):

            MAX_FEATURES = 500
            GOOD_MATCH_PERCENT = 0.15


            # Detect ORB features and compute descriptors.
            orb = cv2.ORB_create(MAX_FEATURES)
            keypoints1, descriptors1 = orb.detectAndCompute(golden_binary, None)
            keypoints2, descriptors2 = orb.detectAndCompute(defective_binary, None)

            # Match features.
            matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
            matches = matcher.match(descriptors1, descriptors2, None)

            # Sort matches by score
            matches.sort(key=lambda x: x.distance, reverse=False)

            # Remove not so good matches
            numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
            matches = matches[:numGoodMatches]

            # Draw top matches
            imMatches = cv2.drawMatches(golden_binary, keypoints1, defective_binary, keypoints2, matches, None)
            cv2.imwrite(r"matches.jpg", imMatches)

            # Extract location of good matches
            points1 = np.zeros((len(matches), 2), dtype=np.float32)
            points2 = np.zeros((len(matches), 2), dtype=np.float32)

            for i, match in enumerate(matches):
                    points1[i, :] = keypoints1[match.queryIdx].pt
                    points2[i, :] = keypoints2[match.trainIdx].pt

            # Find homography
            h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

            # Use homography
            height, width = defective_binary.shape[:2]
            golden_binary = cv2.warpPerspective(golden_binary, h, (width, height))

            return golden_binary

    def align_2(self,template_im,defective_im):
        print(len(template_im.shape))

        # IMAGE REGISTRATION (ALIGNING)
        warp_mode = cv2.MOTION_AFFINE
        # warp_mode = cv2.MOTION_HOMOGRAPHY
        # eye takes N(# of rows in the output) ,M(# of columns)
        warp_matrix = np.eye(2, 3, dtype=np.float32)
        number_of_iterations = 500;
        termination_eps = 1e-7;

        # define termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations, termination_eps)

        ##############33
        defective_gray = cv2.cvtColor(defective_im,cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template_im, cv2.COLOR_BGR2GRAY)
        (cc, warp_matrix) = cv2.findTransformECC(defective_gray, template_gray, warp_matrix, warp_mode, criteria)

        # use warpAffine for translation , euclidean and affine
        # defective_aligned = cv2.warpAffine(roi_defective, warp_matrix ,(size[1],size[0]),flags = cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_CONSTANT,borderValue=0)
        template_aligned = cv2.warpAffine(template_im, warp_matrix, (template_im.shape[1], template_im.shape[0]),
                                           flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP,
                                           borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        # defective_aligned = cv2.warpPerspective(defective_binary, warp_matrix ,(size[1],size[0]),flags = cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
        # check whether they are aligned in shape or not

        return template_aligned


    def colouring(self,image, B, G, R,contours,counter):

            white = np.asarray([255, 255, 255])
            colour = np.asarray([B, G, R])
            rows, columns = image.shape[:2]

            for r in range(rows):
                    for c in range(columns):
                            pixel = image[r][c]
                            if all(pixel == white):
                                    image[r][c] = colour


            for (counter, cnt) in enumerate(contours,counter):

                M = cv2.moments(cnt)
                if M["m00"] != 0:
                        cx = int(M['m10'] / M['m00'])
                        cy = int(M['m01'] / M['m00'])
                else:
                        cx, cy = 0, 0
                image = cv2.putText(image, str(counter + 1), (cx + 10, cy + 10), cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5, (125, 125, 125), 2)
                cv2.imshow('enumerated defects',image)
                # cv2.waitKey(0)

            return counter+1


    def roi(self, image, defective_im,i,blur_roi,lbl_path):

            image = cv2.medianBlur(image, blur_roi)
            cv2.imshow('median blurred roi image',image)
            # cv2.waitKey(0)

            ret, contours,_ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            print(len(contours),i)

            idx = 0
            for (i,cnt) in enumerate(contours,i):
                    idx += 1
                    # print(cnt)
                    x, y, w, h = cv2.boundingRect(cnt)
                    roi_group = defective_im[y - 35:y + h + 35, x - 35:x + w + 35]
                    cv2.imwrite(r'ROI' + str(idx) + '.JPEG',roi_group)
            ########################
                    pixmap = QtGui.QPixmap(r'ROI' + str(idx) + '.JPEG')

                    self.label = QtGui.QLabel(self.centralwidget)
                    self.label.setText(_fromUtf8(""))
                    self.label.setObjectName(_fromUtf8("label"))
                    self.label.setFrameShape(QtGui.QFrame.Box)
                    self.label.setFixedSize(QtCore.QSize(200, 175))
                    self.label.setScaledContents(True)
                    self.horizontalLayout.setSpacing(55)
                    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                    self.horizontalLayout.addWidget(self.label)
                    self.label.deleteLater()
                    self.horizontalLayout.setAlignment(QtCore.Qt.AlignLeft)
                    pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)
                    self.label.setPixmap(pixmap)

                    QtGui.QApplication.processEvents()
            ############################

            ########################CLASS LABEL
                    pixmap = QtGui.QPixmap(lbl_path)
                    self.class_lbl = QtGui.QLabel(self.centralwidget)

                    self.class_lbl.setText(_fromUtf8(""))
                    self.class_lbl.setObjectName(_fromUtf8("label"))
                    self.class_lbl.setFrameShape(QtGui.QFrame.Box)

                    self.class_lbl.setFixedSize(QtCore.QSize(30, 30))
                    self.class_lbl.setScaledContents(True)
                    self.horizontalLayout.setSpacing(10)
                    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                    self.horizontalLayout.addWidget(self.class_lbl)
                    ##########################
                    self.class_lbl.deleteLater()
                    pixmap = pixmap.scaled(self.class_lbl.width(), self.class_lbl.height(), QtCore.Qt.KeepAspectRatio)
                    self.class_lbl.setPixmap(pixmap)
                    QtGui.QApplication.processEvents()

                    self.def_loc = QtGui.QLabel(self.centralwidget)
                    self.def_loc.setFixedSize(QtCore.QSize(30, 30))
                    self.horizontalLayout.addWidget(self.def_loc)
                    #######################
                    self.def_loc.deleteLater()
                    ##################3
                    self.def_loc.setNum(i + 1)
                    QtGui.QApplication.processEvents()

            return contours,i+1
    ########################################################3

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


    def assembledBoard_1(self,path_temp,path_def,alignment,threshold_mis,opening_mis,thresh_fg_temp,thresh_fg_def,blur_roi,a_cspace,a_cspace_def,b_cspace_temp,b_cspace_def,open_it,close_it,pol_minArea):


        print(path_temp)
        print(path_def)
        ############## MISALIGNED OR MISSING COMPONENTS##################3
        template_im = cv2.imread(path_temp)
        defective_im = cv2.imread(path_def)
        print(template_im.shape,defective_im.shape)
        template_im = cv2.resize(template_im, (728, 576))
        defective_im = cv2.resize(defective_im, (728, 576))
        cv2.imshow('template board image', template_im)
        cv2.imshow('defective board image', defective_im)
        # cv2.waitKey(0)


        template_im = alignment(self, template_im, defective_im)

        #############################
        cv2.imshow('template board image', template_im)
        cv2.imshow('defective board image', defective_im)
        # cv2.waitKey(0)

        ###########################
        pixmap = QtGui.QPixmap(path_def)
        pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage.setPixmap(pixmap)

        ###########################
        QtGui.QApplication.processEvents()
        pixmap = QtGui.QPixmap(path_temp)
        pixmap = pixmap.scaled(self.BoardImage_3.width(), self.BoardImage_3.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage_3.setPixmap(pixmap)

        mis_align = missing(self,template_im, defective_im,threshold_mis,opening_mis)
        cnt_num = 0
        contours,cnt_num = roi(self,mis_align,defective_im,cnt_num,blur_roi,lbl_path= _fromUtf8("../GUI icons/missingComponent.png"))
        mis_align = cv2.cvtColor(mis_align,cv2.COLOR_GRAY2BGR)
        counter = 0
        counter = colouring(self,mis_align,125, 0, 200,contours,counter)
        cv2.imshow('mis_align',mis_align)
        # cv2.waitKey(0)

        print(template_im.shape, defective_im.shape)

        # Calling correct_type function
        thresh_temp = preprocessing_assemb(self,template_im,a_cspace,b_cspace_temp,open_it,close_it)
        thresh_def = preprocessing_assemb(self,defective_im,a_cspace_def,b_cspace_def,open_it,close_it)
        cv2.imshow('thresh_temp',thresh_temp)
        cv2.imshow('thresh_def', thresh_def)
        # cv2.waitKey(0)

        # marker based watershed segmentation function is called and resultant markers are displayed
        marked_temp, area_temp, center_ms_temp, fg_temp, _ = watersegment(self,template_im.copy(), thresh_temp)
        cv2.imshow('Marked template image', marked_temp)
        # cv2.waitKey()
        marked_def, area_def, center_ms_def, fg_def, loc = watersegment(self,defective_im.copy(), thresh_def)
        cv2.imshow('Marked defective image', marked_def)


        ############POLARITY ERROR############
        mark_temp = pol_check(self,template_im, fg_temp,pol_minArea)
        mark_def = pol_check(self,defective_im, fg_def,pol_minArea)
        # marker_error = cv2.absdiff(mark_def, mark_temp)
        marker_error = cv2.subtract(mark_def, mark_temp)
        cv2.imshow('marker difference',marker_error)
        cv2.fastNlMeansDenoising(marker_error, marker_error, 37, 7, 21)
        # marker_error = cv2.morphologyEx(marker_error,cv2.MORPH_OPEN,kernel=np.ones((3,3),dtype=np.uint8))
        marker_error=cv2.morphologyEx(marker_error,cv2.MORPH_CLOSE,kernel= np.ones((5,5),dtype=np.uint8),iterations=5)
        cv2.imshow('marker error', marker_error)
        # cv2.waitKey(0)
        # print(marker_error.shape)
        marker_error = cv2.cvtColor(marker_error,cv2.COLOR_BGR2GRAY)
        _,marker_error=cv2.threshold(marker_error,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cv2.imshow('marker error', marker_error)
        # cv2.waitKey(0)
        contours, cnt_num = roi(self, marker_error, defective_im, cnt_num, blur_roi,lbl_path=_fromUtf8("../GUI icons/PolarityCheck.jpg"))
        marker_error = cv2.cvtColor(marker_error, cv2.COLOR_GRAY2BGR)
        counter = colouring(self, marker_error, 255, 255, 0, contours, counter)
        cv2.imshow('colored marker error',marker_error)
        # cv2.waitKey(0)
        ###################################################33


        ##########OPTICAL CHARACTER RECOGNITION#######################
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFixedSize(QtCore.QSize(200, 175))
        self.label.setScaledContents(True)
        self.horizontalLayout.setSpacing(55)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.label)
        ####################
        self.label.deleteLater()
        ##########################
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignLeft)
        ##############################

        path_temp,temp_OCR,a , b,  c , d , txt_temp, x,y,w,h, _ = OCR(self,template_im, fg_temp,thresh_fg_temp)
        ocr_con = after_OCR(self, temp_OCR, counter, path_temp, cnt_num, a, b, c, d)
        # print(path_temp)
        self.timer = QtCore.QTimer()
        if temp_OCR is not 0:


            self.timer.timeout.connect(lambda: words(self, path_temp))
            self.timer.timeout.connect(lambda: words_1(self, path_def))
            self.timer.start(5000)

            self.label_1 = QtGui.QLabel(self.centralwidget)
            self.label_1.setText(_fromUtf8(""))
            self.label_1.setObjectName(_fromUtf8("label"))
            self.label_1.setFrameShape(QtGui.QFrame.Box)
            self.label_1.setFixedSize(QtCore.QSize(200, 175))
            self.label_1.setScaledContents(True)
            self.horizontalLayout.setSpacing(55)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.horizontalLayout.addWidget(self.label_1)
            #########################
            self.label_1.deleteLater()
            ##########################
            self.horizontalLayout.setAlignment(QtCore.Qt.AlignLeft)


        path_def, def_OCR, a1, b1, c1, d1, txt_def, x1,y1,w1,h1,for_correct_ty  = OCR(self,defective_im,fg_def,thresh_fg_def)
        _ = after_OCR(self, def_OCR, counter, path_def, cnt_num, a1, b1, c1, d1)

#########################################################
        #######CORRECT TYPE DEFECT DETECTION
        print(txt_temp)
        print(txt_def)

        if txt_temp != txt_def:
                # print(txt_temp - txt_def)
                #wrong IC is used
                # correct_type_error = defective_im[y1:y1 + h1, x1: x1 + w1]
                correct_type_error = defective_im[b1:b1 + d1, a1: a1 + c1]
                cv2.imshow('wrong IC',correct_type_error)
                # cv2.waitKey(0)

                cv2.imwrite(r'wrong_IC.JPEG', correct_type_error)

                kernel = np.ones((35,35),np.uint8)
                for_correct_ty= cv2.dilate(for_correct_ty,kernel,iterations=5)
                cv2.imshow('for_correct_ty',for_correct_ty)
                # cv2.waitKey(0)

                type_err = np.zeros((576, 728), dtype=np.uint8)
                type_err = cv2.cvtColor(type_err, cv2.COLOR_GRAY2BGR)
                _,contours,_ = cv2.findContours(for_correct_ty,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                for_correct_ty = cv2.cvtColor(for_correct_ty, cv2.COLOR_GRAY2BGR)

                _ = colouring(self,for_correct_ty,0,177,177,contours,counter + 1)
                type_err[b1:b1 + d1, a1: a1 + c1] = for_correct_ty
                # type_err[y1:y1 + h1, x1: x1 + w1] = for_correct_ty
                cv2.imshow('correct type error',type_err)
                # cv2.waitKey(0)

                pixmap = QtGui.QPixmap(r'wrong_IC.JPEG')

                self.label_2 = QtGui.QLabel(self.centralwidget)
                self.label_2.setText(_fromUtf8(""))
                self.label_2.setObjectName(_fromUtf8("label"))
                self.label_2.setFrameShape(QtGui.QFrame.Box)

                self.label_2.setFixedSize(QtCore.QSize(200, 175))
                self.label_2.setScaledContents(True)
                self.horizontalLayout.setSpacing(55)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.horizontalLayout.addWidget(self.label_2)
                ######################
                self.label_2.deleteLater()
                ##################
                self.horizontalLayout.setAlignment(QtCore.Qt.AlignLeft)
                pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(), QtCore.Qt.KeepAspectRatio)
                self.label_2.setPixmap(pixmap)

                QtGui.QApplication.processEvents()
            ############################

            ########################CLASS LABEL
                lbl_path = _fromUtf8("../GUI icons/CorrectType.jpg")
                pixmap = QtGui.QPixmap(lbl_path)
                self.class_lbl = QtGui.QLabel(self.centralwidget)
                self.class_lbl.setText(_fromUtf8(""))
                self.class_lbl.setObjectName(_fromUtf8("label"))
                self.class_lbl.setFrameShape(QtGui.QFrame.Box)

                self.class_lbl.setFixedSize(QtCore.QSize(30, 30))
                self.class_lbl.setScaledContents(True)
                self.horizontalLayout.setSpacing(10)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.horizontalLayout.addWidget(self.class_lbl)
                #########################
                self.class_lbl.deleteLater()
                ################333
                pixmap = pixmap.scaled(self.class_lbl.width(), self.class_lbl.height(), QtCore.Qt.KeepAspectRatio)
                self.class_lbl.setPixmap(pixmap)
                QtGui.QApplication.processEvents()

                self.def_loc = QtGui.QLabel(self.centralwidget)
                self.def_loc.setFixedSize(QtCore.QSize(30, 30))
                self.horizontalLayout.addWidget(self.def_loc)
                #########################
                self.def_loc.deleteLater()
                ################333
                self.def_loc.setNum(cnt_num + 2)
                QtGui.QApplication.processEvents()



#########################################################################
        fg_def = cv2.cvtColor(fg_def, cv2.COLOR_GRAY2BGR)
        if ocr_con is  None:
            defects_col = marker_error ^ mis_align ^ fg_rgb
        elif type_err is None:
            defects_col = marker_error ^ mis_align ^ fg_rgb ^ ocr_con
        else:
            defects_col = marker_error ^ mis_align ^ ocr_con ^ fg_rgb ^ type_err

        cv2.imshow('colored assembled board defects',defects_col)

        background = np.zeros((630, 800, 3), np.uint8)  # black background created for legend


        background[0:576, 0:728] = defects_col  # relevant part of defects are copied onto background image
        background[555:620, 0:728] = np.asarray([255, 255, 255])  # white background for visible texts
        background[0:630, 728:800] = np.asarray([255, 255, 255])
        # group defects are added as legend at the bottom of the all classified defects

        cv2.putText(background, 'Missing Misaligned Components', (50, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 0, 255),2)
        cv2.putText(background,
                    'Polarity Check',
                    (50, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 191, 0), 2)
        cv2.putText(background, 'Optical Character Recognition', (50, 600),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        cv2.putText(background, 'Correct Type Defect', (50, 615), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 255), 2)
        # cv2.imshow('Classified defects', background)
        cv2.imwrite(r'assemb_classified.JPEG', background)
        ################
        pixmap = QtGui.QPixmap(r'assemb_classified.JPEG')
        pixmap = pixmap.scaled(self.BoardImage_2.width(), self.BoardImage_2.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage_2.setPixmap(pixmap)
        self.BoardImage_2.setAlignment(QtCore.Qt.AlignRight)

        cv2.waitKey(0)        #ESC pressed stop timer destroy all windows
        cv2.waitKey(0)
        self.timer.stop()
        cv2.destroyAllWindows()




    def words(self,path_OCR):
            # 5 SECONDS defined
            global number
            if number == len(path_OCR) :
                number = 0 # start over
            pixmap = QtGui.QPixmap(path_OCR[number])
            print(path_OCR[number])
            self.label.setPixmap(pixmap)
            # QtGui.QApplication.processEvents()  # so as to update pixmap
            number += 1

            return

    def words_1(self,path_OCR):
            # 5 SECONDS defined
            global sayac
            if sayac == len(path_OCR) :
                    sayac = 0 # start over
            pixmap = QtGui.QPixmap(path_OCR[sayac])
            print(path_OCR[sayac])
            self.label_1.setPixmap(pixmap)
            # QtGui.QApplication.processEvents()  # so as to update pixmap
            sayac += 1

            return


    def preprocessing_assemb(self,board_im,a_cspace,b_cspace,open_it,close_it):

        blurred_temp = cv2.GaussianBlur(board_im, (15, 15), 0)  # image is smoothened to get over noise

        lab = cv2.cvtColor(blurred_temp, cv2.COLOR_BGR2LAB)  # RGB color space is converted to LAB color space
        hsv = cv2.cvtColor(blurred_temp, cv2.COLOR_BGR2HSV)  # RGB to HSV(Hue,Saturation,value)

        l, a, b = cv2.split(lab)  # lab color space is splitted to channels
        _, thresh_l = cv2.threshold(l, 225, 255,
                                    cv2.THRESH_BINARY_INV)
        cv2.imshow('lightness channel',thresh_l)
        # cv2.waitKey(0)
        _, thresh_a = cv2.threshold(a, a_cspace, 255, cv2.THRESH_BINARY_INV)
        # _, thresh_a = cv2.threshold(a, 135, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow('thresh_a', thresh_a)
        # cv2.waitKey(0)
        # _, thresh_b = cv2.threshold(b, 100, 255, cv2.THRESH_BINARY_INV)
        _, thresh_b = cv2.threshold(b, b_cspace, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow('thresh_b',thresh_b)
        # cv2.waitKey(0)
        merged_lab = cv2.merge((thresh_l, thresh_a, thresh_b))  # channels are merged back to form 1 image
        cv2.imshow('thresholded lab color space', merged_lab)
        # cv2.waitKey(0)

        h, s, v = cv2.split(hsv)
        _, thresh_h = cv2.threshold(h, 170, 255, cv2.THRESH_BINARY_INV)
        _, thresh_s = cv2.threshold(s, 200, 255, cv2.THRESH_BINARY_INV)
        _, thresh_v = cv2.threshold(v, 170, 255, cv2.THRESH_BINARY_INV)
        hsv_thresh = cv2.merge((thresh_h, thresh_s, thresh_v))
        cv2.imshow('thresholded hsv color space', hsv_thresh)
        # cv2.waitKey(0)

        rgb = blurred_temp.copy()
        r, g, b = cv2.split(rgb)
        _, thresh_r = cv2.threshold(r, 200, 255, cv2.THRESH_BINARY_INV)
        _, thresh_g = cv2.threshold(g, 200, 255, cv2.THRESH_BINARY_INV)
        _, thresh_b = cv2.threshold(b, 180, 255, cv2.THRESH_BINARY_INV)
        rgb_thresh = cv2.merge((thresh_r, thresh_g, thresh_b))
        cv2.imshow('thresholded rgb color space', rgb_thresh)
        # cv2.waitKey(0)
        #

        thresh_out = merged_lab & (hsv_thresh | rgb_thresh)  # to get optimum threshold values the color space thresholds are combined in such a way.
        cv2.imshow('thresh_out', thresh_out)
        # cv2.waitKey(0)
        # pre-processing
        gray = cv2.cvtColor(thresh_out, cv2.COLOR_BGR2GRAY)  # 3 channel image is declined to 1 channel

        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # binarized
        cv2.imshow('thresholded image', thresh)

        kernel = np.ones((3, 3), np.uint8)

        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel,
                                  iterations=open_it)  # powerful opening is applied for noise removal
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel,
                                  iterations=close_it)  # powerful closing is applied to make sure the components are uniform

        cv2.imshow("after morphological operations", thresh)
        # cv2.waitKey(0)

        return thresh

    def watersegment(self,board_im, binary):

        # sure background area
        kernel = np.ones((3, 3), np.uint8)
        sure_bg = cv2.dilate(binary, kernel,
                             iterations=1)  # dilation increases the object boundary to background so , we are sure whatever region in the backgronund
        # is really background
        cv2.imshow('dilated image', sure_bg)
        # cv2.waitKey(0)

        # finding foreground area
        dt = cv2.distanceTransform(sure_bg, cv2.DIST_L2,5)  # calculates the distance to the closest nonzero pixel for each of the source image (distance is calculated by euclidean distance(DIST_L2) .
        # for more precise distance estimation 5x5 mask is used.
        dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255)

        _, sure_fg = cv2.threshold(dt, 10, 255, cv2.THRESH_BINARY)  # binarized to feature foreground in white pixels
        sure_fg = np.uint8(sure_fg)  # converted to unsigned 8 bit (single channel)
        cv2.imshow('sure foreground', sure_fg)
        # cv2.waitKey(0)

        # sure_fg=cv2.GaussianBlur(sure_fg,(13,13),0)
        # cv2.imshow('sure fg',sure_fg)

        ###################CONTOUR APPROXIMATION####################
        # edges = cv2.Canny(sure_fg,30,120)
        edges = cv2.Canny(sure_fg, 100, 200)
        cv2.imshow('edges', edges)
        # cv2.waitKey(0)
        _, contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ########################
        n = len(contours) - 1
        contours_ctype = sorted(contours, key=cv2.contourArea, reverse=False)[:n]  # by doing so , largest contours that is image frame itself is excluded
        #
        # contours = sorted(contours, key=lambda contours: cv2.boundingRect(contours)[0] + cv2.boundingRect(contours)[1])
        # sorted contours by x and y
        # sure_fg = cv2.cvtColor(sure_fg,cv2.COLOR_GRAY2BGR)
        print(len(contours))
        cont_area = []
        center_ms = []
        loc = []
        for contour in contours_ctype:
            ###############
            x, y, w, h = cv2.boundingRect(contour)

            area = cv2.contourArea(contour)  # found countours' area are calculated to
            if area > 35:  # compare package sizes(types) of template and defective board
                cont_area.append(area)
                loc.append((x, y, w, h))  # location of corresponding areas are retained for further usage
            #####################

        for contour in contours:

            hull = cv2.convexHull(contour)
            m = cv2.moments(hull)  # moments are calculated based on hulls
            if m["m00"] != 0:  # for perfect segmentations center of mass is calculated as it is in the documentation
                cx = int(m["m10"] / m["m00"])  # center of mass is calculated
                cy = int(m["m01"] / m["m00"])  # for translation and rotation errors
            else:
                cx, cy = 0, 0  # for defective segmentations m00 is zero therefore returns error
                # in order to prevent it , their center of mass is evaluated as 0.

            center_ms.append((cx, cy))  # found center of masses of each contours are retained in center_ms array
            cv2.drawContours(binary, [hull], 0, (255, 255, 255), 2)
            cv2.imshow('convex hull', binary)

        # unknown area
        unknown = cv2.subtract(sure_bg, sure_fg)
        cv2.imshow('unknown area', unknown)
        # cv2.waitKey(0)
        # Marker labelling
        _, markers = cv2.connectedComponents(
            sure_fg)  # there are 93 labels starting from 0-94 (1 for each white components) and 0 for background(black component)
        # print np.amax(markers)
        # Add one to all labels so that sure background is not 0, but 1
        markers = markers + 1
        # markers[boundary == 255] = 0
        markers[unknown == 255] = 0  # mark unknown are as 0
        ############333
        markers = cv2.watershed(board_im, markers)  # watershed marks boundary region with -1
        board_im[markers == -1] = [0, 0, 255]  # boundary region is glowed to red

        return board_im, cont_area, center_ms, sure_fg, loc

    def missing(self,stillFrame, def_img,threshold,opening_mis):
        ##############Missing and Misaligned Components Detection########################

        stillFrame = cv2.cvtColor(stillFrame.copy(), cv2.COLOR_BGR2GRAY)  # RGB color space is converted to gray scale
        def_img = cv2.cvtColor(def_img.copy(), cv2.COLOR_BGR2GRAY)


        print(stillFrame.shape)
        print(def_img.shape)

        size = stillFrame.shape[:2]  # number of rows and columns are retrieved
        def_img = cv2.resize(def_img, (size[1], size[0]))  # equalized sizes for further processing

        stillFrame = cv2.GaussianBlur(stillFrame, (35, 35), 0)  # Missing ICs,blurred sorely to eliminate noise
        def_img = cv2.GaussianBlur(def_img, (35, 35), 0)

        cv2.imshow('stillframe',stillFrame)
        cv2.imshow('def_img',def_img)

        difference = cv2.absdiff(stillFrame,def_img)  # absolute difference is taken for background subtraction(subtracting background and foreground images)
        cv2.imshow('difference',difference)
        _, thresholded_diff = cv2.threshold(difference, threshold, 255, cv2.THRESH_BINARY)  # binarized for misalignment and missing components

        cv2.imshow('thresholded difference ',difference)


        kernel = np.ones((5, 5), np.uint8)
        # opening is carried out for residual noise removal
        opening = cv2.morphologyEx(thresholded_diff, cv2.MORPH_OPEN, kernel,
                                   iterations=opening_mis)
        cv2.imshow('Missing/Misaligned components', opening)  # resultant image is displayed
        # cv2.waitKey(0)

        return opening

    def pol_check(self,board_im, fg_im,pol_minArea):
        global black_im
        fg_im = cv2.cvtColor(fg_im, cv2.COLOR_GRAY2BGR)
        fg_rgb = cv2.bitwise_and(board_im, fg_im)
        cv2.imshow('foreground in rgb color space', fg_rgb)

        gray_im = cv2.cvtColor(fg_rgb, cv2.COLOR_BGR2GRAY)
        _, binary_fg = cv2.threshold(gray_im, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow('binarized foreground image', binary_fg)


        ###########BLOB DETECTION
        params = cv2.SimpleBlobDetector_Params()

        # Filter by Area.
        params.filterByArea = True
        params.maxArea = 500
        params.minArea = pol_minArea
        # Filter by Circularity
        params.filterByCircularity = True
        # params.minCircularity = 0.7
        params.minCircularity = 0.3
        # Filter by Convexity
        params.filterByConvexity = True
        # params.minConvexity = 0.9
        params.minConvexity = 0.2
        # Filter by Inertia
        params.filterByInertia = True
        # params.minInertiaRatio = 0.07
        params.minInertiaRatio = 0.3

        detector = cv2.SimpleBlobDetector_create(params)
        # Detect blobs.
        keypoints = detector.detect(binary_fg)
        black_im = np.zeros((board_im.shape[0], board_im.shape[1]), dtype=np.uint8)

        im_pol = cv2.drawKeypoints(fg_rgb, keypoints, np.array([]), (255, 255, 255),
                                   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("Polarity marks on ICs", im_pol)
        im_pol = cv2.drawKeypoints(black_im, keypoints, np.array([]), (255, 255, 255),
                                   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # cv2.waitKey(0)
        return im_pol


    def OCR(self,board_im, fg_im,thresh_fg):


        global num, fg_rgb
        whole_txt = ""  #string to store all read words
        roi_ocr = 0 # initially
        roi_ctype = 0
        path_OCR = []
        a=0
        b=0
        c=0
        d=0
        x=0
        y=0
        w=0
        h=0
        # Define config parameters.
        # '-l eng'  for using the English language
        # '--oem 1' for using LSTM OCR Engine
        config = ('-l eng --oem 1 --psm 3')
        _,cont_comp,_=cv2.findContours(fg_im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print(len(cont_comp))
        fg_im = cv2.cvtColor(fg_im, cv2.COLOR_GRAY2BGR)

        if (len(cont_comp)  < 22):

            print('I am here !!!')

            fg_im = cv2.bitwise_not(fg_im)
            cv2.imshow('fg_im123',fg_im)
            # cv2.waitKey(0)

        fg_rgb = cv2.bitwise_and(board_im, fg_im)
        cv2.imshow('foreground in rgb color space', fg_rgb)
        # cv2.waitKey(0)
        gray_im = cv2.cvtColor(fg_rgb, cv2.COLOR_BGR2GRAY)

        _, binary_fg = cv2.threshold(gray_im, thresh_fg, 255, cv2.THRESH_BINARY_INV)
        to_morp = cv2.bitwise_not(binary_fg)
        cv2.imshow('binarized foreground image', binary_fg)
        cv2.imshow('inverted foreground image', to_morp)
        # cv2.waitKey(0)

        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        # dilated = cv2.dilate(to_morp, kernel, iterations=5)  # dilate
        dilated = cv2.dilate(to_morp, kernel, iterations=7)  # dilate
        cv2.imshow('dilated', dilated)
        # cv2.waitKey(0)
        _, contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours is not None :

            for i, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                print(area)


                cont_angle = 0
                x, y, w, h = cv2.boundingRect(contour)

                # cv2.rectangle(dilated.copy(),(x,y),(x+w,y+h),(0,255,0),2)

                # cv2.drawContours(dilated, contours, -1, (0, 255, 0), 2)
                cv2.imshow('dilated', dilated)
                # cv2.waitKey(0)
                # print(x,y,w,h)

                # if 5 < h < 350 and 5 < w < 350:
                if (125 < h < 350 and 50 < w < 125) | (200 < w < 350 and 50 < h < 125):  # these values are specific for this example
                # if (90 < h < 350 and 38 < w < 125) | (200 < w < 350 and 50 < h < 125):

                    roi = binary_fg[y:y + h, x: x + w]
                    roi = cv2.copyMakeBorder(roi, 55, 55, 55, 55, cv2.BORDER_CONSTANT, value=[255, 255, 255])
                    cv2.imshow('roi', roi)
                    # cv2.waitKey(0)
                    roi_ocr =dilated[y:y + h, x: x + w]
                    a,b,c,d = x,y,w,h
                    cv2.imshow('binary roi',roi_ocr)

                # print(box)
                # draw rectangle around contour on original image
                    rect_en = cv2.minAreaRect(contour)  # the contour's angle of rotation is retrieved by minAreaRect function
                # thereby I can align it horizontally to input my OCR algorithm since horizontal alignment is compulsory
                    print(rect_en[2])
                    if h > w:
                        cont_angle = 90 - rect_en[2]
                    # roi = cv2.resize(roi, (roi.shape[0], roi.shape[1]))
                    else:
                        cont_angle = -cont_angle

                    # print(h,w)
                    print(cont_angle)

                    roi = imutils.rotate_bound(roi, cont_angle)
                    cv2.imshow('rotated roi',roi)


                    cv2.imwrite(r'extracted_OCR{}.png'.format(i), roi)
                    # read_txt = pytesseract.image_to_string(Image.open(r'C:\Users\furka\PycharmProjects\imageProcessing\openCV\images\extracted_OCR{}.png'.format(ith)),config=config)
                    # cv2.imshow('Text to be recognized',upd_roi)

                ########GROUPING EACH WORD############
                    roi_i = cv2.bitwise_not(roi)
                    kernel = np.ones((1, 3), np.uint8)
                    roi_i = cv2.dilate(roi_i, kernel, iterations=5)
                    cv2.imshow('grouping', roi_i)
                    # cv2.waitKey(0)
                # OCR for these extracted rectangles

                    _, in_cnt, _ = cv2.findContours(roi_i, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # sort contours top to bottom according to x, y coordinates
                    sorted_ctrs = sorted(in_cnt,key=lambda in_cnt: cv2.boundingRect(in_cnt)[0] + cv2.boundingRect(in_cnt)[1])
                    roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)

                    # path_OCR = []

                    for (num,cont) in enumerate(sorted_ctrs,num):

                        area_cont = cv2.contourArea(cont)
                        if area_cont > 250:
                            x, y, w, h = cv2.boundingRect(cont)
                            output = roi.copy()
                            word = output[y:y + h, x: x + w]
                            word = cv2.copyMakeBorder(word, 35, 35, 35, 35, cv2.BORDER_CONSTANT, value=[255, 255, 255])
                            print(cv2.contourArea(cont))

                            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)


                            cv2.imshow('roi',output)
                        # cv2.waitKey(0)
                            cv2.imshow('word', word)
                            text = pytesseract.image_to_string(word, config='--psm 6 -l eng --oem 3')
                        # print(text)
                            whole_txt =  whole_txt + text
                        # print(whole_txt)
                        try:
                            cv2.putText(output, text, (x - 5, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        except:
                            ValueError
                        if area_cont > 250:
                            cv2.imshow('OCR image', output)
                            filepath = r'TextOCR{}.png'.format(num)
                            cv2.imwrite(filepath,output)
                            path_OCR.append(filepath)
                        # cv2.waitKey(0)
                        print(num)
                        num += 1



        if a != 0 :

            roi_ctype = dilated[b:b + d, a:a + c]
            cv2.imshow('dilated new',roi_ctype)

        return path_OCR, roi_ocr, a, b, c, d , whole_txt ,x,y,w,h , roi_ctype

    def after_OCR(self,temp_OCR,counter,path_temp,cnt_num,x,y,w,h):

        ocr_con = np.zeros((576, 728), dtype=np.uint8)
        ocr_con = cv2.cvtColor(ocr_con, cv2.COLOR_GRAY2BGR)
        if x != 0:

            cv2.imshow('temp_OCR',temp_OCR)
            # print(temp_OCR.shape)

            _,contours,_ = cv2.findContours(temp_OCR,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            temp_OCR = cv2.cvtColor(temp_OCR, cv2.COLOR_GRAY2BGR)
            counter = colouring(self,temp_OCR,125,0,255,contours,counter)

            ocr_con[y:y+h,x:x+w] = temp_OCR
            cv2.imshow('ocr context',ocr_con)
            # cv2.waitKey(0)


            ####################CLASS LABEL
            pixmap = QtGui.QPixmap(_fromUtf8("../GUI icons/OCR.png"))
            self.class_lbl = QtGui.QLabel(self.centralwidget)
            self.class_lbl.setText(_fromUtf8(""))
            self.class_lbl.setObjectName(_fromUtf8("label"))
            self.class_lbl.setFrameShape(QtGui.QFrame.Box)

            self.class_lbl.setFixedSize(QtCore.QSize(30, 30))
            self.class_lbl.setScaledContents(True)
            self.horizontalLayout.setSpacing(10)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.horizontalLayout.addWidget(self.class_lbl)
            #########################
            self.class_lbl.deleteLater()
            ################333
            pixmap = pixmap.scaled(self.class_lbl.width(), self.class_lbl.height(), QtCore.Qt.KeepAspectRatio)
            self.class_lbl.setPixmap(pixmap)

            self.def_loc = QtGui.QLabel(self.centralwidget)
            self.def_loc.setFixedSize(QtCore.QSize(30, 30))
            self.horizontalLayout.addWidget(self.def_loc)
            #########################
            self.def_loc.deleteLater()
            ################333
            self.def_loc.setNum(cnt_num + 1)
            QtGui.QApplication.processEvents()
            ###########

            return ocr_con

    def CaptureFrame_solder(self,path_temp,path_def):
            ############33
            #previously captured frames are removed to prevent overflow
            if os.path.exists(path_temp):
                os.remove(path_temp)
                os.remove(path_def)
            else:
                print("The file does not exist")



            temp = 0
            defect = 0

            cap = cv2.VideoCapture(1)
            # cv2.namedWindow("Input stream")

            while (True):
                    ret, frame = cap.read()

                    cv2.imshow("Captured frame", frame)

                    if not ret:
                            break
                    elif cv2.waitKey(1) == 27:  # ESC is pressed, get out of the loop
                            break
                    elif cv2.waitKey(1) == 32:  # Space is pressed , write the captured template board image

                            for i in range(1, 31):  # loop 30 times

                                    cv2.imwrite(
                                            r'solder Template board image' + str(
                                                    i) + '.JPEG', frame)
                                    a = cv2.imread(
                                            r'solder Template board image' + str(
                                                    i) + '.JPEG').astype('float64')
                                    temp = temp + a  # so as to prevent overflow the image is stored as float64 datatype rather than unsigned 8 bits

                            # print(temp.dtype)
                            temp = temp / 30
                            temp = temp.astype('uint8')
                            # print(temp.dtype)
                            cv2.imwrite(path_temp,temp)
                            # cv2.imshow('averaged template board image', temp)
                            ###########
                            pixmap = QtGui.QPixmap(path_temp)
                            # self.horizontalLayout.addWidget(self.label)
                            # self.horizontalLayout.setAlignment(QtCore.Qt.AlignLeft)
                            pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(),QtCore.Qt.KeepAspectRatio)
                            self.BoardImage.setPixmap(pixmap)
                            self.BoardImage.setAlignment(QtCore.Qt.AlignLeft)
                            ###########
                    elif cv2.waitKey(
                            1) == 8:  # Backspace is pressed once again , write the captured defective board image
                            for i in range(1, 31):
                                    cv2.imwrite(
                                            r'solder Defective board image' + str(
                                                    i) + '.JPEG', frame)
                                    b = cv2.imread(
                                            r'solder Defective board image' + str(i) + '.JPEG').astype('float64')
                                    defect = defect + b

                            defect = defect / 30
                            defect = defect.astype('uint8')
                            cv2.imwrite(path_def,defect)
                            # cv2.imshow('averaged defective board image', defect)
                            ###########IMAGE SHOWN IN QLABEL
                            pixmap = QtGui.QPixmap(path_def)
                            pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(),QtCore.Qt.KeepAspectRatio)
                            self.BoardImage_2.setPixmap(pixmap)
                            self.BoardImage_2.setAlignment(QtCore.Qt.AlignRight)
                            ###########

            cap.release()
            cv2.destroyAllWindows()
            return temp, defect


            return

    def solderjoint_1(self,pathway_temp,pathway_def):

        cnt_num = 0 # initial countour number
        counter = 0
        temp_im = cv2.imread(pathway_temp)
        def_im = cv2.imread(pathway_def)
        temp_im = cv2.resize(temp_im, (728, 576))
        def_im = cv2.resize(def_im, (728, 576))
        # cv2.waitKey(0)

        ###########################
        pixmap = QtGui.QPixmap(pathway_def)
        pixmap = pixmap.scaled(self.BoardImage.width(), self.BoardImage.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage.setPixmap(pixmap)

        ###########################
        QtGui.QApplication.processEvents()
        pixmap = QtGui.QPixmap(pathway_temp)
        pixmap = pixmap.scaled(self.BoardImage_3.width(), self.BoardImage_3.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage_3.setPixmap(pixmap)
        #################
        cv2.imshow('temp_im', temp_im)
        cv2.imshow('def_im', def_im)


        temp_im = align_2(self,temp_im, def_im)
        temp_im = cv2.GaussianBlur(temp_im,(5,5),0)
        def_im =  cv2.GaussianBlur(def_im, (5, 5), 0)


        gray_temp = cv2.cvtColor(temp_im,cv2.COLOR_BGR2GRAY)
        gray_def = cv2.cvtColor(def_im, cv2.COLOR_BGR2GRAY)



        _, thresh_temp = cv2.threshold(gray_temp, 80, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
        _, thresh_def = cv2.threshold(gray_def, 90, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)


        cv2.imshow('thresh_temp', thresh_temp)
        cv2.imshow('thresh_def', thresh_def)

        thresh_def = cv2.morphologyEx(thresh_def, cv2.MORPH_CLOSE, kernel=np.ones((3, 3), np.uint8), iterations=6)
        thresh_def = cv2.morphologyEx(thresh_def, cv2.MORPH_OPEN, kernel=np.ones((3, 3), np.uint8), iterations=0)

        thresh_temp = cv2.morphologyEx(thresh_temp, cv2.MORPH_CLOSE, kernel=np.ones((3, 3), np.uint8), iterations=6)
        thresh_temp = cv2.morphologyEx(thresh_temp, cv2.MORPH_OPEN, kernel=np.ones((3, 3), np.uint8), iterations=0)

        cv2.imshow('after morphology ,thresh_temp', thresh_temp)
        cv2.imshow('after morphology, thresh_def', thresh_def)

        short = thresh_def - thresh_temp
        open = thresh_temp - thresh_def
        short = cv2.medianBlur(short,25)
        open = cv2.medianBlur(open,13)
        cv2.imshow('open',open)
        cv2.imshow('short',short)
        # cv2.waitKey(0)



        open_edges = cv2.Canny(open.copy(),30,120)
        short_edges = cv2.Canny(short.copy(),30,120)

        contours,cnt_num = roi(self,short_edges,def_im,cnt_num,blur_roi=1 ,lbl_path=_fromUtf8("../GUI icons/short.jpg"))
        short = cv2.cvtColor(short,cv2.COLOR_GRAY2BGR)
        counter = colouring(self,short,255,255,0,contours,counter)

        contours,cnt_num = roi(self,open_edges,def_im,cnt_num, blur_roi=1,lbl_path=_fromUtf8("../GUI icons/nosolder.jpg"))
        open = cv2.cvtColor(open,cv2.COLOR_GRAY2BGR)
        _ = colouring(self,open,255,191,0,contours,counter)


        thresh_def = cv2.cvtColor(thresh_def, cv2.COLOR_GRAY2BGR)
        defects_col = short ^ open ^ thresh_def
        # defects_col = short ^ open ^ def_im

        cv2.imshow('colored assembled board defects',defects_col)


        background = np.zeros((630, 800, 3), np.uint8)  # black background created for legend

        background[0:576, 0:728] = defects_col  # relevant part of defects are copied onto background image
        background[555:620, 0:728] = np.asarray([255, 255, 255])  # white background for visible texts
        background[0:630, 728:800] = np.asarray([255, 255, 255])
        # group defects are added as legend at the bottom of the all classified defects

        cv2.putText(background, 'Short / Bridging Defect', (50, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    # (139, 0, 139), 2)
                    (0,0,255),2)
        cv2.putText(background,
                    'Open(No solder) Defect',
                    (50, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 191, 0), 2)

        # cv2.imshow('Classified defects', background)
        cv2.imwrite(r'solder_classified.JPEG', background)
        ################
        pixmap = QtGui.QPixmap(r'solder_classified.JPEG')
        pixmap = pixmap.scaled(self.BoardImage_2.width(), self.BoardImage_2.height(), QtCore.Qt.KeepAspectRatio)
        self.BoardImage_2.setPixmap(pixmap)
        self.BoardImage_2.setAlignment(QtCore.Qt.AlignRight)
        # QtGui.QApplication.processEvents()



        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return




    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Optical Inspection", None))
        self.imLoadbtn.setText(_translate("mainWindow", "LOAD IMAGE", None))
        self.inspectbtn.setText(_translate("mainWindow", "Inspect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plain), _translate("mainWindow", "Plain", None))
        self.imLoadbtn_2.setText(_translate("mainWindow", "LOAD IMAGE", None))
        self.inspectbtn_2.setText(_translate("mainWindow", "Inspect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Assembled), _translate("mainWindow", "Assembled", None))
        #######
        self.imLoadbtn_3.setText(_translate("mainWindow", "LOAD IMAGE", None))
        self.inspectbtn_3.setText(_translate("mainWindow", "Inspect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.solderjoint), _translate("mainWindow", "Solder Joint", None))
        #########

        self.BareBoardLbl.setText(_translate("mainWindow", "Bare Board Inspection", None))
        self.AssembledBoardLbl.setText(_translate("mainWindow", "Assembled Board Inspection", None))
        self.AssembledBoardLbl_2.setText(_translate("mainWindow", "Solder Joint Inspection", None))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar", None))
        self.actionCorrect_Type.setText(_translate("mainWindow", "Correct Type", None))
        self.actionPolarity_Check.setText(_translate("mainWindow", "Polarity  Check", None))
        self.actionMissing_Component.setText(_translate("mainWindow", "Missing - Misaligned comp.", None))
        # self.actionComponent_Orientation.setText(_translate("mainWindow", "Comp. Orientation", None))
        self.actionInspect.setText(_translate("mainWindow", "Inspect", None))
        self.actionOCR.setText(_translate("mainWindow", "OCR", None))
        self.actionShort_Circuit.setText(_translate("mainWindow", "Short Circuit , spur , underetch , Cond. too close", None))
        self.actionShort_Circuit.setToolTip(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#aa5500;\">Short Circuit , spur ,</span></p><p><span style=\" font-size:11pt; color:#aa5500;\">underetch , Cond. too close</span></p></body></html>", None))
        self.actionOpen_Circuit.setText(_translate("mainWindow", "Open Circuit , mouse bite , over etch,Cond. too close", None))
        self.actionMissing_Wrong_Size_Hole.setText(_translate("mainWindow", "Missing - Wrong Size Hole", None))
        self.actionMissing_Wrong_Size_Hole.setToolTip(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Missing - Wrong Size Hole</span></p></body></html>", None))
        self.actionPinhole_Breakout.setText(_translate("mainWindow", "Pinhole - Breakout", None))
        self.actionPinhole_Breakout.setToolTip(_translate("mainWindow", "Pinhole - Breakout", None))
        self.actionShort_Bridging.setText(_translate("mainWindow", "Short/Bridging", None))
        self.actionOpen.setText(_translate("mainWindow", "Open", None))



if __name__ == '__main__':

    #
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    #######33
    ui.setupUi(mainWindow)
    ####
    mainWindow.show()
    sys.exit(app.exec_())



#################
#
