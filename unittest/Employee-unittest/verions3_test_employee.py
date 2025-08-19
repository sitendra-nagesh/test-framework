import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    # two class methods run before anything and after anything
    # setUp method runs before any tests and tearDown after anytests.
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.emp1 = Employee("John", "Doe", 50000)
        self.emp2 = Employee("Jane", "Dee", 60000)
        print("setUp")

    def tearDown(self):
        print("TearDown")
        pass

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email, "John.Doe@email.com")
        self.assertEqual(self.emp2.email, "Jane.Dee@email.com")

        self.emp1.first = "Dexter"
        self.emp2.first = "Patrick"

        self.assertEqual(self.emp1.email, "Dexter.Doe@email.com")
        self.assertEqual(self.emp2.email, "Patrick.Dee@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp1.fullname, "John Doe")
        self.assertEqual(self.emp2.fullname, "Jane Dee")

        self.emp1.first = "Dexter"
        self.emp2.first = "Patrick"

        self.assertEqual(self.emp1.fullname, "Dexter Doe")
        self.assertEqual(self.emp2.fullname, "Patrick Dee")
  
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

if __name__ == "__main__":
    unittest.main()
