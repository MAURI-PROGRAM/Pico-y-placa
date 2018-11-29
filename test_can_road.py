import unittest
from can_road import Car

class canroadTestCase(unittest.TestCase):

    def test_canRoad_true(self):
        car1=Car('ABC-1234','2018-11-22','10:20:11')
        self.assertEqual(car1.canRoad(),True)
 
if __name__ == '__main__':
        unittest.main()
        