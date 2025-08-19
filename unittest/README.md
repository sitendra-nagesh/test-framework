# This directory contains files related to unittest module of python.
* Base tests directory has a sample example on how to unittest with a simple calcultion operation
* Employee-unittest directory has multiple step by step unit test conceptual implementation.

# Below are the points worth noting
- unittest is an inbuilt module.
- we need to import unittest module in our test file
- the file name should start test_ e.g. test_base.py
- using __name__=="__main__" with unittest.main() function will allow us to run the test as python file execution. 

- We use assertEqual to achieve the equality.
- multiple edge cases can be added to a single test itself. 
- setUp and tearDown methods are used for beginning and endding of a test method
- setUpClass and tearDownClass methods are used for beginning and end of the CLASS itself. Useful in case a database is created and it has to be destroyed after the test completion

- mock: (useless concept for now) is used to mock internet connection scenarios and more study is required if if it needs to be implemented. 
