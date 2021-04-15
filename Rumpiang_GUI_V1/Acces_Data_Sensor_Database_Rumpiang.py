import mariadb
import datetime

#Acces Data Base 
conn = mariadb.connect(
    user = 'root',
    password = 'zahra105',
    port = 3306,
    database = 'rmcs_0'
)
cur = conn.cursor()
cur.execute("SELECT * FROM `data_common` ORDER BY `data_common`.`time` DESC, `data_common`.`node_id` ASC")
data = cur.fetchall()

class AccesLiveData_DataBase():

    def __init__(self, ID, N_data, step):
        self.N_data = N_data
        self.ID = ID
        self.step = step

    def Acces_ATRH(self):
        #Acces ATRH
        ATRH1_time = []
        ATRH2_time = []
        ATRH3_time = []
        ATRH4_time = []

        ATRH1_Temp = []
        ATRH2_Temp = []
        ATRH3_Temp = []
        ATRH4_Temp = []

        ATRH1_Hum = []
        ATRH2_Hum = []
        ATRH3_Hum = []
        ATRH4_Hum = []

        ATRH1_Pres = []
        ATRH2_Pres = []
        ATRH3_Pres = []
        ATRH4_Pres = []

        ATRH1_Bat = []
        ATRH2_Bat = []
        ATRH3_Bat = []
        ATRH4_Bat = []

        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0

        datetime_now = datetime.datetime.now().replace(microsecond=0,second=0)
        datetime_list = [datetime_now - datetime.timedelta(minutes=self.step*x) for x in range(self.N_data)]

        for i in range(len(data)):
            Node_id = data[i][1]

            if Node_id == 1:

                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        T = data[i][4]
                        H = data[i][5]
                        P = data[i][6]
                        B = data[i][3]

                        ATRH1_time.append(t)
                        ATRH1_Temp.append(T)
                        ATRH1_Hum.append(H)
                        ATRH1_Pres.append(P)
                        ATRH1_Bat.append(B)

                        count_1 = count_1 + 1
     
            elif Node_id == 2:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:


                        T = data[i][4]
                        H = data[i][5]
                        P = data[i][6]
                        B = data[i][3]

                        ATRH2_time.append(t)
                        ATRH2_Temp.append(T)
                        ATRH2_Hum.append(H)
                        ATRH2_Pres.append(P)
                        ATRH2_Bat.append(B)


                        count_2 = count_2 + 1

            elif Node_id == 3:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        T = data[i][4]
                        H = data[i][5]
                        P = data[i][6]
                        B = data[i][3]

                        ATRH3_time.append(t)
                        ATRH3_Temp.append(T)
                        ATRH3_Hum.append(H)
                        ATRH3_Pres.append(P)
                        ATRH3_Bat.append(B)

                        count_3 = count_3 + 1
            
            elif Node_id == 4:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:
                        T = data[i][4]
                        H = data[i][5]
                        P = data[i][6]
                        B = data[i][3]

                        ATRH4_time.append(t)
                        ATRH4_Temp.append(T)
                        ATRH4_Hum.append(H)
                        ATRH4_Pres.append(P)
                        ATRH4_Bat.append(B)

                        count_4 = count_4 + 1
            
            if self.ID == 1 and count_1 == self.N_data:
                break
            elif self.ID == 2 and count_2 == self.N_data:
                break
            elif self.ID == 3 and count_3 == self.N_data:
                break
            elif self.ID == 4 and count_4 == self.N_data:
                break
        
        if self.ID == 1:
            ATRH1_time = self.ConvertDatetime_Time(ATRH1_time)
            return[ATRH1_time, ATRH1_Temp, ATRH1_Hum, ATRH1_Pres, ATRH1_Bat]
        elif self.ID == 2:
            ATRH2_time = self.ConvertDatetime_Time(ATRH2_time)
            return[ATRH2_time, ATRH2_Temp, ATRH2_Hum, ATRH2_Pres, ATRH2_Bat]
        elif self.ID == 3:
            ATRH3_time = self.ConvertDatetime_Time(ATRH3_time)
            return[ATRH3_time, ATRH3_Temp, ATRH3_Hum, ATRH3_Pres, ATRH3_Bat]
        elif self.ID == 4:
            ATRH4_time = self.ConvertDatetime_Time(ATRH4_time)
            return[ATRH4_time, ATRH4_Temp, ATRH4_Hum, ATRH4_Pres, ATRH4_Bat]
           
    
    def Acces_LinearDisplacement(self):
        #Acces LD
        LD1_time = []
        LD1_Disp = []

        LD2_time = []
        LD2_Disp = []

        LD3_time = []
        LD3_Disp = []

        LD4_time = []
        LD4_Disp = []

        LD1_Bat = []
        LD2_Bat = []
        LD3_Bat = []
        LD4_Bat = []

        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0

        datetime_now = datetime.datetime.now().replace(microsecond=0,second=0)
        datetime_list = [datetime_now - datetime.timedelta(minutes=self.step*x) for x in range(self.N_data)]


        for i in range(len(data)):
            Node_id = data[i][1]
            if Node_id == 5: 
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        LD1_time.append(t)
                        LD1_Disp.append(D)
                        LD1_Bat.append(B)

                        count_1 = count_1 + 1

            elif Node_id == 6:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        LD2_time.append(t)
                        LD2_Disp.append(D)
                        LD2_Bat.append(B)

                        count_2 = count_2 + 1
            
            elif Node_id == 7:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        LD3_time.append(t)
                        LD3_Disp.append(D)
                        LD3_Bat.append(B)

                        count_3 = count_3 + 1
            
            elif Node_id == 8:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        LD4_time.append(t)
                        LD4_Disp.append(D)
                        LD4_Bat.append(B)

                        count_4 = count_4 + 1
            
            if self.ID == 1 and count_1 == self.N_data:
                break
            elif self.ID == 2 and count_2 == self.N_data:
                break
            elif self.ID == 3 and count_3 == self.N_data:
                break
            elif self.ID == 4 and count_4 == self.N_data:
                break

        if self.ID == 1:
            LD1_time = self.ConvertDatetime_Time(LD1_time)
            return[LD1_time, LD1_Disp, LD1_Bat]
        elif self.ID == 2:
            LD2_time = self.ConvertDatetime_Time(LD2_time)
            return[LD2_time, LD2_Disp, LD2_Bat]
        elif self.ID == 3:
            LD3_time = self.ConvertDatetime_Time(LD3_time)
            return[LD3_time, LD3_Disp, LD3_Bat]
        elif self.ID == 4:    
            LD4_time = self.ConvertDatetime_Time(LD4_time)
            return[LD4_time, LD4_Disp, LD4_Bat]
    
    def Acces_StrainGauge(self):
        #Acces SG
        SG1_time = []
        SG1_Disp = []

        SG2_time = []
        SG2_Disp = []

        SG3_time = []
        SG3_Disp = []

        SG4_time = []
        SG4_Disp = []

        SG1_Bat = []
        SG2_Bat = []
        SG3_Bat = []
        SG4_Bat = []

        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0

        datetime_now = datetime.datetime.now().replace(microsecond=0,second=0)
        datetime_list = [datetime_now - datetime.timedelta(minutes=self.step*x) for x in range(self.N_data)]


        for i in range(len(data)):
            Node_id = data[i][1]
            if Node_id == 5: 
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        SG1_time.append(t)
                        SG1_Disp.append(D)
                        SG1_Bat.append(B)

                        count_1 = count_1 + 1

            elif Node_id == 6:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        SG2_time.append(t)
                        SG2_Disp.append(D)
                        SG2_Bat.append(B)

                        count_2 = count_2 + 1
            
            elif Node_id == 7:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        SG3_time.append(t)
                        SG3_Disp.append(D)
                        SG3_Bat.append(B)

                        count_3 = count_3 + 1
            
            elif Node_id == 8:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        D = data[i][4]
                        B = data[i][3]

                        SG4_time.append(t)
                        SG4_Disp.append(D)
                        SG4_Bat.append(B)

                        count_4 = count_4 + 1
            
            if self.ID == 1 and count_1 == self.N_data:
                break
            elif self.ID == 2 and count_2 == self.N_data:
                break
            elif self.ID == 3 and count_3 == self.N_data:
                break
            elif self.ID == 4 and count_4 == self.N_data:
                break

        if self.ID == 1:
            SG1_time = self.ConvertDatetime_Time(SG1_time)
            return[SG1_time, SG1_Disp, SG1_Bat]
        elif self.ID == 2:
            SG2_time = self.ConvertDatetime_Time(SG2_time)
            return[SG2_time, SG2_Disp, SG2_Bat]
        elif self.ID == 3:
            SG3_time = self.ConvertDatetime_Time(SG3_time)
            return[SG3_time, SG3_Disp, SG3_Bat]
        elif self.ID == 4:    
            SG4_time = self.ConvertDatetime_Time(SG4_time)
            return[SG4_time, SG4_Disp, SG4_Bat]
 
    def Acces_TemperatureMaterial(self):
        #Acces Temperature Material
        TM1_time = []
        TM1_Temp = []

        TM2_time = []
        TM2_Temp = []

        TM1_Bat = []
        TM2_Bat = []

        count_1 = 0
        count_2 = 0

        datetime_now = datetime.datetime.now().replace(microsecond=0,second=0)
        datetime_list = [datetime_now - datetime.timedelta(minutes=self.step*x) for x in range(self.N_data)]
        
        for i in range(len(data)):
            Node_id = data[i][1]

            if Node_id == 9:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        TM = data[i][4]
                        B = data[i][3]
                        
                        TM1_time.append(t)
                        TM1_Temp.append(TM)
                        TM1_Bat.append(B)

                        count_1 = count_1 + 1

            elif Node_id == 10:
                t = data[i][2]
                for j in range(len(datetime_list)):
                    if t == datetime_list[j]:

                        TM = data[i][4]
                        B = data[i][3]

                        TM2_time.append(t)
                        TM2_Temp.append(TM)
                        TM2_Bat.append(B)

                        count_2 = count_2 + 1
            
            if self.ID == 1 and count_1 == self.N_data:
                break
            elif self.ID == 2 and count_2 == self.N_data:
                break

        if self.ID == 1:
            TM1_time = self.ConvertDatetime_Time(TM1_time)
            return[TM1_time, TM1_Temp, TM1_Bat]
        elif self.ID == 2:
            TM2_time = self.ConvertDatetime_Time(TM2_time)
            return[TM2_time, TM2_Temp, TM2_Bat]
    
    def ConvertDatetime_Time(self, list_datetime):
        time = []
        for j in range(len(list_datetime)):
            datetime_ = list_datetime[j].strftime("%Y-%m-%d %H:%M:%S")
            datetime_ = datetime_.split(' ')
            datetime_ = datetime_[1]
            time.append(datetime_)
        return(time)

class AccesHistoryData_DataBase():
    
    def __init__(self, ID, datetime_begin, datetime_end, step):
        self.ID = ID
        self.datetime_begin = datetime_begin
        self.datetime_end = datetime_end
        self.step = step
    
    def Acces_ATRH(self):
        ATRH1_time = []
        ATRH2_time = []
        ATRH3_time = []
        ATRH4_time = []

        ATRH1_Temp = []
        ATRH2_Temp = []
        ATRH3_Temp = []
        ATRH4_Temp = []

        ATRH1_Hum = []
        ATRH2_Hum = []
        ATRH3_Hum = []
        ATRH4_Hum = []

        ATRH1_Pres = []
        ATRH2_Pres = []
        ATRH3_Pres = []
        ATRH4_Pres = []

        start_datetime = datetime.datetime.strptime(self.datetime_begin, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        end_datetime = datetime.datetime.strptime(self.datetime_end, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        step_datetime = datetime.timedelta(minutes=self.step)

        datetime_list = []

        while start_datetime <= end_datetime:
            datetime_list.append(end_datetime)
            end_datetime -= step_datetime

        for i in range(len(data)):
            Node_id = data[i][1]
            t = data[i][2]
            for j in range(len(datetime_list)):
                if Node_id == 1 and t == datetime_list[j]:

                    T = data[i][4]
                    H = data[i][5]
                    P = data[i][6]

                    ATRH1_time.append(t)
                    ATRH1_Temp.append(T)
                    ATRH1_Hum.append(H)
                    ATRH1_Pres.append(P)

                elif Node_id == 2 and t == datetime_list[j]:

                    T = data[i][4]
                    H = data[i][5]
                    P = data[i][6]

                    ATRH2_time.append(t)
                    ATRH2_Temp.append(T)
                    ATRH2_Hum.append(H)
                    ATRH2_Pres.append(P)

                elif Node_id == 3 and t == datetime_list[j]:

                    T = data[i][4]
                    H = data[i][5]
                    P = data[i][6]

                    ATRH3_time.append(t)
                    ATRH3_Temp.append(T)
                    ATRH3_Hum.append(H)
                    ATRH3_Pres.append(P)

                elif Node_id == 4 and t == datetime_list[j]:

                    T = data[i][4]
                    H = data[i][5]
                    P = data[i][6]

                    ATRH4_time.append(t)
                    ATRH4_Temp.append(T)
                    ATRH4_Hum.append(H)
                    ATRH4_Pres.append(P)
        
        if self.ID == 1:
            ATRH1_time = self.ConvertDatetime_Time(ATRH1_time)
            return[ATRH1_time, ATRH1_Temp, ATRH1_Hum, ATRH1_Pres]
        elif self.ID == 2:
            ATRH2_time = self.ConvertDatetime_Time(ATRH2_time)
            return[ATRH2_time, ATRH2_Temp, ATRH2_Hum, ATRH2_Pres]
        elif self.ID == 3:
            ATRH3_time = self.ConvertDatetime_Time(ATRH3_time)
            return[ATRH3_time, ATRH3_Temp, ATRH3_Hum, ATRH3_Pres]
        elif self.ID == 4:
            ATRH4_time = self.ConvertDatetime_Time(ATRH4_time)
            return[ATRH4_time, ATRH4_Temp, ATRH4_Hum, ATRH4_Pres]

    def Acces_LinearDisplacement(self):
        LD1_time = []
        LD1_Disp = []

        LD2_time = []
        LD2_Disp = []

        LD3_time = []
        LD3_Disp = []

        LD4_time = []
        LD4_Disp = []

        start_datetime = datetime.datetime.strptime(self.datetime_begin, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        end_datetime = datetime.datetime.strptime(self.datetime_end, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        step_datetime = datetime.timedelta(minutes=self.step)

        datetime_list = []

        while start_datetime <= end_datetime:
            datetime_list.append(end_datetime)
            end_datetime -= step_datetime

        for i in range(len(data)):
            Node_id = data[i][1]
            t = data[i][2]
            for j in range(len(datetime_list)):
                if Node_id == 5 and t == datetime_list[j]:
                    D = data[i][4]
                    LD1_time.append(t)
                    LD1_Disp.append(D)
                elif Node_id == 6 and t == datetime_list[j]:
                    D = data[i][4]
                    LD2_time.append(t)
                    LD2_Disp.append(D)
                elif Node_id == 7 and t == datetime_list[j]:
                    D = data[i][4]
                    LD3_time.append(t)
                    LD3_Disp.append(D)
                elif Node_id == 8 and t == datetime_list[j]:
                    D = data[i][4]
                    LD4_time.append(t)
                    LD4_Disp.append(D)
    
        if self.ID == 1:
            LD1_time = self.ConvertDatetime_Time(LD1_time)
            return[LD1_time, LD1_Disp]
        elif self.ID == 2:
            LD2_time = self.ConvertDatetime_Time(LD2_time)
            return[LD2_time, LD2_Disp]
        elif self.ID == 3:
            LD3_time = self.ConvertDatetime_Time(LD3_time)
            return[LD3_time, LD3_Disp]
        elif self.ID == 4:    
            LD4_time = self.ConvertDatetime_Time(LD4_time)
            return[LD4_time, LD4_Disp]

    def Acces_StrainGauge(self):
        SG1_time = []
        SG1_Disp = []

        SG2_time = []
        SG2_Disp = []

        SG3_time = []
        SG3_Disp = []

        SG4_time = []
        SG4_Disp = []

        start_datetime = datetime.datetime.strptime(self.datetime_begin, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        end_datetime = datetime.datetime.strptime(self.datetime_end, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        step_datetime = datetime.timedelta(minutes=self.step)

        datetime_list = []

        while start_datetime <= end_datetime:
            datetime_list.append(end_datetime)
            end_datetime -= step_datetime

        for i in range(len(data)):
            Node_id = data[i][1]
            t = data[i][2]
            for j in range(len(datetime_list)):
                if Node_id == 5 and t == datetime_list[j]:
                    D = data[i][4]
                    SG1_time.append(t)
                    SG1_Disp.append(D)
                elif Node_id == 6 and t == datetime_list[j]:
                    D = data[i][4]
                    SG2_time.append(t)
                    SG2_Disp.append(D)
                elif Node_id == 7 and t == datetime_list[j]:
                    D = data[i][4]
                    SG3_time.append(t)
                    SG3_Disp.append(D)
                elif Node_id == 8 and t == datetime_list[j]:
                    D = data[i][4]
                    SG4_time.append(t)
                    SG4_Disp.append(D)
    
        if self.ID == 1:
            SG1_time = self.ConvertDatetime_Time(SG1_time)
            return[SG1_time, SG1_Disp]
        elif self.ID == 2:
            SG2_time = self.ConvertDatetime_Time(SG2_time)
            return[SG2_time, SG2_Disp]
        elif self.ID == 3:
            SG3_time = self.ConvertDatetime_Time(SG3_time)
            return[SG3_time, SG3_Disp]
        elif self.ID == 4:    
            SG4_time = self.ConvertDatetime_Time(SG4_time)
            return[SG4_time, SG4_Disp]
    
    def Acces_TemperaturMaterial(self):
        TM1_time = []
        TM1_Temp = []

        TM2_time = []
        TM2_Temp = []

        start_datetime = datetime.datetime.strptime(self.datetime_begin, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        end_datetime = datetime.datetime.strptime(self.datetime_end, '%Y-%m-%d %H:%M:%S').replace(microsecond=0, second=0)
        step_datetime = datetime.timedelta(minutes=self.step)

        datetime_list = []

        while start_datetime <= end_datetime:
            datetime_list.append(end_datetime)
            end_datetime -= step_datetime
        
        for i in range(len(data)):
            Node_id = data[i][1]
            t = data[i][2]
            for j in range(len(datetime_list)):
                if Node_id == 9 and t == datetime_list[j]:
                    TM = data[i][4]
                    TM1_time.append(t)
                    TM1_Temp.append(TM)
                elif Node_id == 10 and t == datetime_list[j]:
                    TM = data[i][4]
                    TM2_time.append(t)
                    TM2_Temp.append(TM)

        if self.ID == 1:
            TM1_time = self.ConvertDatetime_Time(TM1_time)
            return[TM1_time, TM1_Temp]
        elif self.ID == 2:
            TM2_time = self.ConvertDatetime_Time(TM2_time)
            return[TM2_time, TM2_Temp]

    def ConvertDatetime_Time(self, list_datetime):
        time = []
        for j in range(len(list_datetime)):
            datetime_ = list_datetime[j].strftime("%Y-%m-%d %H:%M:%S")
            datetime_ = datetime_.split(' ')
            datetime_ = datetime_[1]
            time.append(datetime_)
        return(time)