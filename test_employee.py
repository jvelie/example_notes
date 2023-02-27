import unittest
from employee import Employee

class TestEmploy(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("Chris", "Smith", 60000) 
        self.emp_2 = Employee("Alice", "Smith", 50000)
    
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Chris.Smith@email.com")
        self.assertEqual(self.emp_2.email, "Alice.Smith@email.com")

        self.emp_1.first = "Abigail"
        self.emp_2.first = "Clark"

        self.assertEqual(self.emp_1.email, "Abigail.Smith@email.com")
        self.assertEqual(self.emp_2.email, "Clark.Smith@email.com")
    
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Chris Smith")
        self.assertEqual(self.emp_2.fullname, "Alice Smith")
       
        self.emp_1.first = "Abigail"
        self.emp_2.first = "Clark"

        self.assertEqual(self.emp_1.fullname, "Abigail Smith")
        self.assertEqual(self.emp_2.fullname, "Clark Smith")
    
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 63000)
        self.assertEqual(self.emp_2.pay, 52500)

if __name__ == '__main__':
    unittest.main()