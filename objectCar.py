from datetime import datetime,time

class Car:
    __mornMinhour = time(7)
    __mornMaxhour = time(9,30)
    __afternMinhour = time(16)
    __afternMaxhour = time(19,30)

    def __init__(self,placa,date_str,time_str):
        self.dateAtrib = date_str
        self.timeAtrib = time_str
        pass

    def canbeontheRoad(self):

        #filter per day of the week
        allowedDay = True
        compareDate = datetime.strptime(self.dateAtrib, '%Y-%m-%d').date()
        dayofWeek = (compareDate.toordinal()-1)%7+1
        if dayofWeek<6:
            allowedDay = False
        
        #filter per hour
        allowedHour = True
        compareTime = datetime.strptime(self.timeAtrib,"%X").time()
        rangeMorning = (compareTime >= self.__mornMinhour) and (compareTime <= self.__mornMaxhour)
        rangeAfternoon = (compareTime >= self.__afternMinhour) and (compareTime <= self.__afternMaxhour)
        if (rangeMorning or rangeAfternoon):
            allowedHour = False

        return (allowedDay or allowedHour)