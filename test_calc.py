import unittest  # import the unittest module

import calc  # import the file that contains the functions to be tested

class TestCalc(unittest.TestCase):  # create a TestCalc class that inherits from unittest.TestCase

    def test_add(self):  
        self.assertEqual(calc.add(40, 2), 42)
        self.assertEqual(calc.add(-1, 1), 0)  
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):  
        self.assertEqual(calc.subtract(40, 2), 38)
        self.assertEqual(calc.subtract(-1, 1), -2)  
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):  
        self.assertEqual(calc.multiply(40, 2), 80)
        self.assertEqual(calc.multiply(-1, 1), -1)  
        self.assertEqual(calc.multiply(-1, -1), 1)  

    def test_divide(self):  
        self.assertEqual(calc.divide(40, 2), 20)
        self.assertEqual(calc.divide(-1, 1), -1)  
        self.assertEqual(calc.divide(-1, -1), 1)  
        self.assertEqual(calc.divide(43, 2), 21.5) #Failed when using floor division
        
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # with self.assertRaises(ValueError):
            # calc.divide(10, 0)
            
if __name__ == '__main__':  # check if this file is being run as the main program
    unittest.main()  # run the tests defined in this file using the unittest module

  