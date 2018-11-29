from datetime import datetime

class Car:
    def __init__(self,placa,date,hora):
        self.date_str = date
        pass
    def canbeontheRoad(self):

        #filter per day of the week
        allowedDay=True
        compare_date = datetime.strptime(self.date_str, '%Y-%m-%d').date()
        dayofWeek = (compare_date.toordinal()-1)%7+1
        if dayofWeek<6:
            allowedDay=False
        

        return allowedDay