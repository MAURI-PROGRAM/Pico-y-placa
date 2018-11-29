import unittest
from objectCar import Car

class canroadTestCase(unittest.TestCase): 
    #Test it is Weekend
    def test_canbeontheRoad_allowedDay(self):
        date_str='2018-11-24'
        car1=Car('ABC-1234',date_str,'07:20:11')
        self.assertEqual(car1.canbeontheRoad(),True)

    #Test it is not Weekend
    def test_canbeontheRoad_notallowedDay(self):
        date_str='2018-11-29'
        car1=Car('ABC-1234',date_str,'10:20:11')
        self.assertEqual(car1.canbeontheRoad(),False)
    
if __name__=='__main__':
    unittest.main()

        