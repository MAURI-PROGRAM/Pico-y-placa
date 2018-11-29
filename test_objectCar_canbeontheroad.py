import unittest
from objectCar import Car

class canroadTestCase(unittest.TestCase): 
    #Test. It is Weekend
    def test_canbeontheRoad_allowedDay(self):
        date_str='2018-11-24'
        car1=Car('ABC-1234',date_str,'07:20:11')
        self.assertEqual(car1.canbeontheRoad(),True)
    
    #Test. It is not Weekend and it is between the lag of hours allowed
    def test_canbeontheRoad_allowedHour(self):
        date_str='2018-11-29'
        time_str='19:30:01'
        car1=Car('ABC-1234',date_str,time_str)
        self.assertEqual(car1.canbeontheRoad(),True)

    #Test. It is not Weekend and it is between the lag of hours not allowed
    def test_canbeontheRoad_notallowedHour(self):
        date_str='2018-11-29'
        time_str='7:00:00'
        car1=Car('ABC-1234',date_str,time_str)
        self.assertEqual(car1.canbeontheRoad(),False)
    
    
if __name__=='__main__':
    unittest.main()

        