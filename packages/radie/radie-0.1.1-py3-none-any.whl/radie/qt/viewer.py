import sys

from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg

from ..structures import DataStructure
from ..import loaders
from . import cfg, visualizations, dpi, masterdftree
from . import functions as fn
from . import excel_exporter

class SubWindow(QtWidgets.QMdiSubWindow):
    pass


class VisualizationWindow(SubWindow):
    def __init__(self, visualization: visualizations.base.Visualization=None, parent=None):
        super(VisualizationWindow, self).__init__(parent)

        if visualization:
            self.setWidget(visualization)

    def setWidget(self, visualization: visualizations.base.Visualization):
        if not isinstance(visualization, visualizations.base.Visualization):
            raise TypeError("Visualization Windows can only have Visualization Widgets as their main widget")
        self.resize(visualization.size())
        super(VisualizationWindow, self).setWidget(visualization)
        self.setWindowIcon(visualization.icon())


class SubWindowListItem(QtWidgets.QListWidgetItem):
    def __init__(self, subwindow: SubWindow, name: str=None, parent=None):
        super(SubWindowListItem, self).__init__(parent)
        self.subWindow = subwindow  # type: QtWidgets.QMdiSubWindow
        self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)
        if not name:
            self.setText("sub window")
        else:
            self.setText(name)
        self.setIcon(self.subWindow.widget().icon())

    def showVisualization(self):
        if self.subWindow.isHidden():
            self.subWindow.show()
            self.subWindow.widget().show()

        if self.subWindow.isMinimized():
            self.subWindow.setWindowState(QtCore.Qt.WindowNoState)

        self.subWindow.mdiArea().setActiveSubWindow(self.subWindow)

    def setText(self, atext: str):
        super(SubWindowListItem, self).setText(atext)
        self.subWindow.setWindowTitle(atext)


class SubWindowList(QtWidgets.QListWidget):
    def __init__(self, *args, **kwargs):
        super(SubWindowList, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked | QtWidgets.QAbstractItemView.EditKeyPressed)
        self.itemDoubleClicked.connect(self.processDoubleClick)
        self.itemDelegate().commitData.connect(self.itemTextUpdated)

    def itemTextUpdated(self):
        item = self.currentItem()  # type: SubWindowListItem
        item.subWindow.setWindowTitle(item.text())

    def processDoubleClick(self, item: SubWindowListItem):
        item.showVisualization()


class NewVisAction(QtWidgets.QAction):
    newVisualizationRequested = QtCore.pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(NewVisAction, self).__init__(*args, **kwargs)
        self.vis_class = None  # class: visualizations.base.Visualization
        self.triggered.connect(self.requestNewVisualization)

    def requestNewVisualization(self, checked: bool):
        self.newVisualizationRequested.emit(self.vis_class)


class VisualizationsList(SubWindowList):
    def __init__(self, parent=None):
        super(VisualizationsList, self).__init__(parent)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Radie")
        self.setWindowIcon(QtGui.QIcon(cfg.radie_icon))

        self.resize(*dpi.width_by_height(1024, 600))
        self.centralwidget = QtWidgets.QWidget(self)
        self.verticalLayout_centralWidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_centralWidget.setContentsMargins(0, 0, 0, 0)
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.verticalLayout_centralWidget.addWidget(self.mdiArea)
        self.setCentralWidget(self.centralwidget)

        self.dock_dataFrames = QtWidgets.QDockWidget(self)
        self.dock_dataFrames.setWindowTitle("DataFrames")
        self.treeView_dataFrames = masterdftree.DFTreeView()
        self.dock_dataFrames.setWidget(self.treeView_dataFrames)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_dataFrames)

        self.dock_visualizations = QtWidgets.QDockWidget(self)
        self.dock_visualizations.setWindowTitle("Visualizations")
        self.visList = VisualizationsList()
        self.dock_visualizations.setWidget(self.visList)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_visualizations)
        self.setAcceptDrops(True)

        # --- MainWindow Menu Bar Setup ---#
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))

        self.menuFile = QtWidgets.QMenu("&File", self.menubar)
        self.actionExit = QtWidgets.QAction("&Exit", self)
        self.actionExit.triggered.connect(self.close)
        self.menuFile.addAction(self.actionExit)
        self.actionSave = QtWidgets.QAction("&Save", self)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.action_importFromClipboard = QtWidgets.QAction("Import from &Clipboard", self)
        self.action_importFromClipboard.triggered.connect(self.importDataFrameFromClipboard)
        self.menuFile.addAction(self.action_importFromClipboard)
        self.menubar.addAction(self.menuFile.menuAction())

        self.menuEdit = QtWidgets.QMenu("&Edit", self.menubar)
        self.actionCopy = QtWidgets.QAction("&Copy", self)
        self.menuEdit.addAction(self.actionCopy)
        self.actionPaste = QtWidgets.QAction("&Paste", self)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.menuView = QtWidgets.QMenu("&View", self.menubar)
        self.actionData_Sets = QtWidgets.QAction("&Data Sets", self)
        self.actionData_Sets.triggered.connect(self.dock_dataFrames.show)
        self.menuView.addAction(self.actionData_Sets)
        self.actionVisualizations = QtWidgets.QAction("&Visualizations", self)
        self.actionVisualizations.triggered.connect(self.dock_visualizations.show)
        self.menuView.addAction(self.actionVisualizations)
        self.menubar.addAction(self.menuView.menuAction())

        self.menuVisualizations = QtWidgets.QMenu("V&isualizations", self.menubar)
        self.menubar.addAction(self.menuVisualizations.menuAction())

        self.menuHelp = QtWidgets.QMenu("&Help", self.menubar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.actionSave.setIcon(fn.icon("saveicon.svg"))
        self.actionCopy.setIcon(fn.icon("copyicon.svg"))
        self.actionPaste.setIcon(fn.icon("pasteicon.svg"))
        self.actionExit.setIcon(fn.icon("exiticon.svg"))
        # --- End MainWindow Menu Bar Setup --- #

        ## initialize visualization menu items
        self.vis_actions = []
        for cls in visualizations.visualizations.values():  # type : visualizations.base.Visualization
            action = NewVisAction("add &" + cls.name, self)
            action.vis_class = cls
            action.setIcon(cls.icon())
            action.newVisualizationRequested.connect(self.addNewVisualization)
            self.vis_actions.append(action)
            self.menuVisualizations.addAction(action)

        self.menubar.addAction(self.menuVisualizations.menuAction())
        ## end menus

        self.actionSave.setEnabled(False)

    def closeEvent(self, event):
        quit_msg = ""

        quit_msg += "Are you sure you want to exit the program?"
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent):
        if a0.mimeData().hasUrls:
            a0.acceptProposedAction()
        else:
            super(MainWindow, self).dragEnterEvent(a0)

    def dropEvent(self, a0: QtGui.QDropEvent):
        mime = a0.mimeData()
        urls = mime.urls()
        err_msg = ""
        for url in urls:  # type: QtCore.QUrl
            fname = url.toLocalFile()
            try:
                dfs = loaders.load_file(fname)
            except Exception as inst:
                err_msg += "\nError: {:}.\ncould not load file: {:}".format(str(inst), fname)
                continue

            if isinstance(dfs, DataStructure):
                dfs = [dfs]
            for df in dfs:  # type: DataStructure
                try:
                    self.treeView_dataFrames.addDataFrame(df)
                except Exception as e:
                    err_msg += "\nError: {:}.\nSomething wrong could not load {:} as a DataStructure Object".format(str(e), df)
                    continue

        if err_msg.strip():
            fn.error_popup(err_msg)
        return

    def addNewVisualization(self, visualization: visualizations.base.Visualization):
        subwindow = VisualizationWindow(visualization())
        item = SubWindowListItem(subwindow, name=visualization.name)
        self.visList.addItem(item)
        self.mdiArea.addSubWindow(item.subWindow)
        item.showVisualization()

    def importDataFrameFromClipboard(self):
        df = DataStructure.from_clipboard()
        df.metadata["name"] = "DF - clipboard"
        self.treeView_dataFrames.addDataFrame(df)


def run(debug=False):
    fn.set_process_id("radie")
    # fn.setup_style()
    app = fn.instantiate_app(sys.argv)

    fn.set_popup_exceptions()
    cfg.set_dpi_scaling()
    main_window = MainWindow()
    main_window.show()

    if debug:
        from radie.plugins import examples
        main_window.treeView_dataFrames.addDataFrame(examples.example_powderdiffraction())
        main_window.treeView_dataFrames.addDataFrame(examples.example_vsm())

    # sys.exit(app.exec_())
    # use pyqtgraph.exit to avoid crashes on exit
    # https://stackoverflow.com/questions/27131294/error-qobjectstarttimer-qtimer-can-only-be-used-with-threads-started-with-qt
    app.exec_()
    pg.exit()


def debug():
    run(True)


if __name__ == "__main__":
    run(debug=False)
