from qgis.gui import QgsMapCanvas, QgsMapCanvasLayer, QgsMapTool
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qgis.PyQt import QtGui, QtCore

class MplWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)

    def set_data(self, dataframe):
        self.dataframe = dataframe 

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        self.axes.cla()
        self.dataframe.plot(kind='hist', ax=self.axes)
        self.draw()

class MapWidget(QgsMapCanvas):
    def __init__(self, parent=None, vlayer=None):
        QgsMapCanvas.__init__(self)
        self.setCanvasColor(QtCore.Qt.black)
        self.enableAntiAliasing(True)
        # set extent to the extent of our layer
        self.setExtent(vlayer.extent())
        # set the map canvas layer set
        self.setLayerSet([QgsMapCanvasLayer(vlayer)])
        self.show()

class FilesWidget(QtGui.QTreeView):
    def __init__(self, parent=None, path='.'):
        self.path = path
        QtGui.QTreeWidget.__init__(self, parent)
        self.model = QtGui.QDirModel(self)
        self.model.setReadOnly(True)
        self.model.setSorting(QtCore.QDir.DirsFirst | QtCore.QDir.IgnoreCase | QtCore.QDir.Name);
        self.model.setFilter(QtCore.QDir.Files | QtCore.QDir.NoSymLinks)
        self.model.setNameFilters(['*.gpx'])

        self.setModel(self.model)
        self.header().setSortIndicator(0, QtCore.Qt.AscendingOrder)
        self.header().setSortIndicatorShown(True)
        self.header().setStretchLastSection(True)
        self.header().setClickable(True)

        # index = self.model.index(QtCore.QDir.currentPath())
        index = self.model.index(path)

        self.expand(index);
        self.scrollTo(index)
        self.setCurrentIndex(index)
        self.resizeColumnToContents(0)
        self.show()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = FilesWidget()    
    sys.exit(app.exec_())


