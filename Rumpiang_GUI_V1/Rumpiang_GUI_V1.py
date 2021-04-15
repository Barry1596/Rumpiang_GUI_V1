import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Rumpiang_GUI_Plot import Live_Plot_ATRH, Live_Plot_LinearDisplacement, Live_Plot_StrainGauge, Live_Plot_TemperaturMaterial
from Rumpiang_GUI_Plot import Live_Battery_Plot_ATRH, Live_Battery_Plot_LinearDisplacement, Live_Battery_Plot_StrainGauge, Live_Battery_Plot_TemperaturMaterial 
from Rumpiang_GUI_Plot import Static_Plot_ATRH, Static_Plot_LinearDisplacement, Static_Plot_StrainGauge, Static_Plot_TemperaturMaterial



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
   def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1533, 974)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RumpiangGUI = QtWidgets.QTabWidget(self.centralwidget)
        self.RumpiangGUI.setGeometry(QtCore.QRect(0, 0, 1521, 931))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RumpiangGUI.setFont(font)
        self.RumpiangGUI.setElideMode(QtCore.Qt.ElideNone)
        self.RumpiangGUI.setDocumentMode(False)
        self.RumpiangGUI.setMovable(False)
        self.RumpiangGUI.setObjectName("RumpiangGUI")
        #============================================================Live Tab============================
        self.Live = QtWidgets.QWidget()
        self.Live.setObjectName("Live")
        self.V_Line_3 = QtWidgets.QFrame(self.Live)
        self.V_Line_3.setGeometry(QtCore.QRect(180, 10, 16, 681))
        self.V_Line_3.setAutoFillBackground(False)
        self.V_Line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_Line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_Line_3.setObjectName("V_Line_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Live)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 1, 181, 671))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ATRH_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.ATRH_Label.setObjectName("ATRH_Label")
        self.verticalLayout_2.addWidget(self.ATRH_Label)
        self.ATRH_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.ATRH_Combo_Live.setObjectName("ATRH_Combo_Live")
        self.ATRH_Combo_Live.addItem("")
        self.ATRH_Combo_Live.addItem("")
        self.ATRH_Combo_Live.addItem("")
        self.ATRH_Combo_Live.addItem("")
        self.ATRH_Combo_Live.addItem("")
        self.ATRH_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.ATRH_Combo_Live)
        self.Anemometer_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Anemometer_Label.setObjectName("Anemometer_Label")
        self.verticalLayout_2.addWidget(self.Anemometer_Label)
        self.Anemometer_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Anemometer_Combo_Live.setObjectName("Anemometer_Combo_Live")
        self.Anemometer_Combo_Live.addItem("")
        self.Anemometer_Combo_Live.addItem("")
        self.Anemometer_Combo_Live.addItem("")
        self.Anemometer_Combo_Live.addItem("")
        self.Anemometer_Combo_Live.addItem("")
        self.Anemometer_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.Anemometer_Combo_Live)
        self.Displacement_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Displacement_Label.setObjectName("Displacement_Label")
        self.verticalLayout_2.addWidget(self.Displacement_Label)
        self.Displacement_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Displacement_Combo_Live.setObjectName("Displacement_Combo_Live")
        self.Displacement_Combo_Live.addItem("")
        self.Displacement_Combo_Live.addItem("")
        self.Displacement_Combo_Live.addItem("")
        self.Displacement_Combo_Live.addItem("")
        self.Displacement_Combo_Live.addItem("")
        self.Displacement_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.Displacement_Combo_Live)
        self.H_Inclino_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.H_Inclino_Label.setWordWrap(True)
        self.H_Inclino_Label.setObjectName("H_Inclino_Label")
        self.verticalLayout_2.addWidget(self.H_Inclino_Label)
        self.H_Inclino_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.H_Inclino_Combo_Live.setObjectName("H_Inclino_Combo_Live")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.H_Inclino_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.H_Inclino_Combo_Live)
        self.V_Inclino_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.V_Inclino_Label.setWordWrap(True)
        self.V_Inclino_Label.setObjectName("V_Inclino_Label")
        self.verticalLayout_2.addWidget(self.V_Inclino_Label)
        self.V_Inclino_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.V_Inclino_Combo_Live.setObjectName("V_Inclino_Combo_Live")
        self.V_Inclino_Combo_Live.addItem("")
        self.V_Inclino_Combo_Live.addItem("")
        self.V_Inclino_Combo_Live.addItem("")
        self.V_Inclino_Combo_Live.addItem("")
        self.V_Inclino_Combo_Live.addItem("")
        self.V_Inclino_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.V_Inclino_Combo_Live)
        self.FSG_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.FSG_Label.setWordWrap(True)
        self.FSG_Label.setObjectName("FSG_Label")
        self.verticalLayout_2.addWidget(self.FSG_Label)
        self.FSG_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.FSG_Combo_Live.setObjectName("FSG_Combo_Live")
        self.FSG_Combo_Live.addItem("")
        self.FSG_Combo_Live.addItem("")
        self.FSG_Combo_Live.addItem("")
        self.FSG_Combo_Live.addItem("")
        self.FSG_Combo_Live.addItem("")
        self.FSG_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.FSG_Combo_Live)
        self.HSG_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.HSG_Label.setWordWrap(True)
        self.HSG_Label.setObjectName("HSG_Label")
        self.verticalLayout_2.addWidget(self.HSG_Label)
        self.HSG_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.HSG_Combo_Live.setObjectName("HSG_Combo_Live")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.HSG_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.HSG_Combo_Live)
        self.Seismometer_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Seismometer_Label.setObjectName("Seismometer_Label")
        self.verticalLayout_2.addWidget(self.Seismometer_Label)
        self.Seismometer_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Seismometer_Combo_Live.setObjectName("Seismometer_Combo_Live")
        self.Seismometer_Combo_Live.addItem("")
        self.Seismometer_Combo_Live.addItem("")
        self.Seismometer_Combo_Live.addItem("")
        self.Seismometer_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.Seismometer_Combo_Live)
        self.Thermistor_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Thermistor_Label.setObjectName("Thermistor_Label")
        self.verticalLayout_2.addWidget(self.Thermistor_Label)
        self.Thermistor_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Thermistor_Combo_Live.setObjectName("Thermistor_Combo_Live")
        self.Thermistor_Combo_Live.addItem("")
        self.Thermistor_Combo_Live.addItem("")
        self.Thermistor_Combo_Live.addItem("")
        self.Thermistor_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.Thermistor_Combo_Live)
        self.Acc_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Acc_Label.setObjectName("Acc_Label")
        self.verticalLayout_2.addWidget(self.Acc_Label)
        self.Acc_Combo_Live = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Acc_Combo_Live.setObjectName("Acc_Combo_Live")
        self.Acc_Combo_Live.addItem("")
        self.Acc_Combo_Live.addItem("")
        self.Acc_Combo_Live.addItem("")
        self.Acc_Combo_Live.addItem("")
        self.Acc_Combo_Live.addItem("")
        self.Acc_Combo_Live.addItem("")
        self.verticalLayout_2.addWidget(self.Acc_Combo_Live)
        self.H_Line_3 = QtWidgets.QFrame(self.Live)
        self.H_Line_3.setGeometry(QtCore.QRect(0, 680, 1491, 20))
        self.H_Line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_Line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_Line_3.setObjectName("H_Line_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Live)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(680, 720, 811, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MONITORINGIO = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.MONITORINGIO.setObjectName("MONITORINGIO")
        self.horizontalLayout.addWidget(self.MONITORINGIO)
        self.KONTAK = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.KONTAK.setObjectName("KONTAK")
        self.horizontalLayout.addWidget(self.KONTAK)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Live)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(680, 750, 811, 131))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DESK_MONITORINGIO = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.DESK_MONITORINGIO.setWordWrap(True)
        self.DESK_MONITORINGIO.setObjectName("DESK_MONITORINGIO")
        self.horizontalLayout_4.addWidget(self.DESK_MONITORINGIO)
        self.DES_KONTAK = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_4)
        self.DES_KONTAK.setObjectName("DES_KONTAK")
        self.horizontalLayout_4.addWidget(self.DES_KONTAK)
        self.Logo = QtWidgets.QLabel(self.Live)
        self.Logo.setGeometry(QtCore.QRect(40, 750, 611, 111))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../GundalaGUI_V0/Logo Gundala1.png"))
        self.Logo.setWordWrap(False)
        self.Logo.setObjectName("Logo")

        self.Live_Plot_Widget = QtWidgets.QWidget(self.Live)
        self.Live_Plot_Widget.setGeometry(QtCore.QRect(190, 0, 1331, 691))
        self.Live_Plot_Widget.setObjectName("Live_Plot_Widget")
        self.Live_Plot_Layout = QtWidgets.QGridLayout(self.Live_Plot_Widget)
        self.Live_Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.Live_Plot_Layout.setObjectName("Live_Plot_Layout")
        self.Live_Plot_Layout.addWidget(self.Live_Plot_Widget, 1,1,1,1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.Live)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.Setting = QtWidgets.QLabel(self.Live)
        self.Setting.setGeometry(QtCore.QRect(0, 690, 81, 22))
        self.Setting.setObjectName("Setting")
        self.ListTimeRange = QtWidgets.QComboBox(self.Live)
        self.ListTimeRange.setGeometry(QtCore.QRect(0, 720, 179, 30))
        self.ListTimeRange.setEditable(False)
        self.ListTimeRange.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.ListTimeRange.setMinimumContentsLength(0)
        self.ListTimeRange.setModelColumn(0)
        self.ListTimeRange.setObjectName("ListTimeRange")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.ListTimeRange.addItem("")
        self.Live_Plot_Layout.addWidget(self.gridLayoutWidget, 0, 0, 1, 2)
        self.RumpiangGUI.addTab(self.Live, "")

        #===============================History Tab==========================
        self.Historical = QtWidgets.QWidget()
        self.Historical.setObjectName("Historical")
        self.V_Line_2 = QtWidgets.QFrame(self.Historical)
        self.V_Line_2.setGeometry(QtCore.QRect(180, 0, 20, 681))
        self.V_Line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_Line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_Line_2.setObjectName("V_Line_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Historical)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 0, 181, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ATRH_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ATRH_Label_2.setObjectName("ATRH_Label_2")
        self.verticalLayout.addWidget(self.ATRH_Label_2)
        self.ATRH_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ATRH_Combo_History.setObjectName("ATRH_Combo_History")
        self.ATRH_Combo_History.addItem("")
        self.ATRH_Combo_History.addItem("")
        self.ATRH_Combo_History.addItem("")
        self.ATRH_Combo_History.addItem("")
        self.ATRH_Combo_History.addItem("")
        self.ATRH_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.ATRH_Combo_History)
        self.Anemometer_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Anemometer_Label_2.setObjectName("Anemometer_Label_2")
        self.verticalLayout.addWidget(self.Anemometer_Label_2)
        self.Anemometer_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Anemometer_Combo_History.setObjectName("Anemometer_Combo_History")
        self.Anemometer_Combo_History.addItem("")
        self.Anemometer_Combo_History.addItem("")
        self.Anemometer_Combo_History.addItem("")
        self.Anemometer_Combo_History.addItem("")
        self.Anemometer_Combo_History.addItem("")
        self.Anemometer_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.Anemometer_Combo_History)
        self.Displacement_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Displacement_Label_2.setObjectName("Displacement_Label_2")
        self.verticalLayout.addWidget(self.Displacement_Label_2)
        self.Displacement_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Displacement_Combo_History.setObjectName("Displacement_Combo_History")
        self.Displacement_Combo_History.addItem("")
        self.Displacement_Combo_History.addItem("")
        self.Displacement_Combo_History.addItem("")
        self.Displacement_Combo_History.addItem("")
        self.Displacement_Combo_History.addItem("")
        self.Displacement_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.Displacement_Combo_History)
        self.H_Inclino_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.H_Inclino_Label_2.setWordWrap(True)
        self.H_Inclino_Label_2.setObjectName("H_Inclino_Label_2")
        self.verticalLayout.addWidget(self.H_Inclino_Label_2)
        self.H_Inclino_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.H_Inclino_Combo_History.setObjectName("H_Inclino_Combo_History")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.H_Inclino_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.H_Inclino_Combo_History)
        self.V_Inclino_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.V_Inclino_Label_2.setWordWrap(True)
        self.V_Inclino_Label_2.setObjectName("V_Inclino_Label_2")
        self.verticalLayout.addWidget(self.V_Inclino_Label_2)
        self.V_Inclino_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.V_Inclino_Combo_History.setObjectName("V_Inclino_Combo_History")
        self.V_Inclino_Combo_History.addItem("")
        self.V_Inclino_Combo_History.addItem("")
        self.V_Inclino_Combo_History.addItem("")
        self.V_Inclino_Combo_History.addItem("")
        self.V_Inclino_Combo_History.addItem("")
        self.V_Inclino_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.V_Inclino_Combo_History)
        self.FSG_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.FSG_Label_2.setWordWrap(True)
        self.FSG_Label_2.setObjectName("FSG_Label_2")
        self.verticalLayout.addWidget(self.FSG_Label_2)
        self.FSG_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.FSG_Combo_History.setObjectName("FSG_Combo_History")
        self.FSG_Combo_History.addItem("")
        self.FSG_Combo_History.addItem("")
        self.FSG_Combo_History.addItem("")
        self.FSG_Combo_History.addItem("")
        self.FSG_Combo_History.addItem("")
        self.FSG_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.FSG_Combo_History)
        self.HSG_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.HSG_Label_2.setWordWrap(True)
        self.HSG_Label_2.setObjectName("HSG_Label_2")
        self.verticalLayout.addWidget(self.HSG_Label_2)
        self.HSG_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.HSG_Combo_History.setObjectName("HSG_Combo_History")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.HSG_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.HSG_Combo_History)
        self.Seismometer_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Seismometer_Label_2.setObjectName("Seismometer_Label_2")
        self.verticalLayout.addWidget(self.Seismometer_Label_2)
        self.Seismometer_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Seismometer_Combo_History.setObjectName("Seismometer_Combo_History")
        self.Seismometer_Combo_History.addItem("")
        self.Seismometer_Combo_History.addItem("")
        self.Seismometer_Combo_History.addItem("")
        self.Seismometer_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.Seismometer_Combo_History)
        self.Thermistor_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Thermistor_Label_2.setObjectName("Thermistor_Label_2")
        self.verticalLayout.addWidget(self.Thermistor_Label_2)
        self.Thermistor_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Thermistor_Combo_History.setObjectName("Thermistor_Combo_History")
        self.Thermistor_Combo_History.addItem("")
        self.Thermistor_Combo_History.addItem("")
        self.Thermistor_Combo_History.addItem("")
        self.Thermistor_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.Thermistor_Combo_History)
        self.Acc_Label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Acc_Label_2.setObjectName("Acc_Label_2")
        self.verticalLayout.addWidget(self.Acc_Label_2)
        self.Acc_Combo_History = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Acc_Combo_History.setObjectName("Acc_Combo_History")
        self.Acc_Combo_History.addItem("")
        self.Acc_Combo_History.addItem("")
        self.Acc_Combo_History.addItem("")
        self.Acc_Combo_History.addItem("")
        self.Acc_Combo_History.addItem("")
        self.Acc_Combo_History.addItem("")
        self.verticalLayout.addWidget(self.Acc_Combo_History)
        self.H_Line_2 = QtWidgets.QFrame(self.Historical)
        self.H_Line_2.setGeometry(QtCore.QRect(0, 670, 1481, 16))
        self.H_Line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_Line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_Line_2.setObjectName("H_Line_2")
        self.Logo_2 = QtWidgets.QLabel(self.Historical)
        self.Logo_2.setGeometry(QtCore.QRect(40, 730, 571, 131))
        self.Logo_2.setText("")
        self.Logo_2.setPixmap(QtGui.QPixmap("../GundalaGUI_V0/Logo Gundala1.png"))
        self.Logo_2.setWordWrap(False)
        self.Logo_2.setObjectName("Logo_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.Historical)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(680, 740, 811, 131))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DESK_MONITORINGIO_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.DESK_MONITORINGIO_2.setWordWrap(True)
        self.DESK_MONITORINGIO_2.setObjectName("DESK_MONITORINGIO_2")
        self.horizontalLayout_5.addWidget(self.DESK_MONITORINGIO_2)
        self.DES_KONTAK_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.DES_KONTAK_2.setObjectName("DES_KONTAK_2")
        self.horizontalLayout_5.addWidget(self.DES_KONTAK_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Historical)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(680, 700, 811, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MONITORINGIO_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.MONITORINGIO_2.setObjectName("MONITORINGIO_2")
        self.horizontalLayout_2.addWidget(self.MONITORINGIO_2)
        self.KONTAK_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.KONTAK_2.setObjectName("KONTAK_2")
        self.horizontalLayout_2.addWidget(self.KONTAK_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Historical)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(1360, 0, 160, 264))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Setting_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.Setting_2.setObjectName("Setting_2")
        self.verticalLayout_4.addWidget(self.Setting_2)
        self.BeginTime_String = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.BeginTime_String.setObjectName("BeginTime_String")
        self.verticalLayout_4.addWidget(self.BeginTime_String)
        self.Begin_Date = QtWidgets.QDateEdit(self.verticalLayoutWidget_4)
        self.Begin_Date.setObjectName("Begin_Date")
        self.verticalLayout_4.addWidget(self.Begin_Date)
        self.Begin_Time = QtWidgets.QTimeEdit(self.verticalLayoutWidget_4)
        self.Begin_Time.setObjectName("Begin_Time")
        self.verticalLayout_4.addWidget(self.Begin_Time)
        self.EndTime_String = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.EndTime_String.setObjectName("EndTime_String")
        self.verticalLayout_4.addWidget(self.EndTime_String)
        self.End_Date = QtWidgets.QDateEdit(self.verticalLayoutWidget_4)
        self.End_Date.setObjectName("End_Date")
        self.verticalLayout_4.addWidget(self.End_Date)
        self.End_Time = QtWidgets.QTimeEdit(self.verticalLayoutWidget_4)
        self.End_Time.setObjectName("End_Time")
        self.verticalLayout_4.addWidget(self.End_Time)
        self.SetTimeRange_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.SetTimeRange_2.setObjectName("SetTimeRange_2")
        self.verticalLayout_4.addWidget(self.SetTimeRange_2)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Historical)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(200, 0, 1161, 671))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.History_Plot_Widget = QtWidgets.QWidget(self.Historical)
        self.History_Plot_Widget.setGeometry(QtCore.QRect(200, 0, 1161, 671))
        self.History_Plot_Widget.setObjectName("History_Plot_Widget")
        self.History_Plot_Layout = QtWidgets.QGridLayout(self.History_Plot_Widget)
        self.History_Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.History_Plot_Layout.setObjectName("History_Plot_Layout")
        self.History_Plot_Layout.addWidget(self.History_Plot_Widget, 1,1,1,1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Historical)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.History_Plot_Layout.addWidget(self.gridLayoutWidget_3, 0, 0, 1, 1)
        self.RumpiangGUI.addTab(self.Historical, "")

        #===========================Battery Tab===============================
        self.Battery = QtWidgets.QWidget()
        self.Battery.setObjectName("Battery")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Battery)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1, 0, 181, 671))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ATRH_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.ATRH_Label_3.setObjectName("ATRH_Label_3")
        self.verticalLayout_3.addWidget(self.ATRH_Label_3)
        self.ATRH_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.ATRH_Combo_Battery.setObjectName("ATRH_Combo_Battery")
        self.ATRH_Combo_Battery.addItem("")
        self.ATRH_Combo_Battery.addItem("")
        self.ATRH_Combo_Battery.addItem("")
        self.ATRH_Combo_Battery.addItem("")
        self.ATRH_Combo_Battery.addItem("")
        self.ATRH_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.ATRH_Combo_Battery)
        self.Anemometer_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Anemometer_Label_3.setObjectName("Anemometer_Label_3")
        self.verticalLayout_3.addWidget(self.Anemometer_Label_3)
        self.Anemometer_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Anemometer_Combo_Battery.setObjectName("Anemometer_Combo_Battery")
        self.Anemometer_Combo_Battery.addItem("")
        self.Anemometer_Combo_Battery.addItem("")
        self.Anemometer_Combo_Battery.addItem("")
        self.Anemometer_Combo_Battery.addItem("")
        self.Anemometer_Combo_Battery.addItem("")
        self.Anemometer_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.Anemometer_Combo_Battery)
        self.Displacement_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Displacement_Label_3.setObjectName("Displacement_Label_3")
        self.verticalLayout_3.addWidget(self.Displacement_Label_3)
        self.Displacement_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Displacement_Combo_Battery.setObjectName("Displacement_Combo_Battery")
        self.Displacement_Combo_Battery.addItem("")
        self.Displacement_Combo_Battery.addItem("")
        self.Displacement_Combo_Battery.addItem("")
        self.Displacement_Combo_Battery.addItem("")
        self.Displacement_Combo_Battery.addItem("")
        self.Displacement_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.Displacement_Combo_Battery)
        self.H_Inclino_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.H_Inclino_Label_3.setWordWrap(True)
        self.H_Inclino_Label_3.setObjectName("H_Inclino_Label_3")
        self.verticalLayout_3.addWidget(self.H_Inclino_Label_3)
        self.H_Inclino_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.H_Inclino_Combo_Battery.setObjectName("H_Inclino_Combo_Battery")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.H_Inclino_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.H_Inclino_Combo_Battery)
        self.V_Inclino_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.V_Inclino_Label_3.setWordWrap(True)
        self.V_Inclino_Label_3.setObjectName("V_Inclino_Label_3")
        self.verticalLayout_3.addWidget(self.V_Inclino_Label_3)
        self.V_Inclino_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.V_Inclino_Combo_Battery.setObjectName("V_Inclino_Combo_Battery")
        self.V_Inclino_Combo_Battery.addItem("")
        self.V_Inclino_Combo_Battery.addItem("")
        self.V_Inclino_Combo_Battery.addItem("")
        self.V_Inclino_Combo_Battery.addItem("")
        self.V_Inclino_Combo_Battery.addItem("")
        self.V_Inclino_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.V_Inclino_Combo_Battery)
        self.FSG_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.FSG_Label_3.setWordWrap(True)
        self.FSG_Label_3.setObjectName("FSG_Label_3")
        self.verticalLayout_3.addWidget(self.FSG_Label_3)
        self.FSG_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.FSG_Combo_Battery.setObjectName("FSG_Combo_Battery")
        self.FSG_Combo_Battery.addItem("")
        self.FSG_Combo_Battery.addItem("")
        self.FSG_Combo_Battery.addItem("")
        self.FSG_Combo_Battery.addItem("")
        self.FSG_Combo_Battery.addItem("")
        self.FSG_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.FSG_Combo_Battery)
        self.HSG_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.HSG_Label_3.setWordWrap(True)
        self.HSG_Label_3.setObjectName("HSG_Label_3")
        self.verticalLayout_3.addWidget(self.HSG_Label_3)
        self.HSG_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.HSG_Combo_Battery.setObjectName("HSG_Combo_Battery")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.HSG_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.HSG_Combo_Battery)
        self.Seismometer_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Seismometer_Label_3.setObjectName("Seismometer_Label_3")
        self.verticalLayout_3.addWidget(self.Seismometer_Label_3)
        self.Seismometer_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Seismometer_Combo_Battery.setObjectName("Seismometer_Combo_Battery")
        self.Seismometer_Combo_Battery.addItem("")
        self.Seismometer_Combo_Battery.addItem("")
        self.Seismometer_Combo_Battery.addItem("")
        self.Seismometer_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.Seismometer_Combo_Battery)
        self.Thermistor_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Thermistor_Label_3.setObjectName("Thermistor_Label_3")
        self.verticalLayout_3.addWidget(self.Thermistor_Label_3)
        self.Thermistor_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Thermistor_Combo_Battery.setObjectName("Thermistor_Combo_Battery")
        self.Thermistor_Combo_Battery.addItem("")
        self.Thermistor_Combo_Battery.addItem("")
        self.Thermistor_Combo_Battery.addItem("")
        self.Thermistor_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.Thermistor_Combo_Battery)
        self.Acc_Label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Acc_Label_3.setObjectName("Acc_Label_3")
        self.verticalLayout_3.addWidget(self.Acc_Label_3)
        self.Acc_Combo_Battery = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Acc_Combo_Battery.setObjectName("Acc_Combo_Battery")
        self.Acc_Combo_Battery.addItem("")
        self.Acc_Combo_Battery.addItem("")
        self.Acc_Combo_Battery.addItem("")
        self.Acc_Combo_Battery.addItem("")
        self.Acc_Combo_Battery.addItem("")
        self.Acc_Combo_Battery.addItem("")
        self.verticalLayout_3.addWidget(self.Acc_Combo_Battery)
        self.V_Line = QtWidgets.QFrame(self.Battery)
        self.V_Line.setGeometry(QtCore.QRect(180, 0, 16, 671))
        self.V_Line.setAutoFillBackground(False)
        self.V_Line.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_Line.setObjectName("V_Line")
        self.H_Line = QtWidgets.QFrame(self.Battery)
        self.H_Line.setGeometry(QtCore.QRect(0, 670, 1491, 16))
        self.H_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_Line.setObjectName("H_Line")
        self.Logo_3 = QtWidgets.QLabel(self.Battery)
        self.Logo_3.setGeometry(QtCore.QRect(40, 740, 571, 131))
        self.Logo_3.setText("")
        self.Logo_3.setPixmap(QtGui.QPixmap("../GundalaGUI_V0/Logo Gundala1.png"))
        self.Logo_3.setWordWrap(False)
        self.Logo_3.setObjectName("Logo_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Battery)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(680, 700, 811, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MONITORINGIO_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.MONITORINGIO_3.setObjectName("MONITORINGIO_3")
        self.horizontalLayout_3.addWidget(self.MONITORINGIO_3)
        self.KONTAK_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.KONTAK_3.setObjectName("KONTAK_3")
        self.horizontalLayout_3.addWidget(self.KONTAK_3)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.Battery)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(680, 740, 811, 131))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.DESK_MONITORINGIO_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.DESK_MONITORINGIO_3.setWordWrap(True)
        self.DESK_MONITORINGIO_3.setObjectName("DESK_MONITORINGIO_3")
        self.horizontalLayout_6.addWidget(self.DESK_MONITORINGIO_3)
        self.DES_KONTAK_3 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_6)
        self.DES_KONTAK_3.setObjectName("DES_KONTAK_3")
        self.horizontalLayout_6.addWidget(self.DES_KONTAK_3)

        self.Battery_Plot_Widget = QtWidgets.QWidget(self.Battery)
        self.Battery_Plot_Widget.setGeometry(QtCore.QRect(190, 0, 1331, 671))
        self.Battery_Plot_Widget.setObjectName("Battery_Plot_Widget")
        self.Battery_Plot_Layout = QtWidgets.QGridLayout(self.Battery_Plot_Widget)
        self.Battery_Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.Battery_Plot_Layout.setObjectName("Battery_Plot_Layout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Battery)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.Setting_3 = QtWidgets.QLabel(self.Battery)
        self.Setting_3.setGeometry(QtCore.QRect(0, 680, 179, 22))
        self.Setting_3.setObjectName("Setting_3")
        self.ListTimeRange_2 = QtWidgets.QComboBox(self.Battery)
        self.ListTimeRange_2.setGeometry(QtCore.QRect(0, 700, 179, 30))
        self.ListTimeRange_2.setEditable(False)
        self.ListTimeRange_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.ListTimeRange_2.setMinimumContentsLength(0)
        self.ListTimeRange_2.setModelColumn(0)
        self.ListTimeRange_2.setObjectName("ListTimeRange_2")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.ListTimeRange_2.addItem("")
        self.RumpiangGUI.addTab(self.Battery, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1533, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.RumpiangGUI.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ATRH_Label.setText(_translate("MainWindow", "ATRH"))

        #=====================Live Tab==================
        self.ATRH_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.ATRH_Combo_Live.setItemText(1, _translate("MainWindow", "ATRH 1"))
        self.ATRH_Combo_Live.setItemText(2, _translate("MainWindow", "ATRH 2"))
        self.ATRH_Combo_Live.setItemText(3, _translate("MainWindow", "ATRH 3"))
        self.ATRH_Combo_Live.setItemText(4, _translate("MainWindow", "ATRH 4"))
        self.ATRH_Combo_Live.setItemText(5, _translate("MainWindow", "Display All"))
        self.ATRH_Combo_Live.activated[str].connect(self.Live_ATRH)
        self.Anemometer_Label.setText(_translate("MainWindow", "Anemometer"))
        self.Anemometer_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Anemometer_Combo_Live.setItemText(1, _translate("MainWindow", "Anemometer 1"))
        self.Anemometer_Combo_Live.setItemText(2, _translate("MainWindow", "Anemometer 2"))
        self.Anemometer_Combo_Live.setItemText(3, _translate("MainWindow", "Anemometer 3"))
        self.Anemometer_Combo_Live.setItemText(4, _translate("MainWindow", "Anemometer 4"))
        self.Anemometer_Combo_Live.setItemText(5, _translate("MainWindow", "Display All"))
        self.Displacement_Label.setText(_translate("MainWindow", "Displacement "))
        self.Displacement_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Displacement_Combo_Live.setItemText(1, _translate("MainWindow", "Displacement 1"))
        self.Displacement_Combo_Live.setItemText(2, _translate("MainWindow", "Displacement 2"))
        self.Displacement_Combo_Live.setItemText(3, _translate("MainWindow", "Displacement 3"))
        self.Displacement_Combo_Live.setItemText(4, _translate("MainWindow", "Displacement 4"))
        self.Displacement_Combo_Live.setItemText(5, _translate("MainWindow", "Display All"))
        self.Displacement_Combo_Live.activated[str].connect(self.Live_LinearDisplacement)
        self.H_Inclino_Label.setText(_translate("MainWindow", "Horizontal Inclinometer"))
        self.H_Inclino_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.H_Inclino_Combo_Live.setItemText(1, _translate("MainWindow", "H Inclinometer 1"))
        self.H_Inclino_Combo_Live.setItemText(2, _translate("MainWindow", "H Inclinometer 2"))
        self.H_Inclino_Combo_Live.setItemText(3, _translate("MainWindow", "H Inclinometer 3"))
        self.H_Inclino_Combo_Live.setItemText(4, _translate("MainWindow", "H Inclinometer 4"))
        self.H_Inclino_Combo_Live.setItemText(5, _translate("MainWindow", "H Inclinometer 5"))
        self.H_Inclino_Combo_Live.setItemText(6, _translate("MainWindow", "H Inclinometer 6"))
        self.H_Inclino_Combo_Live.setItemText(7, _translate("MainWindow", "H Inclinometer 7"))
        self.H_Inclino_Combo_Live.setItemText(8, _translate("MainWindow", "H Inclinometer 8"))
        self.H_Inclino_Combo_Live.setItemText(9, _translate("MainWindow", "Display 1-4"))
        self.H_Inclino_Combo_Live.setItemText(10, _translate("MainWindow", "Display 5-8"))
        self.V_Inclino_Label.setText(_translate("MainWindow", "Vertikal Inclinometer"))
        self.V_Inclino_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.V_Inclino_Combo_Live.setItemText(1, _translate("MainWindow", "V Inclinometer 1"))
        self.V_Inclino_Combo_Live.setItemText(2, _translate("MainWindow", "V Inclinometer 2"))
        self.V_Inclino_Combo_Live.setItemText(3, _translate("MainWindow", "V Inclinometer 3"))
        self.V_Inclino_Combo_Live.setItemText(4, _translate("MainWindow", "V Inclinometer 4"))
        self.V_Inclino_Combo_Live.setItemText(5, _translate("MainWindow", "Display All"))
        self.FSG_Label.setText(_translate("MainWindow", "Frame Strain Gauge"))
        self.FSG_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.FSG_Combo_Live.setItemText(1, _translate("MainWindow", "FSG 1"))
        self.FSG_Combo_Live.setItemText(2, _translate("MainWindow", "FSG 2"))
        self.FSG_Combo_Live.setItemText(3, _translate("MainWindow", "FSG 3"))
        self.FSG_Combo_Live.setItemText(4, _translate("MainWindow", "FSG 4"))
        self.FSG_Combo_Live.setItemText(5, _translate("MainWindow", "Display All"))
        self.HSG_Label.setText(_translate("MainWindow", "Hanger Strain Gauge"))
        self.HSG_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.HSG_Combo_Live.setItemText(1, _translate("MainWindow", "HSG 1"))
        self.HSG_Combo_Live.setItemText(2, _translate("MainWindow", "HSG 2"))
        self.HSG_Combo_Live.setItemText(3, _translate("MainWindow", "HSG 3"))
        self.HSG_Combo_Live.setItemText(4, _translate("MainWindow", "HSG 4"))
        self.HSG_Combo_Live.setItemText(5, _translate("MainWindow", "HSG 5"))
        self.HSG_Combo_Live.setItemText(6, _translate("MainWindow", "HSG 6"))
        self.HSG_Combo_Live.setItemText(7, _translate("MainWindow", "HSG 7"))
        self.HSG_Combo_Live.setItemText(8, _translate("MainWindow", "HSG 8"))
        self.HSG_Combo_Live.setItemText(9, _translate("MainWindow", "HSG 9"))
        self.HSG_Combo_Live.setItemText(10, _translate("MainWindow", "HSG 10"))
        self.HSG_Combo_Live.setItemText(11, _translate("MainWindow", "HSG 11"))
        self.HSG_Combo_Live.setItemText(12, _translate("MainWindow", "HSG 12"))
        self.HSG_Combo_Live.setItemText(13, _translate("MainWindow", "Display 1-4"))
        self.HSG_Combo_Live.setItemText(14, _translate("MainWindow", "Display 5-8"))
        self.HSG_Combo_Live.setItemText(15, _translate("MainWindow", "Display 9-12"))
        self.Seismometer_Label.setText(_translate("MainWindow", "Seismometer"))
        self.Seismometer_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Seismometer_Combo_Live.setItemText(1, _translate("MainWindow", "Seismometer 1"))
        self.Seismometer_Combo_Live.setItemText(2, _translate("MainWindow", "Seismometer 2"))
        self.Seismometer_Combo_Live.setItemText(3, _translate("MainWindow", "Display All"))
        self.Thermistor_Label.setText(_translate("MainWindow", "Themistor"))
        self.Thermistor_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Thermistor_Combo_Live.setItemText(1, _translate("MainWindow", "Thermistor 1"))
        self.Thermistor_Combo_Live.setItemText(2, _translate("MainWindow", "Thermistor 2"))
        self.Thermistor_Combo_Live.setItemText(3, _translate("MainWindow", "Display All"))
        self.Thermistor_Combo_Live.activated[str].connect(self.Live_TM)
        self.Acc_Label.setText(_translate("MainWindow", "Accelerometer"))
        self.Acc_Combo_Live.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Acc_Combo_Live.setItemText(1, _translate("MainWindow", "Accelerometer 1"))
        self.Acc_Combo_Live.setItemText(2, _translate("MainWindow", "Accelerometer 2"))
        self.Acc_Combo_Live.setItemText(3, _translate("MainWindow", "Accelerometer 3"))
        self.Acc_Combo_Live.setItemText(4, _translate("MainWindow", "Accelerometer 4"))
        self.Acc_Combo_Live.setItemText(5, _translate("MainWindow", "Display All"))
        self.MONITORINGIO.setText(_translate("MainWindow", "MONITORING.IO"))
        self.KONTAK.setText(_translate("MainWindow", "KONTAK"))
        self.DESK_MONITORINGIO.setText(_translate("MainWindow", "Aplikasi Monitoring.io adalah aplikasi untuk pemantauan kondisi struktur oleh PT. Gundala Widya Karya. Untuk informasi lebih lanjut klik www.gundala.co.id"))
        self.DES_KONTAK.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jl.Tebet Timur dalam III-D no.11, Jakarta Selatan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">support@gundala.co.id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 853 2125 1627</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 21 21282553</p></body></html>"))
        self.Setting.setText(_translate("MainWindow", "Setting"))
        self.ListTimeRange.setCurrentText(_translate("MainWindow", "Time Range"))
        self.ListTimeRange.setItemText(0, _translate("MainWindow", "Time Range"))
        self.ListTimeRange.setItemText(1, _translate("MainWindow", "1 minute"))
        self.ListTimeRange.setItemText(2, _translate("MainWindow", "5 minutes"))
        self.ListTimeRange.setItemText(3, _translate("MainWindow", "15 minutes"))
        self.ListTimeRange.setItemText(4, _translate("MainWindow", "30 minutes"))
        self.ListTimeRange.setItemText(5, _translate("MainWindow", "1 hour"))
        self.ListTimeRange.setItemText(6, _translate("MainWindow", "4 hours"))
        self.ListTimeRange.setItemText(7, _translate("MainWindow", "12 hours"))
        self.ListTimeRange.setItemText(8, _translate("MainWindow", "1 day"))
        self.ListTimeRange.activated[str].connect(self.TimeRange_Live_Plot)
        self.RumpiangGUI.setTabText(self.RumpiangGUI.indexOf(self.Live), _translate("MainWindow", "Live"))

        #=================================History Tab===================================
        self.ATRH_Label_2.setText(_translate("MainWindow", "ATRH"))
        self.ATRH_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.ATRH_Combo_History.setItemText(1, _translate("MainWindow", "ATRH 1"))
        self.ATRH_Combo_History.setItemText(2, _translate("MainWindow", "ATRH 2"))
        self.ATRH_Combo_History.setItemText(3, _translate("MainWindow", "ATRH 3"))
        self.ATRH_Combo_History.setItemText(4, _translate("MainWindow", "ATRH 4"))
        self.ATRH_Combo_History.setItemText(5, _translate("MainWindow", "Display All"))
        self.ATRH_Combo_History.activated[str].connect(self.History_ATRH)
        self.Anemometer_Label_2.setText(_translate("MainWindow", "Anemometer"))
        self.Anemometer_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Anemometer_Combo_History.setItemText(1, _translate("MainWindow", "Anemometer 1"))
        self.Anemometer_Combo_History.setItemText(2, _translate("MainWindow", "Anemometer 2"))
        self.Anemometer_Combo_History.setItemText(3, _translate("MainWindow", "Anemometer 3"))
        self.Anemometer_Combo_History.setItemText(4, _translate("MainWindow", "Anemometer 4"))
        self.Anemometer_Combo_History.setItemText(5, _translate("MainWindow", "Display All"))
        self.Displacement_Label_2.setText(_translate("MainWindow", "Displacement "))
        self.Displacement_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Displacement_Combo_History.setItemText(1, _translate("MainWindow", "Displacement 1"))
        self.Displacement_Combo_History.setItemText(2, _translate("MainWindow", "Displacement 2"))
        self.Displacement_Combo_History.setItemText(3, _translate("MainWindow", "Displacement 3"))
        self.Displacement_Combo_History.setItemText(4, _translate("MainWindow", "Displacement 4"))
        self.Displacement_Combo_History.setItemText(5, _translate("MainWindow", "Display All"))
        self.Displacement_Combo_History.activated[str].connect(self.History_LinearDisplacement)
        self.H_Inclino_Label_2.setText(_translate("MainWindow", "Horizontal Inclinometer"))
        self.H_Inclino_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.H_Inclino_Combo_History.setItemText(1, _translate("MainWindow", "H Inclinometer 1"))
        self.H_Inclino_Combo_History.setItemText(2, _translate("MainWindow", "H Inclinometer 2"))
        self.H_Inclino_Combo_History.setItemText(3, _translate("MainWindow", "H Inclinometer 3"))
        self.H_Inclino_Combo_History.setItemText(4, _translate("MainWindow", "H Inclinometer 4"))
        self.H_Inclino_Combo_History.setItemText(5, _translate("MainWindow", "H Inclinometer 5"))
        self.H_Inclino_Combo_History.setItemText(6, _translate("MainWindow", "H Inclinometer 6"))
        self.H_Inclino_Combo_History.setItemText(7, _translate("MainWindow", "H Inclinometer 7"))
        self.H_Inclino_Combo_History.setItemText(8, _translate("MainWindow", "H Inclinometer 8"))
        self.H_Inclino_Combo_History.setItemText(9, _translate("MainWindow", "Display 1-4"))
        self.H_Inclino_Combo_History.setItemText(10, _translate("MainWindow", "Display 5-8"))
        self.V_Inclino_Label_2.setText(_translate("MainWindow", "Vertikal Inclinometer"))
        self.V_Inclino_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.V_Inclino_Combo_History.setItemText(1, _translate("MainWindow", "V Inclinometer 1"))
        self.V_Inclino_Combo_History.setItemText(2, _translate("MainWindow", "V Inclinometer 2"))
        self.V_Inclino_Combo_History.setItemText(3, _translate("MainWindow", "V Inclinometer 3"))
        self.V_Inclino_Combo_History.setItemText(4, _translate("MainWindow", "V Inclinometer 4"))
        self.V_Inclino_Combo_History.setItemText(5, _translate("MainWindow", "Display All"))
        self.FSG_Label_2.setText(_translate("MainWindow", "Frame Strain Gauge"))
        self.FSG_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.FSG_Combo_History.setItemText(1, _translate("MainWindow", "FSG 1"))
        self.FSG_Combo_History.setItemText(2, _translate("MainWindow", "FSG 2"))
        self.FSG_Combo_History.setItemText(3, _translate("MainWindow", "FSG 3"))
        self.FSG_Combo_History.setItemText(4, _translate("MainWindow", "FSG 4"))
        self.FSG_Combo_History.setItemText(5, _translate("MainWindow", "Display All"))
        self.HSG_Label_2.setText(_translate("MainWindow", "Hanger Strain Gauge"))
        self.HSG_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.HSG_Combo_History.setItemText(1, _translate("MainWindow", "HSG 1"))
        self.HSG_Combo_History.setItemText(2, _translate("MainWindow", "HSG 2"))
        self.HSG_Combo_History.setItemText(3, _translate("MainWindow", "HSG 3"))
        self.HSG_Combo_History.setItemText(4, _translate("MainWindow", "HSG 4"))
        self.HSG_Combo_History.setItemText(5, _translate("MainWindow", "HSG 5"))
        self.HSG_Combo_History.setItemText(6, _translate("MainWindow", "HSG 6"))
        self.HSG_Combo_History.setItemText(7, _translate("MainWindow", "HSG 7"))
        self.HSG_Combo_History.setItemText(8, _translate("MainWindow", "HSG 8"))
        self.HSG_Combo_History.setItemText(9, _translate("MainWindow", "HSG 9"))
        self.HSG_Combo_History.setItemText(10, _translate("MainWindow", "HSG 10"))
        self.HSG_Combo_History.setItemText(11, _translate("MainWindow", "HSG 11"))
        self.HSG_Combo_History.setItemText(12, _translate("MainWindow", "HSG 12"))
        self.HSG_Combo_History.setItemText(13, _translate("MainWindow", "Display 1-4"))
        self.HSG_Combo_History.setItemText(14, _translate("MainWindow", "Display 5-8"))
        self.HSG_Combo_History.setItemText(15, _translate("MainWindow", "Display 9-12"))
        self.Seismometer_Label_2.setText(_translate("MainWindow", "Seismometer"))
        self.Seismometer_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Seismometer_Combo_History.setItemText(1, _translate("MainWindow", "Seismometer 1"))
        self.Seismometer_Combo_History.setItemText(2, _translate("MainWindow", "Seismometer 2"))
        self.Seismometer_Combo_History.setItemText(3, _translate("MainWindow", "Display All"))
        self.Thermistor_Label_2.setText(_translate("MainWindow", "Themistor"))
        self.Thermistor_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Thermistor_Combo_History.setItemText(1, _translate("MainWindow", "Thermistor 1"))
        self.Thermistor_Combo_History.setItemText(2, _translate("MainWindow", "Thermistor 2"))
        self.Thermistor_Combo_History.setItemText(3, _translate("MainWindow", "Display All"))
        self.Thermistor_Combo_History.activated[str].connect(self.History_TM)
        self.Acc_Label_2.setText(_translate("MainWindow", "Accelerometer"))
        self.Acc_Combo_History.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Acc_Combo_History.setItemText(1, _translate("MainWindow", "Accelerometer 1"))
        self.Acc_Combo_History.setItemText(2, _translate("MainWindow", "Accelerometer 2"))
        self.Acc_Combo_History.setItemText(3, _translate("MainWindow", "Accelerometer 3"))
        self.Acc_Combo_History.setItemText(4, _translate("MainWindow", "Accelerometer 4"))
        self.Acc_Combo_History.setItemText(5, _translate("MainWindow", "Display All"))
        self.DESK_MONITORINGIO_2.setText(_translate("MainWindow", "Aplikasi Monitoring.io adalah aplikasi untuk pemantauan kondisi struktur oleh PT. Gundala Widya Karya. Untuk informasi lebih lanjut klik www.gundala.co.id"))
        self.DES_KONTAK_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jl.Tebet Timur dalam III-D no.11, Jakarta Selatan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">support@gundala.co.id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 853 2125 1627</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 21 21282553</p></body></html>"))
        self.MONITORINGIO_2.setText(_translate("MainWindow", "MONITORING.IO"))
        self.KONTAK_2.setText(_translate("MainWindow", "KONTAK"))
        self.Setting_2.setText(_translate("MainWindow", "Setting"))
        self.BeginTime_String.setText(_translate("MainWindow", "Begin Time"))
        self.EndTime_String.setText(_translate("MainWindow", "End Time"))
        self.SetTimeRange_2.setText(_translate("MainWindow", "Set"))
        self.SetTimeRange_2.clicked.connect(self.SetHistory)
        self.RumpiangGUI.setTabText(self.RumpiangGUI.indexOf(self.Historical), _translate("MainWindow", "Historical"))

        #=====================================Battery Tab====================================================
        self.ATRH_Label_3.setText(_translate("MainWindow", "ATRH"))
        self.ATRH_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.ATRH_Combo_Battery.setItemText(1, _translate("MainWindow", "ATRH 1"))
        self.ATRH_Combo_Battery.setItemText(2, _translate("MainWindow", "ATRH 2"))
        self.ATRH_Combo_Battery.setItemText(3, _translate("MainWindow", "ATRH 3"))
        self.ATRH_Combo_Battery.setItemText(4, _translate("MainWindow", "ATRH 4"))
        self.ATRH_Combo_Battery.setItemText(5, _translate("MainWindow", "Display All"))
        self.ATRH_Combo_Battery.activated[str].connect(self.Battery_ATRH)
        self.Anemometer_Label_3.setText(_translate("MainWindow", "Anemometer"))
        self.Anemometer_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Anemometer_Combo_Battery.setItemText(1, _translate("MainWindow", "Anemometer 1"))
        self.Anemometer_Combo_Battery.setItemText(2, _translate("MainWindow", "Anemometer 2"))
        self.Anemometer_Combo_Battery.setItemText(3, _translate("MainWindow", "Anemometer 3"))
        self.Anemometer_Combo_Battery.setItemText(4, _translate("MainWindow", "Anemometer 4"))
        self.Anemometer_Combo_Battery.setItemText(5, _translate("MainWindow", "Display All"))
        self.Displacement_Label_3.setText(_translate("MainWindow", "Displacement "))
        self.Displacement_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Displacement_Combo_Battery.setItemText(1, _translate("MainWindow", "Displacement 1"))
        self.Displacement_Combo_Battery.setItemText(2, _translate("MainWindow", "Displacement 2"))
        self.Displacement_Combo_Battery.setItemText(3, _translate("MainWindow", "Displacement 3"))
        self.Displacement_Combo_Battery.setItemText(4, _translate("MainWindow", "Displacement 4"))
        self.Displacement_Combo_Battery.setItemText(5, _translate("MainWindow", "Display All"))
        self.Displacement_Combo_Battery.activated[str].connect(self.Battery_LinearDisplacement)
        self.H_Inclino_Label_3.setText(_translate("MainWindow", "Horizontal Inclinometer"))
        self.H_Inclino_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.H_Inclino_Combo_Battery.setItemText(1, _translate("MainWindow", "H Inclinometer 1"))
        self.H_Inclino_Combo_Battery.setItemText(2, _translate("MainWindow", "H Inclinometer 2"))
        self.H_Inclino_Combo_Battery.setItemText(3, _translate("MainWindow", "H Inclinometer 3"))
        self.H_Inclino_Combo_Battery.setItemText(4, _translate("MainWindow", "H Inclinometer 4"))
        self.H_Inclino_Combo_Battery.setItemText(5, _translate("MainWindow", "H Inclinometer 5"))
        self.H_Inclino_Combo_Battery.setItemText(6, _translate("MainWindow", "H Inclinometer 6"))
        self.H_Inclino_Combo_Battery.setItemText(7, _translate("MainWindow", "H Inclinometer 7"))
        self.H_Inclino_Combo_Battery.setItemText(8, _translate("MainWindow", "H Inclinometer 8"))
        self.H_Inclino_Combo_Battery.setItemText(9, _translate("MainWindow", "Display 1-4"))
        self.H_Inclino_Combo_Battery.setItemText(10, _translate("MainWindow", "Display 5-8"))
        self.V_Inclino_Label_3.setText(_translate("MainWindow", "Vertikal Inclinometer"))
        self.V_Inclino_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.V_Inclino_Combo_Battery.setItemText(1, _translate("MainWindow", "V Inclinometer 1"))
        self.V_Inclino_Combo_Battery.setItemText(2, _translate("MainWindow", "V Inclinometer 2"))
        self.V_Inclino_Combo_Battery.setItemText(3, _translate("MainWindow", "V Inclinometer 3"))
        self.V_Inclino_Combo_Battery.setItemText(4, _translate("MainWindow", "V Inclinometer 4"))
        self.V_Inclino_Combo_Battery.setItemText(5, _translate("MainWindow", "Display All"))
        self.FSG_Label_3.setText(_translate("MainWindow", "Frame Strain Gauge"))
        self.FSG_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.FSG_Combo_Battery.setItemText(1, _translate("MainWindow", "FSG 1"))
        self.FSG_Combo_Battery.setItemText(2, _translate("MainWindow", "FSG 2"))
        self.FSG_Combo_Battery.setItemText(3, _translate("MainWindow", "FSG 3"))
        self.FSG_Combo_Battery.setItemText(4, _translate("MainWindow", "FSG 4"))
        self.FSG_Combo_Battery.setItemText(5, _translate("MainWindow", "Display All"))
        self.HSG_Label_3.setText(_translate("MainWindow", "Hanger Strain Gauge"))
        self.HSG_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.HSG_Combo_Battery.setItemText(1, _translate("MainWindow", "HSG 1"))
        self.HSG_Combo_Battery.setItemText(2, _translate("MainWindow", "HSG 2"))
        self.HSG_Combo_Battery.setItemText(3, _translate("MainWindow", "HSG 3"))
        self.HSG_Combo_Battery.setItemText(4, _translate("MainWindow", "HSG 4"))
        self.HSG_Combo_Battery.setItemText(5, _translate("MainWindow", "HSG 5"))
        self.HSG_Combo_Battery.setItemText(6, _translate("MainWindow", "HSG 6"))
        self.HSG_Combo_Battery.setItemText(7, _translate("MainWindow", "HSG 7"))
        self.HSG_Combo_Battery.setItemText(8, _translate("MainWindow", "HSG 8"))
        self.HSG_Combo_Battery.setItemText(9, _translate("MainWindow", "HSG 9"))
        self.HSG_Combo_Battery.setItemText(10, _translate("MainWindow", "HSG 10"))
        self.HSG_Combo_Battery.setItemText(11, _translate("MainWindow", "HSG 11"))
        self.HSG_Combo_Battery.setItemText(12, _translate("MainWindow", "HSG 12"))
        self.HSG_Combo_Battery.setItemText(13, _translate("MainWindow", "Display 1-4"))
        self.HSG_Combo_Battery.setItemText(14, _translate("MainWindow", "Display 5-8"))
        self.HSG_Combo_Battery.setItemText(15, _translate("MainWindow", "Display 9-12"))
        self.Seismometer_Label_3.setText(_translate("MainWindow", "Seismometer"))
        self.Seismometer_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Seismometer_Combo_Battery.setItemText(1, _translate("MainWindow", "Seismometer 1"))
        self.Seismometer_Combo_Battery.setItemText(2, _translate("MainWindow", "Seismometer 2"))
        self.Seismometer_Combo_Battery.setItemText(3, _translate("MainWindow", "Display All"))
        self.Thermistor_Label_3.setText(_translate("MainWindow", "Themistor"))
        self.Thermistor_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Thermistor_Combo_Battery.setItemText(1, _translate("MainWindow", "Thermistor 1"))
        self.Thermistor_Combo_Battery.setItemText(2, _translate("MainWindow", "Thermistor 2"))
        self.Thermistor_Combo_Battery.setItemText(3, _translate("MainWindow", "Display All"))
        self.Thermistor_Combo_Battery.activated[str].connect(self.Battery_TM)
        self.Acc_Label_3.setText(_translate("MainWindow", "Accelerometer"))
        self.Acc_Combo_Battery.setItemText(0, _translate("MainWindow", "Select Sensor ..."))
        self.Acc_Combo_Battery.setItemText(1, _translate("MainWindow", "Accelerometer 1"))
        self.Acc_Combo_Battery.setItemText(2, _translate("MainWindow", "Accelerometer 2"))
        self.Acc_Combo_Battery.setItemText(3, _translate("MainWindow", "Accelerometer 3"))
        self.Acc_Combo_Battery.setItemText(4, _translate("MainWindow", "Accelerometer 4"))
        self.Acc_Combo_Battery.setItemText(5, _translate("MainWindow", "Display All"))
        self.MONITORINGIO_3.setText(_translate("MainWindow", "MONITORING.IO"))
        self.KONTAK_3.setText(_translate("MainWindow", "KONTAK"))
        self.DESK_MONITORINGIO_3.setText(_translate("MainWindow", "Aplikasi Monitoring.io adalah aplikasi untuk pemantauan kondisi struktur oleh PT. Gundala Widya Karya. Untuk informasi lebih lanjut klik www.gundala.co.id"))
        self.DES_KONTAK_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jl.Tebet Timur dalam III-D no.11, Jakarta Selatan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">support@gundala.co.id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 853 2125 1627</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 21 21282553</p></body></html>"))
        self.Setting_3.setText(_translate("MainWindow", "Setting"))
        self.ListTimeRange_2.setCurrentText(_translate("MainWindow", "Time Range"))
        self.ListTimeRange_2.setItemText(0, _translate("MainWindow", "Time Range"))
        self.ListTimeRange_2.setItemText(1, _translate("MainWindow", "1 minute"))
        self.ListTimeRange_2.setItemText(2, _translate("MainWindow", "5 minutes"))
        self.ListTimeRange_2.setItemText(3, _translate("MainWindow", "15 minutes"))
        self.ListTimeRange_2.setItemText(4, _translate("MainWindow", "30 minutes"))
        self.ListTimeRange_2.setItemText(5, _translate("MainWindow", "1 hour"))
        self.ListTimeRange_2.setItemText(6, _translate("MainWindow", "4 hours"))
        self.ListTimeRange_2.setItemText(7, _translate("MainWindow", "12 hours"))
        self.ListTimeRange_2.setItemText(8, _translate("MainWindow", "1 day"))
        self.ListTimeRange_2.activated[str].connect(self.TimeRange_Battery_Plot)
        self.RumpiangGUI.setTabText(self.RumpiangGUI.indexOf(self.Battery), _translate("MainWindow", "Battery"))


        self.Index = {
                "ATRH1":0,
                "ATRH2":0,
                "ATRH3":0,
                "ATRH4":0,
                "ATRH_All":0,
                "LD1":0,
                "LD2":0,
                "LD3":0,
                "LD4":0,
                "LD_All":0,
                "FSG1":0,
                "FSG2":0,
                "FSG3":0,
                "FSG4":0,
                "FSG_All":0,
                "HSG1":0,
                "HSG2":0,
                "HSG3":0,
                "HSG4":0,
                "HSG5":0,
                "HSG6":0,
                "HSG7":0,
                "HG8":0,
                "HSG9":0,
                "HSG10":0,
                "HSG11":0,
                "HSG12":0,
                "HSG_All":0,
                "TM1":0,
                "TM2":0,
                "TM_All":0
        }
   #=====================================================================================================================================================================
#Live Plot ATRH

   def Live_ATRH(self, text):
        if text == 'ATRH 1':
                self.configure_Live_Plot_ATRH(1,5,1,'ATRH 1')
                self.zero_one_Index('ATRH1')
        elif text == 'ATRH 2':
                self.configure_Live_Plot_ATRH(2,5,1,'ATRH 2')
                self.zero_one_Index('ATRH2')
        elif text == 'ATRH 3':
                self.configure_Live_Plot_ATRH(3,5,1,'ATRH 3')
                self.zero_one_Index('ATRH3')
        elif text == 'ATRH 4':
                self.configure_Live_Plot_ATRH(4,5,1,'ATRH 4')
                self.zero_one_Index('ATRH4')
        elif text == 'Display All':
                print('ATRH_All')
                self.zero_one_Index('ATRH_All')
        
#Live Plot Linear Displacement

   def Live_LinearDisplacement(self, text):
        if text == 'Displacement 1':
                self.configure_Live_Plot_LinearDisplacement(1,5,1,'Displacement 1',1,1,1,1)
                self.zero_one_Index('LD1')
        elif text == 'Displacement 2':
                self.configure_Live_Plot_LinearDisplacement(2,5,1,'Displacement 2',1,1,1,1)
                self.zero_one_Index('LD2')
        elif text == 'Displacement 3':
                self.configure_Live_Plot_LinearDisplacement(3,5,1,'Displacement 3',1,1,1,1)
                self.zero_one_Index('LD3')
        elif text == 'Displacement 4':
                self.configure_Live_Plot_LinearDisplacement(4,5,1,'Displacement 4',1,1,1,1)
                self.zero_one_Index('LD4')
        elif text == 'Display All':
                self.configure_Live_Plot_LinearDisplacement(1,5,1,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,1,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,1,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,1,'Displacement 4',1,1,1,1)
                self.zero_one_Index('LD_All')

#Live Plot Strain Gauge

   def Live_FrameStrainGauge(self, text):
        if text == 'FSG 1':
                self.configure_Live_Plot_StrainGauge(1,5,1,'FSG 1',1,1,1,1)
                self.zero_one_Index('FSG1')
        elif text == 'FSG 2':
                self.configure_Live_Plot_StrainGauge(2,5,1,'FSG 2',1,1,1,1)
                self.zero_one_Index('FSG2')
        elif text == 'FSG 3':
                self.configure_Live_Plot_StrainGauge(3,5,1,'FSG 3',1,1,1,1)
                self.zero_one_Index('FSG3')
        elif text == 'FSG 4':
                self.configure_Live_Plot_StrainGauge(4,5,1,'FSG 4',1,1,1,1)
                self.zero_one_Index('FSG4')
        elif text == 'Display All':
                self.configure_Live_Plot_StrainGauge(1,5,1,'FSG 1',0,0,1,1)
                self.add_Live_Plot_StrainGauge(2,5,1,'FSG 2',0,1,1,1)
                self.add_Live_Plot_StrainGauge(3,5,1,'FSG 3',1,0,1,1)
                self.add_Live_Plot_StrainGauge(4,5,1,'FSG 4',1,1,1,1)
                self.zero_one_Index('FSG_All')
                
   def Live_HangerStrainGauge(self, text):
        if text == 'HSG 1':
                self.configure_Live_Plot_StrainGauge(5,5,1,'HSG 1',1,1,1,1)
                self.zero_one_Index('HSG1')
        elif text == 'HSG 2':
                self.configure_Live_Plot_StrainGauge(6,5,1,'HSG 2',1,1,1,1)
                self.zero_one_Index('HSG2')
        elif text == 'HSG 3':
                self.configure_Live_Plot_StrainGauge(4,5,1,'HSG 3',1,1,1,1)
                self.zero_one_Index('HSG3')
        elif text == 'HSG 4':
                self.configure_Live_Plot_StrainGauge(2,5,1,'HSG 4',1,1,1,1)
                self.zero_one_Index('HSG4')
        elif text == 'HSG 5':
                self.configure_Live_Plot_StrainGauge(3,5,1,'HSG 5',1,1,1,1)
                self.zero_one_Index('HSG5')
        elif text == 'HSG 6':
                self.configure_Live_Plot_StrainGauge(4,5,1,'HSG 6',1,1,1,1)
                self.zero_one_Index('HSG6')
        elif text == 'HSG 7':
                self.configure_Live_Plot_StrainGauge(2,5,1,'HSG 7',1,1,1,1)
                self.zero_one_Index('HSG7')
        elif text == 'HSG 8':
                self.configure_Live_Plot_StrainGauge(3,5,1,'HSG 8',1,1,1,1)
                self.zero_one_Index('HSG8')
        elif text == 'HSG 9':
                self.configure_Live_Plot_StrainGauge(4,5,1,'HSG 9',1,1,1,1)
                self.zero_one_Index('HSG9')
        elif text == 'HSG 10':
                self.configure_Live_Plot_StrainGauge(2,5,1,'HSG 10',1,1,1,1)
                self.zero_one_Index('HSG10')
        elif text == 'HSG 11':
                self.configure_Live_Plot_StrainGauge(3,5,1,'HSG 11',1,1,1,1)
                self.zero_one_Index('HSG11')
        elif text == 'HSG 12':
                self.configure_Live_Plot_StrainGauge(4,5,1,'HSG 12',1,1,1,1)
                self.zero_one_Index('HSG12')                 
        elif text == 'Display All':
                self.configure_Live_Plot_StrainGauge(2,5,1,'HSG 1',0,1,1,1)
                self.add_Live_Plot_StrainGauge(3,5,1,'HSG 2',1,0,1,1)
                self.add_Live_Plot_StrainGauge(4,5,1,'HSG 3',1,1,1,1)
                self.add_Live_Plot_StrainGauge(2,5,1,'HSG 4',0,1,1,1)
                self.add_Live_Plot_StrainGauge(3,5,1,'HSG 5',1,0,1,1)
                self.add_Live_Plot_StrainGauge(4,5,1,'HSG 6',1,1,1,1)
                self.add_Live_Plot_StrainGauge(2,5,1,'HSG 7',0,1,1,1)
                self.add_Live_Plot_StrainGauge(3,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_StrainGauge(4,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_StrainGauge(2,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_StrainGauge(3,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_StrainGauge(4,5,1,'HSG 12',1,1,1,1)
                self.zero_one_Index('HSG_All')

#Live Plot Temperatur Material

   def Live_TM(self, text):
        if text == 'Thermistor 1':
                self.configure_Live_Plot_Temperatur_Material(1,5,1,'Thermistor 1',1,1,1,1)
                self.zero_one_Index('TM1')
        elif text == 'Thermistor 2':
                self.configure_Live_Plot_Temperatur_Material(2,5,1,'Thermistor 2',1,1,1,1)
                self.zero_one_Index('TM2')
        elif text == 'Display All':
                self.configure_Live_Plot_Temperatur_Material(1,5,1,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,1,'Thermistor 2',0,1,2,1)
                self.zero_one_Index('TM_All')

#==================================================================================================================================================================

#History Plot ATRH

   def History_ATRH(self, text):
        if text == 'ATRH 1':
                print('ATRH1')
                self.zero_one_Index('ATRH1')
        elif text == 'ATRH 2':
                print('ATRH2')
                self.zero_one_Index('ATRH2')
        elif text == 'ATRH 3':
                print('ATRH3')
                self.zero_one_Index('ATRH3')
        elif text == 'ATRH 4':
                print('ATRH4')
                self.zero_one_Index('ATRH4')
        elif text == 'Display All':
                print('ATRH_All')
                self.zero_one_Index('ATRH_All')

#History Plot Linear Displacement

   def History_LinearDisplacement(self, text):
        if text == 'Displacement 1':
                print('LD1')
                self.zero_one_Index('LD1')
        elif text == 'Displacement 2':
                print('LD2')
                self.zero_one_Index('LD2')
        elif text == 'Displacement 3':
                print('LD3')
                self.zero_one_Index('LD3')
        elif text == 'Displacement 4':
                print('LD4')
                self.zero_one_Index('LD4')
        elif text == 'Display All':
                print('LD_All')
                self.zero_one_Index('LD_All')

#History Plot Frame Strain Gauge

   def History_StrainGauge(self, text):
        if text == 'FSG 1':
                print('FSG1')
                self.zero_one_Index('FSG1')
        elif text == 'FSG 2':
                print('FSG2')
                self.zero_one_Index('FSG2')
        elif text == 'FSG 3':
                print('FSG3')
                self.zero_one_Index('FSG3')
        elif text == 'FSG 4':
                print('FSG4')
                self.zero_one_Index('FSG4')
        elif text == 'Display All':
                print('FSG_All')
                self.zero_one_Index('FSG_All')


   def History_StrainGauge(self, text):                
        if text == 'HSG 1':
                print('HSG1')
                self.zero_one_Index('HSG1')
        elif text == 'HSG 2':
                print('HSG2')
                self.zero_one_Index('HSG2')
        elif text == 'HSG 3':
                print('HSG3')
                self.zero_one_Index('HSG3')
        elif text == 'HSG 4':
                print('HSG4')
                self.zero_one_Index('HSG4')
        elif text == 'HSG 5':
                print('HSG5')
                self.zero_one_Index('HSG5')
        elif text == 'HSG 6':
                print('HSG6')
                self.zero_one_Index('HSG6')
        elif text == 'HSG 7':
                print('HSG7')
                self.zero_one_Index('HSG7')
        elif text == 'HSG 8':
                print('HSG8')
                self.zero_one_Index('HSG8')
        elif text == 'HSG 9':
                print('HSG9')
                self.zero_one_Index('HSG9')
        elif text == 'HSG 10':
                print('HSG10')
                self.zero_one_Index('HSG10')
        elif text == 'HSG 11':
                print('HSG11')
                self.zero_one_Index('HSG11')
        elif text == 'HSG 12':
                print('HSG12')
                self.zero_one_Index('HSG12')                                                                        
        elif text == 'Display All':
                print('HSG_All')
                self.zero_one_Index('HSG_All')

#History Plot Temperatur Material

   def History_TM(self, text):
        if text == 'Thermistor 1':
                print('TM1')
                self.zero_one_Index('TM1')
        elif text == 'Thermistor 2':
                print('TM2')
                self.zero_one_Index('TM2')
        elif text == 'Display All':
                print('TM_All')
                self.zero_one_Index('TM_All')

#=====================================================================================================================================================================
#Battery Plot ATRH

   def Battery_ATRH(self, text):
        if text == 'ATRH 1':
                self.configure_Battery_Plot_ATRH(1,5,1,'ATRH 1',1,1,1,1)
                self.zero_one_Index('ATRH1')
        elif text == 'ATRH 2':
                self.configure_Battery_Plot_ATRH(2,5,1,'ATRH 2',1,1,1,1)
                self.zero_one_Index('ATRH2')
        elif text == 'ATRH 3':
                self.configure_Battery_Plot_ATRH(3,5,1,'ATRH 3',1,1,1,1)
                self.zero_one_Index('ATRH3')
        elif text == 'ATRH 4':
                self.configure_Battery_Plot_ATRH(4,5,1,'ATRH 4',1,1,1,1)
                self.zero_one_Index('ATRH4')
        elif text == 'Display All':
                print('ATRH_All')
                self.zero_one_Index('ATRH_All')

#Battery Plot Linear Displacement

   def Battery_LinearDisplacement(self, text):
        if text == 'Displacement 1':
                self.configure_Battery_Plot_LinearDisplacement(1,5,1,'Displacement 1',1,1,1,1)
                self.zero_one_Index('LD1')
        elif text == 'Displacement 2':
                self.configure_Battery_Plot_LinearDisplacement(2,5,1,'Displacement 2',1,1,1,1)
                self.zero_one_Index('LD2')
        elif text == 'Displacement 3':
                self.configure_Battery_Plot_LinearDisplacement(3,5,1,'Displacement 3',1,1,1,1)
                self.zero_one_Index('LD3')
        elif text == 'Displacement 4':
                self.configure_Battery_Plot_LinearDisplacement(4,5,1,'Displacement 4',1,1,1,1)
                self.zero_one_Index('LD4')
        elif text == 'Display All':
                self.configure_Battery_Plot_LinearDisplacement(1,5,1,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,1,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,1,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,1,'Displacement 4',1,1,1,1)
                self.zero_one_Index('LD_All')

#Battery Plot Strain Gauge

   def Battery_FrameStrainGauge(self, text):
        if text == 'FSG 1':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,1,'FSG 1',1,1,1,1)
                self.zero_one_Index('FSG1')
        elif text == 'FSG 2':
                self.configure_Battery_Plot_FrameStrainGauge(2,5,1,'FSG 2',1,1,1,1)
                self.zero_one_Index('FSG2')
        elif text == 'FSG 3':
                self.configure_Battery_Plot_FrameStrainGauge(2,5,1,'FSG 3',1,1,1,1)
                self.zero_one_Index('FSG3')
        elif text == 'FSG 4':
                self.configure_Battery_Plot_FrameStrainGauge(2,5,1,'FSG 3',1,1,1,1)
                self.zero_one_Index('FSG4')
        elif text == 'Display All':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,1,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,1,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrmaeStrainGauge(3,5,1,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,1,'FSG 4',1,1,1,1)
                self.zero_one_Index('FSG_All')

   def Battery_FrameStrainGauge(self, text):
        if text == 'HSG 1':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 1',1,1,1,1)
                self.zero_one_Index('SG5')
        elif text == 'HSG 2':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 2',1,1,1,1)
                self.zero_one_Index('SG6')
        elif text == 'HSG 3':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 3',1,1,1,1)
                self.zero_one_Index('SG7')
        elif text == 'HSG 4':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 4',1,1,1,1)
                self.zero_one_Index('SG8')
        elif text == 'HSG 5':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 5',1,1,1,1)
                self.zero_one_Index('SG9')
        elif text == 'HSG 6':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 6',1,1,1,1)
                self.zero_one_Index('SG10')
        elif text == 'HSG 7':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 7',1,1,1,1)
                self.zero_one_Index('SG11')
        elif text == 'HSG 8':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 8',1,1,1,1)
                self.zero_one_Index('SG12')    
        elif text == 'HSG 9':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 9',1,1,1,1)
                self.zero_one_Index('SG13')
        elif text == 'HSG 10':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 10',1,1,1,1)
                self.zero_one_Index('SG14')
        elif text == 'HSG 11':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 11',1,1,1,1)
                self.zero_one_Index('SG15')
        elif text == 'HSG 12':
                self.configure_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 12',1,1,1,1)
                self.zero_one_Index('SG16')     
        elif text == 'Display All':
                self.configure_Battery_HangerStrainGauge(2,5,1,'HSG 1',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,1,'HSG 2',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,1,'HSG 3',1,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 4',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,1,'HSG 5',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,1,'HSG 6',1,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 7',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,1,'HSG 8',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,1,'HSG 9',1,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 10',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,1,'HSG 11',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,1,'HSG 12',1,1,1,1)
                self.zero_one_Index('HSG_All')


#Battery Plot Temperatur Material

   def Battery_TM(self, text):
        if text == 'Thermistor 1':
                self.configure_Battery_Plot_Temperatur_Material(1,5,1,'Thermistor 1',1,1,1,1)
                self.zero_one_Index('TM1')
        elif text == 'Thermistor 2':
                self.configure_Battery_Plot_Temperatur_Material(2,5,1,'Thermistor 2',1,1,1,1)
                self.zero_one_Index('TM2')
        elif text == 'Display All':
                self.configure_Battery_Plot_Temperatur_Material(1,5,1,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,1,'Thermistor 2',0,1,2,1)
                self.zero_one_Index('TM_All')

#========================================================================================================================================================================

   def zero_one_Index(self, text):
        for key in self.Index:
                self.Index[key]=0
                if key == text:
                        self.Index[key] = 1
        return(self.Index)


#========================================Configure Live Plot Sensor====================================== 

   def TimeRange_Live_Plot(self, text):
        if self.Index['ATRH1']==1:
                self.Live_Plot_Time_ATRH(1,text,'ATRH 1')
        elif self.Index['ATRH2']==1:
                self.Live_Plot_Time_ATRH(2,text,'ATRH 2')
        elif self.Index['ATRH3']==1:
                self.Live_Plot_Time_ATRH(3,text,'ATRH 3')
        elif self.Index['ATRH4']==1:
                self.Live_Plot_Time_ATRH(4,text,'ATRH 4')
        elif self.Index['LD1']==1:
                self.Live_Plot_Time_LinearDisplacement(1,text,'Displacement 1')
        elif self.Index['LD2']==1:
                self.Live_Plot_Time_LinearDisplacement(2,text,'Displacement 2')
        elif self.Index['LD3']==1:
                self.Live_Plot_Time_LinearDisplacement(3,text,'Displacement 3')
        elif self.Index['LD4']==1:
                self.Live_Plot_Time_LinearDisplacement(4,text,'Displacement 4')
        elif self.Index['LD_All']==1:
                self.Live_Plot_Time_Multi_LinearDisplacement(text)
        elif self.Index['FSG1']==1:
                self.Live_Plot_Time_FrameStrainGauge(1,text,'FSG 1')
        elif self.Index['FSG2']==1:
                self.Live_Plot_Time_FrameStrainGauge(2,text,'FSG 2')
        elif self.Index['FSG3']==1:
                self.Live_Plot_Time_FrameStrainGauge(3,text,'FSG 3')
        elif self.Index['FSG4']==1:
                self.Live_Plot_Time_FrameStrainGauge(4,text,'FSG 4')
        elif self.Index['FSG_All']==1:
                self.Live_Plot_Time_Multi_FrameStrainGauge(text)
        elif self.Index['HSG1']==1:
                self.Live_Plot_Time_HangerStrainGauge(1,text,'HSG 1')
        elif self.Index['HSG2']==1:
                self.Live_Plot_Time_HangerStrainGauge(2,text,'HSG 2')
        elif self.Index['HSG3']==1:
                self.Live_Plot_Time_HangerStrainGauge(3,text,'HSG 3')
        elif self.Index['HSG4']==1:
                self.Live_Plot_Time_HangerStrainGauge(4,text,'HSG 4')
        elif self.Index['HSG5']==1:
                self.Live_Plot_Time_HangerStrainGauge(1,text,'HSG 5')
        elif self.Index['HSG6']==1:
                self.Live_Plot_Time_HangerStrainGauge(2,text,'HSG 6')
        elif self.Index['HSG7']==1:
                self.Live_Plot_Time_HangerStrainGauge(3,text,'HSG 7')
        elif self.Index['HSG8']==1:
                self.Live_Plot_Time_HangerStrainGauge(4,text,'HSG 8')
        elif self.Index['HSG9']==1:
                self.Live_Plot_Time_HangerStrainGauge(1,text,'HSG 9')
        elif self.Index['HSG10']==1:
                self.Live_Plot_Time_HangerStrainGauge(2,text,'HSG 10')
        elif self.Index['HSG11']==1:
                self.Live_Plot_Time_HangerStrainGauge(3,text,'HSG 11')
        elif self.Index['HSG12']==1:
                self.Live_Plot_Time_HangerStrainGauge(4,text,'HSG 12')
        elif self.Index['HSG_All']==1:
                self.Live_Plot_Time_Multi_HangerStrainGauge(text)
        elif self.Index['TM1']==1:
                self.Live_Plot_Time_TemperaturMaterial(1,text,'Thermistor 1')
        elif self.Index['TM2']==1:
                self.Live_Plot_Time_TemperaturMaterial(2,text,'Thermistor 2')
        elif self.Index['TM_All']==1:
                self.Live_Plot_Time_Multi_TemperaturMaterial(text)

   def Live_Plot_Time_ATRH(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Live_Plot_ATRH(ID,5,1,tittle)
        elif text == '15 minutes':
                self.configure_Live_Plot_ATRH(ID,5,3,tittle)
        elif text == '30 minutes':
                self.configure_Live_Plot_ATRH(ID,5,6,tittle)
        elif text == '1 hour':
                self.configure_Live_Plot_ATRH(ID,5,12,tittle)
        elif text == '4 hours':
                self.configure_Live_Plot_ATRH(ID,5,48,tittle)
        elif text == '12 hours':
                self.configure_Live_Plot_ATRH(ID,5,144,tittle)
        elif text == '1 day':
                self.configure_Live_Plot_ATRH(ID,5,288,tittle)

   def Live_Plot_Time_LinearDisplacement(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Live_Plot_LinearDisplacement(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_LinearDisplacement(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_LinearDisplacement(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_LinearDisplacement(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Live_Plot_LinearDisplacement(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Live_Plot_LinearDisplacement(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_LinearDisplacement(ID,5,288,tittle,1,1,1,1)

   def Live_Plot_Time_FrameStrainGauge(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_FrameStrainGauge(ID,5,288,tittle,1,1,1,1)

   def Live_Plot_Time_StrainStrainGauge(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_HangerStrainGauge(ID,5,288,tittle,1,1,1,1)

   def Live_Plot_Time_TemperaturMaterial(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Live_Plot_Temperatur_Material(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_Temperatur_Material(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_Temperatur_Material(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_Temperatur_Material(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Live_Plot_Temperatur_Material(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Live_Plot_Temperatur_Material(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_Temperatur_Material(ID,5,288,tittle,1,1,1,1)


   def Live_Plot_Time_Multi_LinearDisplacement(self, text):
        if text == '5 minutes':
                self.configure_Live_Plot_LinearDisplacement(1,5,1,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,1,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,1,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,1,'Displacement 4',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_LinearDisplacement(1,5,3,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,3,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,3,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,3,'Displacement 4',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_LinearDisplacement(1,5,6,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,6,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,6,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,6,'Displacement 4',1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_LinearDisplacement(1,5,12,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,12,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,12,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,12,'Displacement 4',1,1,1,1)
        elif text == '4 hour':
                self.configure_Live_Plot_LinearDisplacement(1,5,48,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,48,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,48,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,48,'Displacement 4',1,1,1,1)
        elif text == '12 hour':
                self.configure_Live_Plot_LinearDisplacement(1,5,144,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,144,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,144,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,144,'Displacement 4',1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_LinearDisplacement(1,5,288,'Displacement 1',0,0,1,1)
                self.add_Live_Plot_LinearDisplacement(2,5,288,'Displacement 2',0,1,1,1)
                self.add_Live_Plot_LinearDisplacement(3,5,288,'Displacement 3',1,0,1,1)
                self.add_Live_Plot_LinearDisplacement(4,5,288,'Displacement 4',1,1,1,1)

   def Live_Plot_Time_Multi_FrameStrainGauge(self, text):
        if text == '5 minutes':
                self.configure_Live_Plot_FrameStrainGauge(1,5,1,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,1,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,1,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,1,'FSG 4',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_FrameStrainGauge(1,5,3,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,3,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,3,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,3,'FSG 4',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_FrameStrainGauge(1,5,6,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,6,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,6,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,6,'FSG 4',1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_FrameStrainGauge(1,5,12,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,12,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,12,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,12,'FSG 4',1,1,1,1)
        elif text == '4 hour':
                self.configure_Live_Plot_FrameStrainGauge(1,5,48,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,48,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,48,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,48,'FSG 4',1,1,1,1)
        elif text == '12 hour':
                self.configure_Live_Plot_FrameStrainGauge(1,5,144,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,144,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,144,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,144,'FSG 4',1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_FrameStrainGauge(1,5,288,'FSG 1',0,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(2,5,288,'FSG 2',0,1,1,1)
                self.add_Live_Plot_FrameStrainGauge(3,5,288,'FSG 3',1,0,1,1)
                self.add_Live_Plot_FrameStrainGauge(4,5,288,'FSG 4',1,1,1,1)

   def Live_Plot_Time_Multi_HangerStrainGauge(self, text):
        if text == '5 minutes':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)
        elif text == '1 hour':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)
        elif text == '4 hour':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)
        elif text == '12 hour':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)
        elif text == '1 day':
                self.configure_Live_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(5,5,1,'HSG 5',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(6,5,1,'HSG 6',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(7,5,1,'HSG 7',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(8,5,1,'HSG 8',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(9,5,1,'HSG 9',1,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(10,5,1,'HSG 10',0,1,1,1)
                self.add_Live_Plot_HangerStrainGauge(11,5,1,'HSG 11',1,0,1,1)
                self.add_Live_Plot_HangerStrainGauge(12,5,1,'HSG 12',1,1,1,1)

   def Live_Plot_Time_Multi_TemperaturMaterial(self, text):
        if text == '5 minutes':
                self.configure_Live_Plot_Temperatur_Material(1,5,1,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,1,'Thermistor 2',0,1,2,1)
        elif text == '15 minutes':
                self.configure_Live_Plot_Temperatur_Material(1,5,3,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,3,'Thermistor 2',0,1,2,1)
        elif text == '30 minutes':
                self.configure_Live_Plot_Temperatur_Material(1,5,6,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,6,'Thermistor 2',0,1,2,1)
        elif text == '1 hour':
                self.configure_Live_Plot_Temperatur_Material(1,5,12,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,12,'Thermistor 2',0,1,2,1)
        elif text == '4 hour':
                self.configure_Live_Plot_Temperatur_Material(1,5,48,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,48,'Thermistor 2',0,1,2,1)
        elif text == '12 hour':
                self.configure_Live_Plot_Temperatur_Material(1,5,144,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,144,'Thermistor 2',0,1,2,1)
        elif text == '1 day':
                self.configure_Live_Plot_Temperatur_Material(1,5,288,'Thermistor 1',0,0,2,1)
                self.add_Live_Plot_TemperaturMaterial(2,5,288,'Thermistor 2',0,1,2,1)


   def configure_Live_Plot_ATRH(self, ID, N_data, step, tittle):
        for i in reversed(range(self.Live_Plot_Layout.count())):
                self.Live_Plot_Layout.itemAt(i).widget().setParent(None)
        self.add_Live_Plot_ATRH_Temperatur(ID, N_data, step, tittle,1,0,1,1)
        self.add_Live_Plot_ATRH_Humidity(ID, N_data, step, tittle,0,0,1,1)
        self.add_Live_Plot_ATRH_Pressure(ID, N_data, step, tittle,0,1,2,1)
        
   def configure_Live_Plot_LinearDisplacement(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Live_Plot_Layout.count())):
                self.Live_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Plot_LinearDisplacement(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Live_Plot_FrameStrainGauge(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Live_Plot_Layout.count())):
                self.Live_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Plot_StrainGauge(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Live_Plot_HangerStrainGauge(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Live_Plot_Layout.count())):
                self.Live_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Plot_StrainGauge(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Live_Plot_Temperatur_Material(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Live_Plot_Layout.count())):
                self.Live_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Plot_TemperaturMaterial(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)



   def add_Live_Plot_ATRH_Temperatur(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2, cor_3):
        self.plot = Live_Plot_ATRH(self.Live_Plot_Widget)
        self.plot.ubah_Parameter_Temperatur(ID, N_data, step, tittle)
        self.plot.update_figure_Temperatur(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)
   def add_Live_Plot_ATRH_Humidity(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2, cor_3):
        self.plot = Live_Plot_ATRH(self.Live_Plot_Widget)
        self.plot.ubah_Parameter_Humidity(ID, N_data, step, tittle)
        self.plot.update_figure_Humidity(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)
   def add_Live_Plot_ATRH_Pressure(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2, cor_3):
        self.plot = Live_Plot_ATRH(self.Live_Plot_Widget)
        self.plot.ubah_Parameter_Pressure(ID, N_data, step, tittle)
        self.plot.update_figure_Pressure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def add_Live_Plot_LinearDisplacement(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Plot_LinearDisplacement(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Live_Plot_FrameStrainGauge(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Plot_StrainGauge(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Live_Plot_HangerStrainGauge(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Plot_StrainGauge(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Live_Plot_TemperaturMaterial(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Plot_TemperaturMaterial(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

#====================================================Configure History Plot======================================
   
   def SetHistory(self):
    
        time_begin = self.Begin_Time.time().toString()
        time_end = self.End_Time.time().toString()

        date_begin = self.Begin_Date.date().toString()
        date_begin = date_begin.split(' ')

        self.configure_date(date_begin)
        
        datetime_begin = date_begin[3]+'-'+date_begin[1]+'-'+date_begin[2]+' '+time_begin
        datetime_begin = str(datetime_begin)
        
        date_end = self.End_Date.date().toString()
        date_end = date_end.split(' ')

        self.configure_date(date_end)
    
        datetime_end = date_end[3]+'-'+date_end[1]+'-'+date_end[2]+' '+time_end
        datetime_end = str(datetime_end)

        if self.Index['ATRH1'] == 1:
            self.configure_HistoryPlot_ATRH(1, datetime_begin, datetime_end, 1, 'ATRH 1',1,1,1,1)
        elif self.Index['ATRH2'] == 1:
            self.configure_HistoryPlot_ATRH(2,datetime_begin,datetime_end,1,'ATRH 2',1,1,1,1)
        elif self.Index['ATRH3'] == 1:
            self.configure_HistoryPlot_ATRH(3,datetime_begin,datetime_end,1,'ATRH 3',1,1,1,1)
        elif self.Index['ATRH4'] == 1:
            self.configure_HistoryPlot_ATRH(4,datetime_begin,datetime_end,1,'ATRH 4',1,1,1,1)
        elif self.Index['LD1'] == 1:
            self.configure_HistoryPlot_LinearDisplacement(1,datetime_begin,datetime_end,1,'Displacement 1',1,1,1,1)
        elif self.Index['LD2'] == 1:
            self.configure_HistoryPlot_LinearDisplacement(2,datetime_begin,datetime_end,1,'Displacement 2',1,1,1,1)
        elif self.Index['LD3'] == 1:
            self.configure_HistoryPlot_LinearDisplacement(3,datetime_begin,datetime_end,1,'Displacement 3',1,1,1,1)
        elif self.Index['LD4'] == 1:
            self.configure_HistoryPlot_LinearDisplacement(4,datetime_begin,datetime_end,1,'Displacement 4',1,1,1,1)
        elif self.Index['FSG1'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(1,datetime_begin,datetime_end,1,'FSG 1',1,1,1,1)
        elif self.Index['FSG2'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(2,datetime_begin,datetime_end,1,'FSG 2',1,1,1,1)
        elif self.Index['FSG3'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(3,datetime_begin,datetime_end,1,'FSG 3',1,1,1,1)
        elif self.Index['FSG4'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(4,datetime_begin,datetime_end,1,'FSG 4',1,1,1,1)
        elif self.Index['HSG1'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(1,datetime_begin,datetime_end,1,'HSG 1',1,1,1,1)
        elif self.Index['HSG2'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(2,datetime_begin,datetime_end,1,'HSG 2',1,1,1,1)
        elif self.Index['HSG3'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(3,datetime_begin,datetime_end,1,'HSG 3',1,1,1,1)
        elif self.Index['HSG4'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(4,datetime_begin,datetime_end,1,'HSG 4',1,1,1,1)        
        elif self.Index['HSG5'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(1,datetime_begin,datetime_end,1,'HSG 5',1,1,1,1)
        elif self.Index['HSG6'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(2,datetime_begin,datetime_end,1,'HSG 6',1,1,1,1)
        elif self.Index['HSG7'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(3,datetime_begin,datetime_end,1,'HSG 7',1,1,1,1)
        elif self.Index['HSG8'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(4,datetime_begin,datetime_end,1,'HSG 8',1,1,1,1)        
        elif self.Index['HSG9'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(1,datetime_begin,datetime_end,1,'HSG 9',1,1,1,1)
        elif self.Index['HSG10'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(2,datetime_begin,datetime_end,1,'HSG 10',1,1,1,1)
        elif self.Index['HSG11'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(3,datetime_begin,datetime_end,1,'HSG 11',1,1,1,1)
        elif self.Index['HSG12'] == 1:
            self.configure_HistoryPlot_FrameStrainGauge(4,datetime_begin,datetime_end,1,'HSG 12',1,1,1,1)                        
        elif self.Index['TM1'] == 1:
            self.configure_HistoryPlot_TemperaturMaterial(1,datetime_begin,datetime_end,1,'Thermistor 1',1,1,1,1)
        elif self.Index['TM2'] == 1:
            self.configure_HistoryPlot_TemperaturMaterial(2,datetime_begin,datetime_end,1,'Thermistor 2',1,1,1,1)
   
   def configure_date(self, date):
        if date[1] =='Jan':
            date[1] = str('01')
        elif date[1] == 'Feb':
            date[1] = str('02')
        elif date[1] == 'Mar':
            date[1] = str('03')
        elif date[1] == 'Apr':
            date[1] = str('04')
        elif date[1] == 'Mei':
            date[1] = str('05')
        elif date[1] == 'Jun':
            date[1] = str('06')
        elif date[1] == 'Jul':
            date[1] = str('07')
        elif date[1] == 'Agu':
            date[1] = str('08')
        elif date[1] == 'Sep':
            date[1] = str('09')
        elif date[1] == 'Okt':
            date[1] = str('10')
        elif date[1] == 'Nov':
            date[1] = str('11')
        else:
            date[1] = str('12')

        if date[2] =='1':
            date[2] = str('01')
        elif date[2] == '2':
            date[2] = str('02')
        elif date[2] == '3':
            date[2] = str('03')
        elif date[2] == '4':
            date[2] = str('04')
        elif date[2] == '5':
            date[2] = str('05')
        elif date[2] == '6':
            date[2] = str('06')
        elif date[2] == '7':
            date[2] = str('07')
        elif date[2] == '8':
            date[2] = str('08')
        elif date[2] == '9':
            date[2] = str('09')
  
  
  
  
  
   def configure_HistoryPlot_ATRH(self,ID,date_begin,date_end,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.History_Plot_Layout.count())): 
                self.History_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Static_Plot_ATRH(self.History_Plot_Widget)
        self.plot.ubah_Parameter_Static_Temp(ID, date_begin, date_end, step, title)
        self.plot.update_figure_static_Temp(ID,date_begin,date_end,step,title)
        self.History_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_HistoryPlot_LinearDisplacement(self,ID,date_begin,date_end,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.History_Plot_Layout.count())): 
                self.History_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Static_Plot_LinearDisplacement(self.History_Plot_Widget)
        self.plot.ubah_Parameter_Static(ID, date_begin, date_end, step, title)
        self.plot.update_figure_static(ID,date_begin,date_end,step,title)
        self.History_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_HistoryPlot_FrameStrainGauge(self,ID,date_begin,date_end,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.History_Plot_Layout.count())): 
                self.History_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Static_Plot_StrainGauge(self.History_Plot_Widget)
        self.plot.ubah_Parameter_Static(ID, date_begin, date_end, step, title)
        self.plot.update_figure_static(ID,date_begin,date_end,step,title)
        self.History_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_HistoryPlot_HangerStrainGauge(self,ID,date_begin,date_end,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.History_Plot_Layout.count())): 
                self.History_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Static_Plot_StrainGauge(self.History_Plot_Widget)
        self.plot.ubah_Parameter_Static(ID, date_begin, date_end, step, title)
        self.plot.update_figure_static(ID,date_begin,date_end,step,title)
        self.History_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_HistoryPlot_TemperaturMaterial(self,ID,date_begin,date_end,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.History_Plot_Layout.count())): 
                self.History_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Static_Plot_TemperaturMaterial(self.History_Plot_Widget)
        self.plot.ubah_Parameter_Static(ID, date_begin, date_end, step, title)
        self.plot.update_figure_static(ID,date_begin,date_end,step,title)
        self.History_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)
  
  
  

        

#====================================================Configure Battery Plot=======================================
   def TimeRange_Battery_Plot(self, text):
        if self.Index['ATRH1']==1:
                self.Battery_Plot_Time_ATRH(1,text,'ATRH 1')
        elif self.Index['ATRH2']==1:
                self.Battery_Plot_Time_ATRH(2,text,'ATRH 2')
        elif self.Index['ATRH3']==1:
                self.Battery_Plot_Time_ATRH(3,text,'ATRH 3')
        elif self.Index['ATRH4']==1:
                self.Battery_Plot_Time_ATRH(4,text,'ATRH 4')
        elif self.Index['ATRH_All']==1:
                self.Battery_Plot_Time_Multi_ATRH(text)
        elif self.Index['LD1']==1:
                self.Battery_Plot_Time_LinearDisplacement(1,text,'Displacement 1')
        elif self.Index['LD2']==1:
                self.Battery_Plot_Time_LinearDisplacement(2,text,'Displacement 2')
        elif self.Index['LD3']==1:
                self.Battery_Plot_Time_LinearDisplacement(3,text,'Displacement 3')
        elif self.Index['LD4']==1:
                self.Battery_Plot_Time_LinearDisplacement(4,text,'Displacement 4')
        elif self.Index['LD_All']==1:
                self.Battery_Plot_Time_Multi_LinearDisplacement(text)
        elif self.Index['TM1']==1:
                self.Battery_Plot_Time_TemperaturMaterial(1,text,'Thermistor 1')
        elif self.Index['TM2']==1:
                self.Battery_Plot_Time_TemperaturMaterial(2,text,'Thermistor 2')
        elif self.Index['TM_All']==1:
                self.Battery_Plot_Time_Multi_TemperaturMaterial(text)

   def Battery_Plot_Time_ATRH(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Battery_Plot_ATRH(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_ATRH(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_ATRH(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_ATRH(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Battery_Plot_ATRH(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Battery_Plot_ATRH(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_ATRH(ID,5,288,tittle,1,1,1,1)

   def Battery_Plot_Time_LinearDisplacement(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_LinearDisplacement(ID,5,288,tittle,1,1,1,1)

   def Battery_Plot_Time_FrameStrainGauge(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_FrameStrainGauge(ID,5,288,tittle,1,1,1,1)

   def Battery_Plot_Time_HangerStrainGauge(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_HangerStrainGauge(ID,5,288,tittle,1,1,1,1)

   def Battery_Plot_Time_TemperaturMaterial(self, ID, text, tittle):
        if text == '5 minutes':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,1,tittle,1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,3,tittle,1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,6,tittle,1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,12,tittle,1,1,1,1)
        elif text == '4 hours':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,48,tittle,1,1,1,1)
        elif text == '12 hours':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,144,tittle,1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_Temperatur_Material(ID,5,288,tittle,1,1,1,1)

   def Battery_Plot_Time_Multi_ATRH(self, text):
        if text == '5 minutes':
                self.configure_Battery_Plot_ATRH(1,5,1,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,1,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,1,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,1,'ATRH 4',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_ATRH(1,5,3,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,3,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,3,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,3,'ATRH 4',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_ATRH(1,5,6,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,6,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,6,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,6,'ATRH 4',1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_ATRH(1,5,12,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,12,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,12,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,12,'ATRH 4',1,1,1,1)
        elif text == '4 hour':
                self.configure_Battery_Plot_ATRH(1,5,48,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,48,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,48,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,48,'ATRH 4',1,1,1,1)
        elif text == '12 hour':
                self.configure_Battery_Plot_ATRH(1,5,144,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,144,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,144,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,144,'ATRH 4',1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_ATRH(1,5,288,'ATRH 1',0,0,1,1)
                self.add_Battery_Plot_ATRH(2,5,288,'ATRH 2',0,1,1,1)
                self.add_Battery_Plot_ATRH(3,5,288,'ATRH 3',1,0,1,1)
                self.add_Battery_Plot_ATRH(4,5,288,'ATRH 4',1,1,1,1)

   def Battery_Plot_Time_Multi_LinearDisplacement(self, text):
        if text == '5 minutes':
                self.configure_Battery_Plot_LinearDisplacement(1,5,1,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,1,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,1,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,1,'Displacement 4',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_LinearDisplacement(1,5,3,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,3,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,3,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,3,'Displacement 4',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_LinearDisplacement(1,5,6,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,6,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,6,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,6,'Displacement 4',1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_LinearDisplacement(1,5,12,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,12,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,12,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,12,'Displacement 4',1,1,1,1)
        elif text == '4 hour':
                self.configure_Battery_Plot_LinearDisplacement(1,5,48,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,48,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,48,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,48,'Displacement 4',1,1,1,1)
        elif text == '12 hour':
                self.configure_Battery_Plot_LinearDisplacement(1,5,144,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,144,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,144,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,144,'Displacement 4',1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_LinearDisplacement(1,5,288,'Displacement 1',0,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(2,5,288,'Displacement 2',0,1,1,1)
                self.add_Battery_Plot_LinearDisplacement(3,5,288,'Displacement 3',1,0,1,1)
                self.add_Battery_Plot_LinearDisplacement(4,5,288,'Displacement 4',1,1,1,1)

   def Battery_Plot_Time_Multi_FrameStrainGauge(self, text):
        if text == '5 minutes':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,1,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,1,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,1,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,1,'FSG 4',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,3,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,3,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,3,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,3,'FSG 4',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,6,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,6,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,6,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,6,'FSG 4',1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,12,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,12,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,12,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,12,'FSG 4',1,1,1,1)
        elif text == '4 hour':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,48,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,48,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,48,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,48,'FSG 4',1,1,1,1)
        elif text == '12 hour':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,144,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,144,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,144,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,144,'FSG 4',1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_FrameStrainGauge(1,5,288,'FSG 1',0,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(2,5,288,'FSG 2',0,1,1,1)
                self.add_Battery_Plot_FrameStrainGauge(3,5,288,'FSG 3',1,0,1,1)
                self.add_Battery_Plot_FrameStrainGauge(4,5,288,'FSG 4',1,1,1,1)

   def Battery_Plot_Time_Multi_HangerStrainGauge(self, text):
        if text == '5 minutes':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,1,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,1,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,1,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,1,'HSG 4',1,1,1,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,3,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,3,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,3,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,3,'HSG 4',1,1,1,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,6,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,6,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,6,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,6,'HSG 4',1,1,1,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,12,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,12,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,12,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,12,'HSG 4',1,1,1,1)
        elif text == '4 hour':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,48,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,48,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,48,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,48,'HSG 4',1,1,1,1)
        elif text == '12 hour':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,144,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,144,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,144,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,144,'HSG 4',1,1,1,1)
        elif text == '1 day':
                self.configure_Battery_Plot_HangerStrainGauge(1,5,288,'HSG 1',0,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(2,5,288,'HSG 2',0,1,1,1)
                self.add_Battery_Plot_HangerStrainGauge(3,5,288,'HSG 3',1,0,1,1)
                self.add_Battery_Plot_HangerStrainGauge(4,5,288,'HSG 4',1,1,1,1)

   def Battery_Plot_Time_Multi_TemperaturMaterial(self, text):
        if text == '5 minutes':
                self.configure_Battery_Plot_Temperatur_Material(1,5,1,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,1,'Thermistor 2',0,1,2,1)
        elif text == '15 minutes':
                self.configure_Battery_Plot_Temperatur_Material(1,5,3,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,3,'Thermistor 2',0,1,2,1)
        elif text == '30 minutes':
                self.configure_Battery_Plot_Temperatur_Material(1,5,6,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,6,'Thermistor 2',0,1,2,1)
        elif text == '1 hour':
                self.configure_Battery_Plot_Temperatur_Material(1,5,12,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,12,'Thermistor 2',0,1,2,1)
        elif text == '4 hour':
                self.configure_Battery_Plot_Temperatur_Material(1,5,48,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,48,'Thermistor 2',0,1,2,1)
        elif text == '12 hour':
                self.configure_Battery_Plot_Temperatur_Material(1,5,144,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,144,'Thermistor 2',0,1,2,1)
        elif text == '1 day':
                self.configure_Battery_Plot_Temperatur_Material(1,5,288,'Thermistor 1',0,0,2,1)
                self.add_Battery_Plot_TemperaturMaterial(2,5,288,'Thermistor 2',0,1,2,1)


   def configure_Battery_Plot_ATRH(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Battery_Plot_Layout.count())):
                self.Battery_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Battery_Plot_ATRH(self.Battery_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Battery_Plot_LinearDisplacement(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Battery_Plot_Layout.count())):
                self.Battery_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Battery_Plot_LinearDisplacement(self.Battery_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Battery_Plot_FrameStrainGauge(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Battery_Plot_Layout.count())):
                self.Battery_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Battery_Plot_StrainGauge(self.Battery_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Battery_Plot_HangerStrainGauge(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Battery_Plot_Layout.count())):
                self.Battery_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Battery_Plot_StrainGauge(self.Battery_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

   def configure_Battery_Plot_Temperatur_Material(self, ID, N_data, step, tittle, cor_0, cor_1, cor_2, cor_3):
        for i in reversed(range(self.Battery_Plot_Layout.count())):
                self.Battery_Plot_Layout.itemAt(i).widget().setParent(None)
        
        self.plot = Live_Battery_Plot_TemperaturMaterial(self.Battery_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)



   def add_Battery_Plot_ATRH(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Battery_Plot_ATRH(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Battery_Plot_LinearDisplacement(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Battery_Plot_LinearDisplacement(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Battery_Plot_FrameStrainGauge(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Battery_Plot_StrainGauge(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Battery_Plot_HangerStrainGauge(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Battery_Plot_StrainGauge(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

   def add_Battery_Plot_TemperaturMaterial(self, ID, N_data, step, tittle, cor_0,cor_1,cor_2,cor_3):
        self.plot = Live_Battery_Plot_TemperaturMaterial(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID, N_data, step, tittle)
        self.plot.update_figure(ID, N_data, step, tittle)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0,cor_1,cor_2, cor_3)

#=====================================================================================================================================================================


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

