
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Accesing_Data_Sensor_API_Rumpiang import AccesLiveData_API, AccesHistoryData_API



class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)
    def compute_initial_figure(self):
        pass


class Live_Plot_ATRH(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter_Temperatur(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_Temperatur(self.ID, self.N_data, self.step, self.title))
        timer.start(60000)
    
    def ubah_Parameter_Humidity(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_Humidity(self.ID, self.N_data, self.step, self.title))
        timer.start(60000)

    def ubah_Parameter_Pressure(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_Pressure(self.ID, self.N_data, self.step, self.title))
        timer.start(60000)

    def update_figure_Temperatur(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_ATRH()
        l = data[1]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Temperatur [°C]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()
    
    def update_figure_Humidity(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_ATRH()
        l = data[2]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Humidity [%]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

    def update_figure_Pressure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_ATRH()
        l = data[3]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Pressure [Pa]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

class Live_Plot_LinearDisplacement(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(60000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_LinearDisplacement()
        l = data[1]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Displacement [mm]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

class Live_Plot_StrainGauge(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(60000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_StrainGauge()
        l = data[1]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Strain [μS]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

class Live_Plot_TemperaturMaterial(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(12000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_TemperaturMaterial()
        l = data[1]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Temperatur [°C]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()


class Live_Battery_Plot_ATRH(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(60000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_ATRH()
        l = data[4]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Voltage [V]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

class Live_Battery_Plot_LinearDisplacement(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(12000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_LinearDisplacement()
        l = data[2]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Voltage [V]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

class Live_Battery_Plot_StrainGauge(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(12000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_StrainGauge()
        l = data[2]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Voltage [V]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()

class Live_Battery_Plot_TemperaturMaterial(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(12000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData_API(ID,N_data,step).Acces_TemperaturMaterial()
        l = data[2]
        a = data[0]
        a.reverse()
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Voltage [V]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.axes.set_xticklabels(a, rotation=45)
        self.draw()


class Static_Plot_ATRH(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter_Static_Temp(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static_Temp(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
    
    def ubah_Parameter_Static_Hum(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static_Hum(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
    
    def ubah_Parameter_Static_Press(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static_Press(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
        
    def update_figure_static_Temp(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData_API(ID, date_begin, date_end, step).Acces_ATRH()
        l = data[1]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Temperatur [°C]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.axes.set_xticklabels(a, rotation=90)
        self.draw()
    
    def update_figure_static_Hum(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData_API(ID, date_begin, date_end, step).Acces_ATRH()
        l = data[2]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Humidity [%]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.axes.set_xticklabels(a, rotation=90)
        self.draw()
    
    def update_figure_static_Press(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData_API(ID, date_begin, date_end, step).Acces_ATRH()
        l = data[3]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Pressure [Pa]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.axes.set_xticklabels(a, rotation=90)
        self.draw()

class Static_Plot_LinearDisplacement(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter_Static(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
        
    def update_figure_static(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData_API(ID, date_begin, date_end, step).Acces_LinearDisplacement()
        l = data[1]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Displacement [mm]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.axes.set_xticklabels(a, rotation=90)
        self.draw()
        

class Static_Plot_StrainGauge(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter_Static(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
        
    def update_figure_static(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData_API(ID, date_begin, date_end, step).Acces_StrainGauge()
        l = data[1]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Strain [μS]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.axes.set_xticklabels(a, rotation=90)
        self.draw()

class Static_Plot_TemperaturMaterial(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter_Static(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
        
    def update_figure_static(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData_API(ID, date_begin, date_end, step).Acces_TemperaturMaterial()
        l = data[1]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Temperatur [°C]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.axes.set_xticklabels(a, rotation=90)
        self.draw()
