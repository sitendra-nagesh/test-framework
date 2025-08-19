import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp1 = Employee("John", "Doe", 50000)
        emp2 = Employee("Jane", "Dee", 60000)

        self.assertEqual(emp1.email, "John.Doe@email.com")
        self.assertEqual(emp2.email, "Jane.Dee@email.com")

        emp1.first = "Dexter"
        emp2.first = "Patrick"

        self.assertEqual(emp1.email, "Dexter.Doe@email.com")
        self.assertEqual(emp2.email, "Patrick.Dee@email.com")

    def test_fullname(self):
        emp1 = Employee("John", "Doe", 50000)
        emp2 = Employee("Jane", "Dee", 60000)

        self.assertEqual(emp1.fullname, "John Doe")
        self.assertEqual(emp2.fullname, "Jane Dee")

        emp1.first = "Dexter"
        emp2.first = "Patrick"

        self.assertEqual(emp1.fullname, "Dexter Doe")
        self.assertEqual(emp2.fullname, "Patrick Dee")

  
    def test_apply_raise(self):
        emp1 = Employee("John", "Doe", 50000)
        emp2 = Employee("Jane", "Dee", 60000)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 52500)
        self.assertEqual(emp2.pay, 63000)
        

if __name__ == "__main__":
    unittest.main()
