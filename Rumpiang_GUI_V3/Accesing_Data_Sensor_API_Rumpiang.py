import requests
import datetime

#==== Thermistor Saint Gobain =======
class AccesLiveData_API():

    def __init__(self, ID, N_data, step):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        
    def Acces_ATRH(self):

        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID)
        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        current_date_Time = current_date_Time - datetime.timedelta(minutes = current_date_Time.minute%5)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data[0]": 'data0',
            "data[1]": 'data1',
            "data[2]": 'data2',
            "data[3]": 'battery',
            "options[filterTime]": c_str_datetime,
            "options[filterNumberBefore]": self.N_data,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        Humidity = []
        Pressure = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=(5*self.step*x)) for x in range(self.N_data)]

        for j in range(len(datetime_list)):
            datetime_ = datetime_list[j].strftime("%Y-%m-%d %H:%M:%S")
            datetime_ = datetime_.split(' ')
            datetime_ = datetime_[1]
            time.append(datetime_)

        for i in range(len(range(self.N_data))):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)
            Humidity_plot = float(Data_json['data'][i]['data1'])
            Humidity.append(Humidity_plot)
            Pressure_plot = float(Data_json['data'][i]['data2'])
            Pressure.append(Pressure_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)
    
        return[time, Temperatur, Humidity, Pressure, battery]

    def Acces_LinearDisplacement(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID+8)

        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        current_date_Time = current_date_Time - datetime.timedelta(minutes = current_date_Time.minute%5)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data[0]": 'data0',
            "data[1]": 'battery',
            "options[filterTime]": c_str_datetime,
            "options[filterNumberBefore]": self.N_data,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Displacement = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=(5*self.step*x)) for x in range(self.N_data)]
        for j in range(len(datetime_list)):
            datetime_ = datetime_list[j].strftime("%Y-%m-%d %H:%M:%S")
            datetime_ = datetime_.split(' ')
            datetime_ = datetime_[1]
            time.append(datetime_)

        for i in range(len(range(self.N_data))):
            Displacement_plot = float(Data_json['data'][i]['data0'])
            Displacement.append(Displacement_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)
        
        return[time, Displacement, battery]

    def Acces_StrainGauge(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID+24)

        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        current_date_Time = current_date_Time - datetime.timedelta(minutes = current_date_Time.minute%5)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data[0]": 'data0',
            "data[1]": 'battery',
            "options[filterTime]": c_str_datetime,
            "options[filterNumberBefore]": self.N_data,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 10 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Strain = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=(5*self.step*x)) for x in range(self.N_data)]
        for j in range(len(datetime_list)):
            datetime_ = datetime_list[j].strftime("%Y-%m-%d %H:%M:%S")
            datetime_ = datetime_.split(' ')
            datetime_ = datetime_[1]
            time.append(datetime_)

        for i in range(len(range(self.N_data))):
            Strain_plot = float(Data_json['data'][i]['data0'])
            Strain.append(Strain_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)
        
        return[time, Strain, battery]

    def Acces_TemperaturMaterial(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID+42)

        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        current_date_Time = current_date_Time - datetime.timedelta(minutes = current_date_Time.minute%5)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data[0]": 'data0',
            "data[1]": 'battery',
            "options[filterTime]": c_str_datetime,
            "options[filterNumberBefore]": self.N_data,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 2 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=(5*self.step*x)) for x in range(self.N_data)]
        for j in range(len(datetime_list)):
            datetime_ = datetime_list[j].strftime("%Y-%m-%d %H:%M:%S")
            datetime_ = datetime_.split(' ')
            datetime_ = datetime_[1]
            time.append(datetime_)

        for i in range(len(range(self.N_data))):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)
        
        return[time, Temperatur, battery]


class AccesHistoryData_API():

    def __init__(self, ID, date_begin, date_end, step):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
    
    def Acces_ATRH(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID)

        data = {
            "data[0]": 'data0',
            "data[1]": 'data1',
            "data[2]": 'data2',
            "data[3]": 'battery',
            "options[filterBegin]": self.date_begin,
            "options[filterEnd]": self.date_end,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        Humidity = []
        Pressure = []
        battery = []

        time_plot = self.date_end

        for i in range(len(Data_json['data'])):
            time_plot = datetime.datetime.strptime(time_plot, "%Y-%m-%d %H:%M:%S")
            time_plot = time_plot - datetime.timedelta(minutes = 5)
            time_plot = time_plot.strftime("%Y-%m-%d %H:%M:%S")
            time.append(time_plot)
        
        for i in range(len(time)): 
            time[i] = time[i].split(' ')
            time[i] = time[i][1]
    
        for i in range(len(Data_json['data'])):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)
            Humidity_plot = float(Data_json['data'][i]['data1'])
            Humidity.append(Humidity_plot)
            Pressure_plot = float(Data_json['data'][i]['data2'])
            Pressure.append(Pressure_plot)
            # time_plot = Data_json['data'][i]['time']
            # time_plot = time_plot.split(' ')
            # time_plot = time_plot[1]
            # time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Temperatur, Humidity, Pressure, battery]

    
    def Acces_LinearDisplacement(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID+8)

        data = {
            "data[0]": 'data0',
            "data[1]": 'battery',
            "options[filterBegin]": self.date_begin,
            "options[filterEnd]": self.date_end,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Displacement = []
        battery = []

        time_plot = self.date_end

        for i in range(len(Data_json['data'])):
            time_plot = datetime.datetime.strptime(time_plot, "%Y-%m-%d %H:%M:%S")
            time_plot = time_plot - datetime.timedelta(minutes = 5)
            time_plot = time_plot.strftime("%Y-%m-%d %H:%M:%S")
            time.append(time_plot)
        
        for i in range(len(time)): 
            time[i] = time[i].split(' ')
            time[i] = time[i][1]
            

        for i in range(len(Data_json['data'])):
            Displacement_plot = float(Data_json['data'][i]['data0'])
            Displacement.append(Displacement_plot)
            # time_plot = Data_json['data'][i]['time']
            # time_plot = time_plot.split(' ')
            # time_plot = time_plot[1]
            # time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Displacement, battery]

    def Acces_StrainGauge(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID+24)

        data = {
            "data[0]": 'data0',
            "data[1]": 'battery',
            "options[filterBegin]": self.date_begin,
            "options[filterEnd]": self.date_end,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 10 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Strain = []
        battery = []

        time_plot = self.date_end

        for i in range(len(Data_json['data'])):
            time_plot = datetime.datetime.strptime(time_plot, "%Y-%m-%d %H:%M:%S")
            time_plot = time_plot - datetime.timedelta(minutes = 5)
            time_plot = time_plot.strftime("%Y-%m-%d %H:%M:%S")
            time.append(time_plot)
        
        for i in range(len(time)): 
            time[i] = time[i].split(' ')
            time[i] = time[i][1]

        for i in range(len(Data_json['data'])):
            Strain_plot = float(Data_json['data'][i]['data0'])
            Strain.append(Strain_plot)
            # time_plot = Data_json['data'][i]['time']
            # time_plot = time_plot.split(' ')
            # time_plot = time_plot[1]
            # time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Strain, battery]
     
    def Acces_TemperaturMaterial(self):
        http = 'http://36.92.138.59/rmcs/data/common/0/101/{}'.format(self.ID+42)

        data = {
            "data[0]": 'data0',
            "data[1]": 'battery',
            "options[filterBegin]": self.date_begin,
            "options[filterEnd]": self.date_end,
            "options[filterStep]": (self.step*300)
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q'
        }

        if self.ID > 2 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, params = data, headers=headers)
        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        battery = []

        time_plot = self.date_end

        for i in range(len(Data_json['data'])):
            time_plot = datetime.datetime.strptime(time_plot, "%Y-%m-%d %H:%M:%S")
            time_plot = time_plot - datetime.timedelta(minutes = 5)
            time_plot = time_plot.strftime("%Y-%m-%d %H:%M:%S")
            time.append(time_plot)
        
        for i in range(len(time)): 
            time[i] = time[i].split(' ')
            time[i] = time[i][1]

        for i in range(len(Data_json['data'])):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)
            # time_plot = Data_json['data'][i]['time']
            # time_plot = time_plot.split(' ')
            # time_plot = time_plot[1]
            # time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Temperatur, battery]
    




