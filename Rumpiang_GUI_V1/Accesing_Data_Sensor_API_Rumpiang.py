import requests
import datetime

#==== Thermistor Saint Gobain =======
class AccesLiveData_API():

    def __init__(self, ID, N_data, step):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        
    def Acces_ATRH(self):

        http = 'http://192.168.1.41/rmcs/data/common/0/101/{}'.format(self.ID)
        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data": ["data0", "data1", "data2", "battery"],
            "options": {
                "filterTime" : c_str_datetime,
                "filterNumberBefore" : self.N_data,
                "filterStep" : (self.step*60)      
            }
        } 

        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        Humidity = []
        Pressure = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=self.step*x) for x in range(self.N_data)]

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
        http = 'http://192.168.1.41/rmcs/data/common/0/101/{}'.format(self.ID+4)

        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data": ["data0", "battery"],
            "options": {
                "filterTime" : c_str_datetime,
                "filterNumberBefore" : self.N_data,
                "filterStep" : (self.step*60)               
            }
        } 

        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Displacement = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=(self.step*x)) for x in range(self.N_data)]
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
    
    def Acces_TemperaturMaterial(self):
        http = 'http://192.168.1.41/rmcs/data/common/0/101/{}'.format(self.ID+8)

        current_date_Time = datetime.datetime.now().replace(microsecond=0, second=0)
        c_str_datetime = str(current_date_Time)
        
        data = {
            "data": ["data0", "battery"],
            "options": {
                "filterTime" : c_str_datetime,
                "filterNumberBefore" : self.N_data,
                "filterStep" : (self.step*60)
                
            }
        } 

        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        if self.ID > 2 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        battery = []

        datetime_list = [current_date_Time - datetime.timedelta(minutes=(self.step*x)) for x in range(self.N_data)]
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
        http = 'http://192.168.1.41/rmcs/data/common/0/101/{}'.format(self.ID)
        data = {
            "data": ["data0", "data1", "data2", "battery"],
            "options": {
                "filterBegin" : self.date_begin,
                "filterEnd" : self.date_end,
                "filterStep" : (self.step*60)        
            }
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        Humidity = []
        Pressure = []
        battery = []

        for i in range(len(Data_json['data'])):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)
            Humidity_plot = float(Data_json['data'][i]['data1'])
            Humidity.append(Humidity_plot)
            Pressure_plot = float(Data_json['data'][i]['data2'])
            Pressure.append(Pressure_plot)
            time_plot = Data_json['data'][i]['time']
            time_plot = time_plot.split(' ')
            time_plot = time_plot[1]
            time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Temperatur, Humidity, Pressure, battery]

    
    def Acces_LinearDisplacement(self):
        http = 'http://192.168.1.41/rmcs/data/common/0/101/{}'.format(self.ID+4)
        data = {
            "data": ["data0", "battery"],
            "options": {
                "filterBegin" : self.date_begin,
                "filterEnd" : self.date_end,
                "filterStep" : (self.step*60)        
            }
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }
        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Displacement = []
        battery = []

        for i in range(len(Data_json['data'])):
            Displacement_plot = float(Data_json['data'][i]['data0'])
            Displacement.append(Displacement_plot)
            time_plot = Data_json['data'][i]['time']
            time_plot = time_plot.split(' ')
            time_plot = time_plot[1]
            time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Displacement, battery]
    
    def Acces_TemperaturMaterial(self):
        http = 'http://192.168.1.41/rmcs/data/common/0/101/{}'.format(self.ID)
        data = {
            "data": ["data0", "battery"],
            "options": {
                "filterBegin" : self.date_begin,
                "filterEnd" : self.date_end,
                "filterStep" : (self.step*60)        
            }
        } 
        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        if self.ID > 4 or self.ID < 1:
            return("Please Enter The Correct ID Sensor")
        else:
            Request_Data = requests.get(http, json = data, headers=headers)
        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        battery = []

        for i in range(len(Data_json['data'])):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)
            time_plot = Data_json['data'][i]['time']
            time_plot = time_plot.split(' ')
            time_plot = time_plot[1]
            time.append(time_plot)
            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Temperatur, battery]
    




