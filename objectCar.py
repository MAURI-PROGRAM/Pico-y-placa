from datetime import datetime,time
import re

class Car:
    __mornMinhour = time(7)
    __mornMaxhour = time(9,30)
    __afternMinhour = time(16)
    __afternMaxhour = time(19,30)

    def __init__(self,plate_str,date_str,time_str):
        self.dateAtrib = date_str
        self.timeAtrib = time_str
        self.plateAtrib = plate_str

    def canbeontheRoad(self):

        #filter per day of the week
        #the day of the week are Monday=1, Tuesday=2 .... Sunday=7 for this program
        try:
            compareDate = datetime.strptime(self.dateAtrib, '%Y-%m-%d').date()
        except:
            print('format of date incorrect')
            return None
        dayofWeek = (compareDate.toordinal()-1)%7+1
        if dayofWeek>5:
            return True
        
        #filter per hour
        try:
            compareTime = datetime.strptime(self.timeAtrib,"%X").time()
        except:
            print('format of time incorrect')
            return None  
        rangeMorning = (compareTime >= self.__mornMinhour) and (compareTime <= self.__mornMaxhour)
        rangeAfternoon = (compareTime >= self.__afternMinhour) and (compareTime <= self.__afternMaxhour)
        if not(rangeMorning or rangeAfternoon):
            return True
        
        #filter per last digit of the license plate number
        # dictionary structure, dayandNumber={number_of_week:[last digit]}
        patron = re.compile('[A-Za-z]{3}[-][1-9]{3,4}$')
        matcher = patron.match(self.plateAtrib)
        if matcher is None:
            print('format of time incorrect')
            return None
        lastDigit = int(self.plateAtrib[-1])
        dayandNumber = {1:[1,2],2:[3,4],3:[5,6],4:[7,8],5:[9,0]}
        if not(lastDigit in dayandNumber.get(dayofWeek)):
            return True
        
        return False