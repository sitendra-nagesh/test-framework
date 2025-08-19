import unittest
import calc

class TestCalc(unittest.TestCase):
    
    #def test_add(self):
        #result = calc.add(10, 5)
        #self.assertEqual(result, 14)
   
   # Below test will not run because it does not start with keyword test.
    #def add_test(self):
    #    result = calc.add(10, 5)
    #    self.assertEqual(result, 15)
    
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-3,-5), -8)

    def test_subtact(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-3,-5), 2)

    def test_mulitply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-3,-5), 15)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-3,-5), 0.6)

        # self.assertEqual(calc.divide(10,0) , 0)
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        
        # Using context manager(?)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
