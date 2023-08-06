#/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

from qgis.core import (QgsApplication, QgsVectorLayer, QgsMapLayerRegistry,
                        QgsDataSourceURI, QgsGeometry, QgsPointV2, QgsLineStringV2)
from qgis.gui import (QgsMapCanvas, QgsMapCanvasLayer, QgsRubberBand,
                        QgsMapToolPan, QgsMapToolZoom, QgsVertexMarker)
# from qgis.core import *
# from qgis.gui import *
from qgis.PyQt import QtCore, QtGui
from MyWidgets import MapWidget, MplWidget, FilesWidget
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',)
                    # filename='myapp.log',
                    # filemode='w')

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.add_map_data()
        self.init_ui()

    def add_map_data(self):
        # add PostGIS layer
        self.uri = QgsDataSourceURI()
        # set host name, port, database name, username and password
        dbname = "shenzhen_osm"
        self.uri.setConnection("10.10.5.126", "5432", dbname, "postgres", "password")
        # set database schema, table name, geometry column and optionally subset (WHERE clause)
        self.uri.setDataSource("public", "shenzhen_kailide", "geom", "")
        self.vlayer = QgsVectorLayer(self.uri.uri(), "links", "postgres")

        # self.vlayer = QgsVectorLayer("./data/file.shp", "vlayer", "ogr")
        if self.vlayer.isValid():
            self.statusBar().showMessage("Datasource connected")
            # logging.info('Connected to ' + dbname)
            QgsMapLayerRegistry.instance().addMapLayer(self.vlayer)
            logging.info('Map layer registered')
        else:
            logging.error('Database connection failed, please check your data connection')
            self.statusBar().showMessage("Please check your data connection")

    def init_ui(self):
        # set road layer style
        rendererV2 = self.vlayer.rendererV2()
        sym = rendererV2.symbol()
        sym.setColor(QtGui.QColor('#BEBEBE'))
        sym.setWidth(0.1)

        # widgets
        self.mapWidget = MapWidget(self, self.vlayer)
        self.mplWidget = MplWidget(self)
        self.filesWidget = FilesWidget(self, path='./tracks')

        self.pathLabel = QtGui.QLabel("path result (link IDs)", self)
        self.pathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pathLineEdit = QtGui.QLineEdit(self)

        # plot line width distribution
        self.dataframe = pd.DataFrame([feat.geometry().length() for feat in self.vlayer.getFeatures()])
        self.mplWidget.set_data(self.dataframe)

        # statusbar
        self.statusBar().showMessage("ready")

        # toolbar and actions
        self.toolbar = self.addToolBar('Toolbar')
        actPlot = QtGui.QAction('&Plot', self)
        actFullExtent = QtGui.QAction('Full &Extent', self)
        actShowTracks = QtGui.QAction('Show &Tracks', self)
        actZoomIn = QtGui.QAction('Zoom &In', self)
        actZoomOut = QtGui.QAction('Zoom &Out', self)
        actPan = QtGui.QAction('&Pan', self)

        # action shortcuts
        actPlot.setShortcut('Ctrl+P')
        actFullExtent.setShortcut('Ctrl+E')
        actShowTracks.setShortcut('Ctrl+T')
        actZoomIn.setShortcut('Ctrl+]')
        actZoomOut.setShortcut('Ctrl+[')
        actPan.setShortcut('Ctrl+M')

        # action icons
        actPlot.setIcon(QtGui.QIcon(QtGui.QPixmap("./icons/plot.png")))
        actFullExtent.setIcon(QtGui.QIcon(QtGui.QPixmap("./icons/extent.png")))
        actShowTracks.setIcon(QtGui.QIcon(QtGui.QPixmap("./icons/tracks.png")))
        actZoomIn.setIcon(QtGui.QIcon(QtGui.QPixmap("./icons/zoomin.png")))
        actZoomOut.setIcon(QtGui.QIcon(QtGui.QPixmap("./icons/zoomout.png")))
        actPan.setIcon(QtGui.QIcon(QtGui.QPixmap("./icons/pan.png")))

        # map tools
        self.toolZoomIn = QgsMapToolZoom(self.mapWidget, False)
        self.toolZoomOut = QgsMapToolZoom(self.mapWidget, True)
        self.toolPan = QgsMapToolPan(self.mapWidget)

        # action handlers
        actPlot.triggered.connect(self.mplWidget.update_figure)
        actFullExtent.triggered.connect(self.mapWidget.zoomToFullExtent)
        actZoomIn.triggered.connect(lambda s: self.mapWidget.setMapTool(self.toolZoomIn))
        actZoomOut.triggered.connect(lambda s: self.mapWidget.setMapTool(self.toolZoomOut))
        actPan.triggered.connect(lambda s: self.mapWidget.setMapTool(self.toolPan))
        actShowTracks.triggered.connect(lambda s: [i.hide() if i.isVisible() else i.setVisible(True) for i in [self.marker_o, self.r]])
        self.pathLineEdit.textChanged.connect(self.show_links_path)

        self.mapWidget.xyCoordinates.connect( 
                lambda s: self.statusBar().showMessage(
                    str.format("{0}, {1}",s.x(), s.y())))
        self.filesWidget.selectionModel().selectionChanged.connect(
        lambda s: self.show_gpx_path(self.filesWidget.model.filePath(self.filesWidget.selectedIndexes()[0])))
        self.r = QgsRubberBand(self.mapWidget, False)  # False = not a polygon
        self.r.setColor(QtGui.QColor(255,0,0,120))
        self.r.setWidth(3)
         
        self.marker_o = QgsVertexMarker(self.mapWidget)

        self.toolbar.addAction(actFullExtent)
        self.toolbar.addAction(actZoomIn)
        self.toolbar.addAction(actZoomOut)
        self.toolbar.addAction(actPan)
        self.toolbar.addSeparator()
        self.toolbar.addAction(actPlot)
        self.toolbar.addAction(actShowTracks)
        self.toolbar.setMovable(True)

        # dock widgets
        self.mapdock = QtGui.QDockWidget("map")
        self.mapdock.setWidget(self.mapWidget)
        self.mapdock.setAllowedAreas(QtCore.Qt.RightDockWidgetArea | QtCore.Qt.LeftDockWidgetArea)
        self.mapdock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)

        # horizontal 1
        self.hsplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.vsplitter_left = QtGui.QSplitter(QtCore.Qt.Vertical)

        self.hs = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.hs.addWidget(self.pathLabel)
        self.hs.addWidget(self.pathLineEdit)
        self.vsplitter_left.addWidget(self.hs)
        self.vsplitter_left.addWidget(self.mapdock)
        self.hsplitter.addWidget(self.vsplitter_left)
        self.vsplitter_right = QtGui.QSplitter(QtCore.Qt.Vertical)

        # horizontal 2, vertical 1
        self.filesdock = QtGui.QDockWidget("files")
        self.filesdock.setWidget(self.filesWidget)
        self.filesdock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.vsplitter_right.addWidget(self.filesdock)

        # horizontal 2 vertical 2
        self.mpldock = QtGui.QDockWidget("mpl")
        self.mpldock.setWidget(self.mplWidget)
        self.mpldock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.vsplitter_right.addWidget(self.mpldock)


        self.hsplitter.addWidget(self.vsplitter_right)
        self.setCentralWidget(self.hsplitter)
        self.show()

    def show_gpx_path(self, path):
        logging.info('show gpx path ' + path)
        self.statusBar().showMessage(path)
        if not path.endswith('gpx'):
            self.statusBar().showMessage("Not a GPX file")
            return
        uri = path + "?type=track"
        gpx_layer = QgsVectorLayer(uri, "track", "gpx")
        geom = [feat.geometry() for feat in gpx_layer.getFeatures()][0]
        o_pt,d_pt = geom.asPolyline()[0], geom.asPolyline()[-1]
        self.marker_o.setColor(QtGui.QColor(255, 0, 0))
        self.marker_o.setCenter(o_pt)
        self.marker_o.setIconSize(8)
        self.marker_o.setIconType(QgsVertexMarker.ICON_CIRCLE) # or ICON_CROSS, ICON_X
        self.marker_o.setPenWidth(2)
        self.marker_o.show()
        self.r.setToGeometry(geom, None)
        self.mapWidget.zoomToFeatureExtent(geom.boundingBox())

    def show_links_path(self):
        logging.info('show links path')
        self.statusBar().showMessage('links path')
        links = ','.join(self.pathLineEdit.text().split(','))

        # OK to render but show wrong point sequence
        # line = QgsLineStringV2()
        # feats = [feat for feat in self.vlayer.getFeatures() if feat['osm_id'] in links]
        # for feat in feats:
            # pts = feat.geometry().asPolyline() 
            # for pt in pts:
                # line.addVertex(QgsPointV2(pt))
        # geom = QgsGeometry(line)
        # self.r.setToGeometry(geom, None)
        # self.mapWidget.zoomToFeatureExtent(geom.boundingBox())

        # set condition in another way
        self.uri.setDataSource("public", "shenzhen_kailide", "geom", "osm_id in ({0})".format(links))
        self.vlayer2 = QgsVectorLayer(self.uri.uri(), "links_path", "postgres")
        # set renderer for vlayer2
        renderer = self.vlayer2.rendererV2()
        sym = renderer.symbol()
        sym.setColor(QtGui.QColor(0,0,255,120))
        sym.setWidth(2)
        num_of_features = len([i for i in self.vlayer2.getFeatures()])
        if self.vlayer2.isValid() and num_of_features!=0:
            self.mapWidget.clear()
            logging.info('Map layer cleared')
            QgsMapLayerRegistry.instance().addMapLayer(self.vlayer2)
            self.mapWidget.setLayerSet([QgsMapCanvasLayer(self.vlayer2), QgsMapCanvasLayer(self.vlayer)])
            self.mapWidget.setExtent(self.vlayer2.extent())
            logging.info('Map layer registered')
        else:
            logging.error('Database connection failed or query result is empty')

if __name__ == '__main__':
    app = QgsApplication([], True)
    QgsApplication.setPrefixPath('/Applications/QGIS.app/Contents/MacOS', True)
    # use the below under linux
    # QgsApplication.setPrefixPath('/usr', True)
    QgsApplication.initQgis()

    win = MainWindow() 
    win.show()
    retval = app.exec_()
    QgsApplication.exitQgis()
    sys.exit(retval)
