from datetime import datetime,time

class Car:
    __mornMinhour = time(7)
    __mornMaxhour = time(9,30)
    __afternMinhour = time(16)
    __afternMaxhour = time(19,30)

    def __init__(self,plate_str,date_str,time_str):
        self.dateAtrib = date_str
        self.timeAtrib = time_str
        self.plateAtrib = plate_str
        pass

    def canbeontheRoad(self):

        #filter per day of the week
        #the day of the week are Monday=1, Tuesday=2 .... Sunday=7 for this program
        compareDate = datetime.strptime(self.dateAtrib, '%Y-%m-%d').date()
        dayofWeek = (compareDate.toordinal()-1)%7+1
        if dayofWeek>5:
            return True
        
        #filter per hour
        compareTime = datetime.strptime(self.timeAtrib,"%X").time()
        rangeMorning = (compareTime >= self.__mornMinhour) and (compareTime <= self.__mornMaxhour)
        rangeAfternoon = (compareTime >= self.__afternMinhour) and (compareTime <= self.__afternMaxhour)
        if not(rangeMorning or rangeAfternoon):
            return True
        
        #filter per last digit of the license plate number
        # dictionary structure, dayandNumber={number_of_week:[last digit]}
        lastDigit = int(self.plateAtrib[-1])
        dayandNumber = {1:[1,2],2:[3,4],3:[5,6],4:[7,8],5:[9,0]}
        if not(lastDigit in dayandNumber.get(dayofWeek)):
            return True
        
        return False