# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GmlConverter
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from qgis.utils import *
from qgis.gui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
#from qgis.core import QgsVectorJoinInfo
# Import the code for the dialog
from gml_converter_dialog import DropZDDialog, GmlOpenFileDialog
import os.path


class GmlConverter:

    def __init__(self, iface):
        self.iface = iface
        self.canves = self.iface.mapCanvas()
        self.dir = None

        #self.drop_zd_dlg = DropZDDialog()
        #self.drop_zd_dlg.setWindowTitle(u'三維轉二維')

        self.gml_open_file_dlg = GmlOpenFileDialog()
        self.gml_open_file_dlg.setWindowTitle(u'gml檔案轉移')

    def initGui(self):
        self.menu = QMenu(self.iface.mainWindow())
        self.menu.setTitle(u'gml檔案轉移')

        self.toolBar = self.iface.addToolBar(u'gml檔案轉移')
        self.toolBar.setObjectName('GmlConverterTool')

        #self.action_drop_zd = QAction(QIcon("C:/Users/tesla/.qgis2/python/plugins/GmlConverter/Drop_ZD.png"), u"三維轉二維", self.iface.mainWindow())
        #self.action_drop_zd.setCheckable(True)
        #self.action_drop_zd.triggered.connect(self.drop_zd_init)
        #self.toolBar.addAction(self.action_drop_zd)

        self.action_gml_open_file = QAction(QIcon("C:/Users/tesla/.qgis2/python/plugins/GmlConverter/GmlConverter.png"), u"gml檔案轉移", self.iface.mainWindow())
        self.action_gml_open_file.setCheckable(True)
        self.action_gml_open_file.triggered.connect(self.gml_open_file_init)
        self.toolBar.addAction(self.action_gml_open_file)

        self.gml_open_file_dlg.ui.cancel.clicked.connect(self.gml_cancel)
        self.gml_open_file_dlg.ui.open_gml.clicked.connect(self.gml_open)
        self.gml_open_file_dlg.ui.convert.clicked.connect(self.convert)
        self.gml_open_file_dlg.ui.convert_2.clicked.connect(self.get_finish_id)
        

    def unload(self):
        
        #self.iface.removeToolBarIcon(self.action_drop_zd)
        #self.iface.removePluginMenu(u"&三維轉二維", self.action_drop_zd)
        self.iface.removeToolBarIcon(self.action_gml_open_file)
        self.iface.removePluginMenu(u"&gml檔案轉移", self.action_gml_open_file)

    '''
    def drop_zd_init(self):

        self.mapInstance = QgsMapLayerRegistry.instance()
        self.mapLayers = self.mapInstance.mapLayers()
        if (len(self.mapLayers) < 2):
            QMessageBox.information(self.iface.mainWindow(), 
                                    "Error", 
                                    u"請先開啟系統圖資")
            return
        
        layers = self.iface.legendInterface().layers()


        for layer in layers:
            layerType = layer.type()
            if layerType == QgsMapLayer.VectorLayer:
                if layer.name() == "admin":
                    break

        layer = QFileDialog()
        path1 = "C:/Users/tesla/Desktop/PDS2QGIS"
        title = ""
        filter = "gml(*.gml)"
        dir = QFileDialog.getOpenFileName(layer, title, path1, filter)

        fileName = dir
        layer = QgsVectorLayer(fileName, fileName[32:], "ogr")
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        output_fileName = fileName[32:]
        path2 = r"C:/Users/tesla/Desktop/gmlfile/" + output_fileName
        if output_fileName == "EUMETER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "EUPIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "HYDRANT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "MANHOLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "METER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PACKER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PCROSS.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "PIPECOVER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPEHAT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "SADDLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "STATION.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "VALVE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)
        #
        ########################################################
        
        layer = QFileDialog()
        path1 = "C:/Users/tesla/Desktop/gmlfile/"
        title = ""
        filter = "shp(*.shp)"
        dir = QFileDialog.getOpenFileName(layer, title, path1, filter)

        fileName = dir
        layer = QgsVectorLayer(fileName, fileName[31:], "ogr")
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        output_fileName2 = 'New_' + fileName[31:]
        path2 = r"C:/Users/tesla/Desktop/gmlfile/" + output_fileName2
        if output_fileName == "EUMETER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "EUPIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "HYDRANT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "MANHOLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "METER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PACKER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PCROSS.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "PIPECOVER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPEHAT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "SADDLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "STATION.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "VALVE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        print("wkbType" + str(layer.wkbType()))
        
        
        layer = QFileDialog()
        path1 = "C:/Users/tesla/Desktop/PDS2QGIS"
        title = ""
        filter = "gml(*.gml)"
        dir = QFileDialog.getOpenFileName(layer, title, path1, filter)

        fileName = dir
        layer = QgsVectorLayer(fileName, fileName[32:], "ogr")
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        output_fileName = fileName[32:]
        path2 = r"C:/Users/tesla/Desktop/gmlfile/" + output_fileName
        QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiLineString)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)
        #
        ########################################################

        layer = QFileDialog()
        path1 = "C:/Users/tesla/Desktop/gmlfile/"
        title = ""
        filter = "shp(*.shp)"
        dir = QFileDialog.getOpenFileName(layer, title, path1, filter)

        fileName = dir
        layer = QgsVectorLayer(fileName, fileName[31:], "ogr")
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        output_fileName2 = 'New_' + fileName[31:]
        path2 = r"C:/Users/tesla/Desktop/gmlfile/" + output_fileName2
        QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiLineString)
        print("wkbType" + str(layer.wkbType()))
        '''
    # gml檔案轉移 - 啟動點
    def gml_open_file_init(self):
        self.mapInstance = QgsMapLayerRegistry.instance()
        self.mapLayers = self.mapInstance.mapLayers()
        if (len(self.mapLayers) < 2):
            QMessageBox.information(self.iface.mainWindow(), "Error", u"請先開啟系統圖資")
            return
        
        layers = self.iface.legendInterface().layers()

        for layer in layers:
            layerType = layer.type()
            if layerType == QgsMapLayer.VectorLayer:
                if layer.name() == "admin":
                    break

        self.gml_open_file_dlg.show()

    # 開啟圖層 - 加入圖層
    def gml_open(self):

        # 開啟檔案對話框
        layer = QFileDialog()
        # 路徑
        path1 = "C:/Users/tesla/Desktop/PDS2QGIS"
        # 黨名
        title = ""
        # 檔案格式
        filter = "gml(*.gml)"
        dir = QFileDialog.getOpenFileName(layer, title, path1, filter)
        fileName = dir

        # 載入圖層
        layer = QgsVectorLayer(fileName, fileName[32:], "ogr")
        # 座標設定為3826
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        # 轉換gml圖檔為shp圖檔，幾何類型三維轉二維
        output_fileName = fileName[32:]
        path2 = r"C:/Users/tesla/Desktop/gmlfile/" + output_fileName
        if output_fileName == "EUMETER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "EUPIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "HYDRANT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "MANHOLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "METER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PACKER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PCROSS.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "PIPECOVER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPEHAT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "SADDLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "STATION.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "VALVE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"ESRI Shapefile", overrideGeometryType=QgsWKBTypes.MultiPoint)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)
        #
        ########################################################
        
        # 轉換shp圖檔為gml圖檔
        layer = QFileDialog()
        path1 = "C:/Users/tesla/Desktop/gmlfile/"
        title = ""
        filter = "shp(*.shp)"
        dir = QFileDialog.getOpenFileName(layer, title, path1, filter)

        fileName = dir
        layer = QgsVectorLayer(fileName, fileName[31:], "ogr")
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        output_fileName2 = 'New_' + fileName[31:]
        path2 = r"C:/Users/tesla/Desktop/gmlfile/" + output_fileName2
        if output_fileName == "EUMETER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "EUPIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "HYDRANT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "MANHOLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "METER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PACKER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PCROSS.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiLineString)
        elif output_fileName == "PIPECOVER.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "PIPEHAT.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "SADDLE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "STATION.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        elif output_fileName == "VALVE.gml":
            QgsVectorFileWriter.writeAsVectorFormat(layer, path2, "utf-8", None,"GML", overrideGeometryType=QgsWKBTypes.MultiPoint)
        print("wkbType" + str(layer.wkbType()))

        ########################################################


        # 開啟gml圖檔
        layer = QFileDialog()
        path = "C:/Users/tesla/Desktop/gmlfile/"
        title = ""
        filter = "gml(*.gml)"
        self.dir = QFileDialog.getOpenFileName(layer, title, path, filter)

        self.gml_open_file_dlg.ui.label_open_gml.setText(self.dir)

        ########################################################

        # 載入圖層
        print (self.dir)
        fileName = self.dir
        layer = QgsVectorLayer(self.dir, fileName[35:], "ogr")
        crs = layer.crs()
        crs.createFromId(3826)
        layer.setCrs(crs)

        QgsMapLayerRegistry.instance().addMapLayer(layer)
        
    # 圖徵轉入資料庫
    def convert(self):

        # 點選圖層為主要轉入圖層
        layer = iface.activeLayer()
        if layer.name() == "EUMETER.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('eumter')[0]
            #iface.setActiveLayer(sourceLYR)
            # Set the selection on the source layer (Could also be done manually with the selection tools
            #sourceLYR = layer.selectedFeatures()
        elif layer.name() == "EUPIPE.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('eupipe')[0]
        elif layer.name() == "HYDRANT.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('hydrant')[0]
        elif layer.name() == "MANHOLE.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('manhole')[0]
        elif layer.name() == "METER.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('meter')[0]
        elif layer.name() == "PACKER.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('packer')[0]
        elif layer.name() == "PCROSS.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('Pcross')[0]
        elif layer.name() == "PIPE.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('pipe')[0]
        elif layer.name() == "PIPECOVER.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('pipecover')[0]
        elif layer.name() == "PIPEHAT.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('pipehat')[0]
        elif layer.name() == "SADDLE.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('saddle')[0]
        elif layer.name() == "STATION.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('station')[0]
        elif layer.name() == "VALVE.gml.shp.gml":
            sourceLYR = iface.legendInterface().selectedLayers()
            # Make the source layer active
            destLYR = QgsMapLayerRegistry.instance().mapLayersByName('valve')[0]
        # Copy
        iface.actionCopyFeatures().trigger()
        # Set destination layer active
        iface.setActiveLayer(destLYR)
        # Turn on editing on destination layer, so we can paste
        destLYR.startEditing()
        # Paste features
        iface.actionPasteFeatures().trigger()
        destLYR.updateFields()
        destLYR.commitChanges()

    # 取得 finish_id 識別碼
    def get_finish_id(self):
        db_conn = self.get_db_connection()        
        
        layer = iface.activeLayer()
        selection = layer.selectedFeatures()
        
        for f in selection: 
            #print f[0]
            self.gid = f[0]

            query_string = u'SELECT * FROM work_unit'
            query = db_conn.exec_(query_string)
            if query.isActive():
                while query.next():
                    self.unitcode = query.value(0)
            #print(self.unitcode)
        query.clear()
        db_conn.close()
            
        if layer.name() == 'pipe':
            self.point = f.geometry().asMultiPolyline()[0][0]
            #print self.point
            self.pipe_sn()
        elif layer.name() == 'eumeter':
            self.Lpoint = f.geometry().asPoint()
            #print self.Lpoint
            self.eumeter_sn()
        elif layer.name() == 'eupipe':
            QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'eupip 無 FINISH_ID !')
            pass
        elif layer.name() == 'hydrant':
            self.Lpoint = f.geometry().asPoint()
            #print self.Lpoint
            self.hydrant_sn()
        elif layer.name() == 'manhole':
            self.Lpoint = f.geometry().asPoint()
            #print self.Lpoint
            self.manhole_sn()
        elif layer.name() == 'meter':
            self.Lpoint = f.geometry().asPoint()
            #print self.Lpoint
            self.meter_sn()
        elif layer.name() == 'packer':
            QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'packer 無 FINISH_ID !')
            pass
        elif layer.name() == 'pcross':
            QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'pcross 無 FINISH_ID !')
            pass
        elif layer.name() == 'pipecover':
            QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'pipecover 無 FINISH_ID !')
            pass
        elif layer.name() == 'saddle':
            QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'saddle 無 FINISH_ID !')
            pass
        elif layer.name() == 'station':
            self.Lpoint = f.geometry().asPoint()
            #print self.Lpoint
            self.station_sn()
        elif layer.name() == 'valve':
            self.Lpoint = f.geometry().asPoint()
            #print self.Lpoint
            self.valve_sn()

    # 管線 - 建立 finish_id 識別碼
    def pipe_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.point.x()) + ' ' + str(self.point.y())
        #print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)
        #print(self.frame_no)

        query_string = u'SELECT gid FROM pipe WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)

        query_string = u'SELECT pipe_mtr FROM pipe WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                pipe_mtr = query.value(0)
                #print(pipe_mtr)
                if pipe_mtr == u'CIP':
                    self.type_id = u'0'
                elif pipe_mtr == u'DIP':
                    self.type_id = u'1'
                elif pipe_mtr == u'SP':
                    self.type_id = u'2'
                elif pipe_mtr == u'SSP':
                    self.type_id = u'3'
                elif pipe_mtr == u'GIP':
                    self.type_id = u'4'
                elif pipe_mtr == u'PVCP':
                    self.type_id = u'5'
                elif pipe_mtr == u'PVCP/PE':
                    self.type_id = u'6'
                elif pipe_mtr == u'ABSP':
                    self.type_id = u'7'
                elif pipe_mtr == u'PEP':
                    self.type_id = u'8'
                elif pipe_mtr == u'HIWP':
                    self.type_id = u'9'
                elif pipe_mtr == u'RCP':
                    self.type_id = u'A'
                elif pipe_mtr == u'PSCP':
                    self.type_id = u'B'
                elif pipe_mtr == u'PCCP':
                    self.type_id = u'C'
                elif pipe_mtr == u'PESP':
                    self.type_id = u'D'
                elif pipe_mtr == u'FRP':
                    self.type_id = u'E'
                elif pipe_mtr == u'ACP':
                    self.type_id = u'X'
                elif pipe_mtr == u'PBP':
                    self.type_id = u'Y'
                elif pipe_mtr == u'LP':
                    self.type_id = u'Z'
                else:
                    self.type_id = u''
                #print self.type_id

        query_string = u'SELECT pipe_size FROM pipe WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                pipe_size = query.value(0)
                #print(pipe_size)
                if pipe_size == u'13' or pipe_size == u'16':
                    self.std = u'0'
                elif pipe_size == u'20':
                    self.std = u'1'
                elif pipe_size == u'25':
                    self.std = u'2'
                elif pipe_size == u'33':
                    self.std = u'3'
                elif pipe_size == u'40':
                    self.std = u'4'
                elif pipe_size == u'50':
                    self.std = u'5'
                elif pipe_size == u'65':
                    self.std = u'6'
                elif pipe_size == u'75' or pipe_size == u'80':
                    self.std = u'7'
                elif pipe_size == u'100':
                    self.std = u'8'
                elif pipe_size == u'125':
                    self.std = u'9'
                elif pipe_size == u'150':
                    self.std = u'A'
                elif pipe_size == u'200':
                    self.std = u'B'
                elif pipe_size == u'250':
                    self.std = u'C'
                elif pipe_size == u'300':
                    self.std = u'D'
                elif pipe_size == u'350':
                    self.std = u'E'
                elif pipe_size == u'400':
                    self.std = u'F'
                elif pipe_size == u'450':
                    self.std = u'G'
                elif pipe_size == u'500':
                    self.std = u'H'
                elif pipe_size == u'600':
                    self.std = u'I'
                elif pipe_size == u'700':
                    self.std = u'J'
                elif pipe_size == u'800':
                    self.std = u'K'
                elif pipe_size == u'900':
                    self.std = u'L'
                elif pipe_size == u'1000':
                    self.std = u'M'
                elif pipe_size == u'1100':
                    self.std = u'N'
                elif pipe_size == u'1200':
                    self.std = u'O'
                elif pipe_size == u'1350':
                    self.std = u'P'
                elif pipe_size == u'1500':
                    self.std = u'Q'
                elif pipe_size == u'1750':
                    self.std = u'R'
                elif pipe_size == u'1800':
                    self.std = u'S'
                elif pipe_size == u'2000':
                    self.std = u'T'
                elif pipe_size == u'2200':
                    self.std = u'U'
                elif pipe_size == u'2400':
                    self.std = u'V'
                elif pipe_size == u'2600':
                    self.std = u'W'
                elif pipe_size == u'3200':
                    self.std = u'X'
                else:
                    self.std = u''
                #print self.std


            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'01' + self.type_id + self.std + self.serial_number.zfill(3)
            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'01' + self.type_id + self.std + self.serial_number_jump.zfill(3)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE pipe SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)
            print query_string
            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
            
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 用戶水表 - 建立 finish_id 識別碼
    def eumeter_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.Lpoint.x()) + ' ' + str(self.Lpoint.y())
        print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)

        query_string = u'SELECT gid FROM pipe WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)
                print self.id

        query_string = u'SELECT meter_tag FROM eumeter WHERE gid={}'.format(self.gid)
        print query_string
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                meter_tag = query.value(0)
                if meter_tag == u'2':
                    self.type_id = u'2'
                elif meter_tag == u'3':
                    self.type_id = u'3'
                elif meter_tag == u'4':
                    self.type_id = u'4'
                elif meter_tag == u'5':
                    self.type_id = u'5'
                elif meter_tag == u'6':
                    self.type_id = u'6'
                elif meter_tag == u'7':
                    self.type_id = u'7'
                else:
                    self.type_id = u'8'
                print meter_tage
            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'05' + self.type_id + u'0' + self.serial_number.zfill(5)
            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'05' + self.type_id + u'0' + self.serial_number_jump.zfill(5)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE eumeter SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)
            print query_string
            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
            
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 消防栓 - 建立 finish_id 識別碼
    def hydrant_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.Lpoint.x()) + ' ' + str(self.Lpoint.y())
        print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)

        query_string = u'SELECT gid FROM pipe WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)

        query_string = u'SELECT hydrant_type FROM hydrant WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                meter_tag = query.value(0)
                if hydrant_type == u'0':
                    self.type_id = u'0'
                elif hydrant_type == u'1':
                    self.type_id = u'1'
                elif hydrant_type == u'2':
                    self.type_id = u'2'
                elif hydrant_type == u'3':
                    self.type_id = u'3'
                elif hydrant_type == u'4':
                    self.type_id = u'4'
                elif hydrant_type == u'5':
                    self.type_id = u'5'

            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'03' + self.type_id + u'0' + self.serial_number.zfill(3)
            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'03' + self.type_id + u'0' + self.serial_number_jump.zfill(3)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE eumeter SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)
            print query_string
            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
            
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 人手孔 - 建立 finish_id 識別碼
    def manhole_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.Lpoint.x()) + ' ' + str(self.Lpoint.y())
        print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)

        query_string = u'SELECT gid FROM manhole WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)
        
        query_string = u'SELECT cover_type FROM manhole WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                cover_type = query.value(0)
                if cover_type == u'1':
                    self.type_id = u'1'
                elif cover_type == u'2':
                    self.type_id = u'2'
                    print cover_type

            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'02' + self.type_id + u'0' + self.serial_number.zfill(3)

            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'02' + self.type_id + u'0' + self.serial_number_jump.zfill(3)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE manhole SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)

            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
            
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 總水量計表 - 建立 finish_id 識別碼
    def meter_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.Lpoint.x()) + ' ' + str(self.Lpoint.y())
        print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)

        query_string = u'SELECT gid FROM meter WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)

        query_string = u'SELECT meter_type FROM meter WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                meter_type = query.value(0)
                if meter_type == u'0':
                    self.type_id = u'0'
                elif meter_type == u'1':
                    self.type_id = u'1'
                elif meter_type == u'2':
                    self.type_id = u'2'
                elif meter_type == u'3':
                    self.type_id = u'3'
                elif meter_type == u'4':
                    self.type_id = u'4'
                elif meter_type == u'5':
                    self.type_id = u'5'
                elif meter_type == u'6':
                    self.type_id = u'6'
                elif meter_type == u'7':
                    self.type_id = u'7'
                elif meter_type == u'8':
                    self.type_id = u'8'
                elif meter_type == u'9':
                    self.type_id = u'9'
                elif meter_type == u'A':
                    self.type_id = u'A'
                elif meter_type == u'B':
                    self.type_id = u'B'
                elif meter_type == u'C':
                    self.type_id = u'C'

            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'06' + self.type_id + u'0' + self.serial_number.zfill(3)
            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'06' + self.type_id + u'0' + self.serial_number_jump.zfill(3)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE meter SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)
            print query_string
            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
            
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 淨水廠 - 建立 finish_id 識別碼
    def station_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.Lpoint.x()) + ' ' + str(self.Lpoint.y())
        print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)

        query_string = u'SELECT gid FROM station WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)

        query_string = u'SELECT stan_type FROM station WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                stan_type = query.value(0)
                if stan_type == u'0':
                    self.type_id = u'0'
                elif stan_type == u'1':
                    self.type_id = u'1'
                elif stan_type == u'2':
                    self.type_id = u'2'
                elif stan_type == u'3':
                    self.type_id = u'3'
                elif stan_type == u'4':
                    self.type_id = u'4'
                elif stan_type == u'5':
                    self.type_id = u'5'
                elif stan_type == u'6':
                    self.type_id = u'6'
                elif stan_type == u'7':
                    self.type_id = u'7'

            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'97' + self.type_id + u'0' + self.serial_number.zfill(3)
            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'97' + self.type_id + u'0' + self.serial_number_jump.zfill(3)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE station SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)
            print query_string
            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
            
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 閥類 - 建立 finish_id 識別碼
    def valve_sn(self):
        db_conn = self.get_db_connection()

        self.point_xy = str(self.Lpoint.x()) + ' ' + str(self.Lpoint.y())
        print self.point_xy
        query_string = u'SELECT no FROM frame WHERE ST_Contains(the_geom, ST_GeometryFromText(\'POINT({})\', 4326))'.format(self.point_xy)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.frame_no = query.value(0)
                print 1
        query_string = u'SELECT gid FROM valve WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.id = query.value(0)
                print 2

        query_string = u'SELECT valve_type FROM valve WHERE gid={}'.format(self.gid)
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                valve_type = query.value(0)
                if valve_type == u'0':
                    self.type_id = u'0'
                elif valve_type == u'1':
                    self.type_id = u'1'
                elif valve_type == u'2':
                    self.type_id = u'2'
                elif valve_type == u'3':
                    self.type_id = u'3'
                elif valve_type == u'4':
                    self.type_id = u'4'
                elif valve_type == u'5':
                    self.type_id = u'5'
                elif valve_type == u'6':
                    self.type_id = u'6'
                elif valve_type == u'7':
                    self.type_id = u'7'
                elif valve_type == u'8':
                    self.type_id = u'8'
                elif valve_type == u'9':
                    self.type_id = u'9'
                elif valve_type == u'A':
                    self.type_id = u'A'
                elif valve_type == u'B':
                    self.type_id = u'B'
                elif valve_type == u'C':
                    self.type_id = u'C'
                elif valve_type == u'D':
                    self.type_id = u'D'
                elif valve_type == u'E':
                    self.type_id = u'E'

            self.get_serial_number()
            finish_id = self.unitcode + self.frame_no + u'04' + self.type_id + u'0' + self.serial_number.zfill(3)
            if not self.serial_number_jump == u'0':
                finish_id = self.unitcode + self.frame_no + u'04' + self.type_id + u'0' + self.serial_number_jump.zfill(3)

            db_conn = self.get_db_connection()
            query_string = u'UPDATE valve SET finish_id={} WHERE gid={}'.format(finish_id, self.gid)
            query = db_conn.exec_(query_string)

            if query.isActive():
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 成功!')
            else:
                QMessageBox.information(self.iface.mainWindow(), u'GET FINSH_ID', u'取得 FINSH_ID 失敗!')
                
            query.clear()
            db_conn.close()
        query.clear()
        db_conn.close()

    # 取得識別碼
    def get_serial_number(self):
        layer = iface.activeLayer()
        db_conn = self.get_db_connection()  


        query_string = u'SELECT * FROM work_unit'
        query = db_conn.exec_(query_string)
        if query.isActive():
            while query.next():
                self.unitcode = query.value(0)

        # 目前識別碼最大的序號
        serial_number_max = 0
        # 記錄跳號
        serial_number_jump = 0
        # 查詢 finish_id 之字串，由區處編號 + 索引圖碼 + 類別碼 + 種類 + 規格 + 序號
        if layer.name() == 'pipe':
            finish_id = self.unitcode + self.frame_no + u'01' + self.type_id + self.std + u'%'
        elif layer.name() == 'eumeter':
            finish_id = self.unitcode + self.frame_no + u'05' + self.type_id + u'0' + u'%'
        elif layer.name() == 'hydrant':
            finish_id = self.unitcode + self.frame_no + u'03' + self.type_id + u'%'
        elif layer.name() == 'manhole':
            finish_id = self.unitcode + self.frame_no + u'02' + self.type_id + u'0' + u'%'
        elif layer.name() == 'meter':
            finish_id = self.unitcode + self.frame_no + u'06' + self.type_id + u'0' + u'%'
        elif layer.name() == 'station':
            finish_id = self.unitcode + self.frame_no + u'97' + self.type_id + u'0' + u'%'
        elif layer.name() == 'valve':
            finish_id = self.unitcode + self.frame_no + u'04' + self.type_id + u'0' + u'%'
        #print finish_id
        # 查詢目前識別碼最大的序號
        query_string = u'SELECT substring(finish_id, 20, 3) FROM pipe WHERE finish_id LIKE \'{}\' ORDER BY substring(finish_id, 20, 3) DESC LIMIT 1'.format(finish_id)
        #print '1' + query_string

        query = db_conn.exec_(query_string)
        if query.isActive():
            # 當 query 有資料時，代表有記錄，若無記錄 serial_number_max 維持 0
            while query.next():
                serial_number_max = int(query.value(0))

        # 資料表欄位已有序號時，該 索引圖框 已有資料了
        if serial_number_max > 0:
            # 要新增的 識別碼 的序號
            serial_number = 0
            # 查詢目前所有的序號，從小到大檢視是否有 跳號
            query_string = u'SELECT substring(finish_id, 20, 3) FROM pipe WHERE finish_id LIKE \'{}\' ORDER BY substring(finish_id, 20, 3) ASC'.format(finish_id)
            #print '2' + query_string
            query = db_conn.exec_(query_string)
            
            if query.isActive():
                # 如果最大的序號 小於、等於 筆數資料，則要新增的序號 等於 現有最大序號加 1
                if serial_number_max <= query.size():
                    serial_number = serial_number_max + 1
                # 如果最大的序號 大於 筆數資料，代表中間存在 跳號
                else:
                    # 暫存 序號
                    i = 1
                    # 連續式 設定新增的序號 等於 現有最大序號加 1
                    serial_number = serial_number_max + 1
                    while query.next():
                        # 欄位的序號 - 暫存續號 大於 0，將 記錄跳號 設為 i
                        if (int(query.value(0)) - i) > 0:
                            serial_number_jump = i
                            break
                        i += 1
        # 代表 serial_number_max == 0，新增為該 索引圖框 第一筆資料
        else:
            serial_number = 1

        self.serial_number = unicode(serial_number)
        self.serial_number_jump = unicode(serial_number_jump)

        query.clear()
        db_conn.close()

    # 對話框關閉
    def gml_cancel(self):
        self.gml_open_file_dlg.close()
    

    # 開啟與 資料庫 的連線
    def get_db_connection(self):
    # 取得現有 QGIS 圖層之資料來源
    #layer = self.iface.activeLayer()
        layer = self.iface.mapCanvas().layer(0)
        provider = layer.dataProvider()
    # 若目前有圖層開啟的狀態，則取得圖層的連接資訊
        if provider.name() == 'postgres':
    # get the URI containing the connection parameters
            uri = QgsDataSourceURI(provider.dataSourceUri())
            pg_conn = QSqlDatabase.addDatabase('QPSQL')
            if pg_conn.isValid():
                pg_conn.setHostName(uri.host())
                pg_conn.setDatabaseName(uri.database())
                pg_conn.setPort(int(uri.port()))
                pg_conn.setUserName(uri.username())
                pg_conn.setPassword(uri.password())

        if not pg_conn.open():
            err = pg_conn.lastError()
            print err.driverText()
        else:
            return pg_conn