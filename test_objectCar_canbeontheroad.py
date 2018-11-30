import unittest
from objectCar import Car

class canroadTestCase(unittest.TestCase): 
    #Test. It is Weekend
    def test_canbeontheRoad_allowedDay(self):
        date_str='2018-11-24'
        car1=Car('ABC-1234',date_str,'07:20:11')
        self.assertEqual(car1.canbeontheRoad(),True)
    
    #Test. It is not Weekend and between the lag of hours are allowed
    def test_canbeontheRoad_allowedHour(self):
        date_str='2018-11-29'
        time_str='19:30:01'
        car1=Car('ABC-1234',date_str,time_str)
        self.assertEqual(car1.canbeontheRoad(),True)

    #Test. It is not Weekend , between the lag of hours  and last digit number are allowed
    def test_canbeontheRoad_allowedPlate(self):
        date_str='2018-11-27'
        time_str='7:00:00'
        licPlatenum='ABC-1231'
        car1=Car(licPlatenum,date_str,time_str)
        self.assertEqual(car1.canbeontheRoad(),True)
    
    #Test. It is not Weekend, between the lag of hours and last digit number aren't allowed
    def test_canbeontheRoad_notallowedPlate(self):
        date_str='2018-11-26'
        time_str='7:00:00'
        licPlatenum='ABC-1231'
        car1=Car(licPlatenum,date_str,time_str)
        self.assertEqual(car1.canbeontheRoad(),False)
    
if __name__=='__main__':
    unittest.main()     