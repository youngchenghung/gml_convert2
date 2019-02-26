# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GmlConverterDialog
                                 A QGIS plugin
 GmlConverter
                             -------------------
        begin                : 2019-02-13
        git sha              : $Format:%H$
        copyright            : (C) 2019 by  
        email                :  
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import *
from qgis.core import *
from qgis.utils import *

from ui_gml_open_file import Ui_GmlOpenFile
from ui_drop_zd import Ui_DropZD

class DropZDDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self, iface.mainWindow())
        self.ui = Ui_DropZD()
        self.ui.setupUi(self)

class GmlOpenFileDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self, iface.mainWindow())
        self.ui = Ui_GmlOpenFile()
        self.ui.setupUi(self)
