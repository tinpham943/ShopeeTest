import unittest
from selenium import webdriver

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://newtours.demoaut.com/")
        inst.driver.title

    def test_login_passed(self):
        # get the search textbox
        self.username_field = self.driver.find_element_by_name('userName')
        self.password_field = self.driver.find_element_by_name('password')
        self.login_button = self.driver.find_element_by_name('login')
        self.username_field.clear()
        self.password_field.clear()

        # enter account and submit
        self.username_field.send_keys('shopeetest')
        self.password_field.send_keys('Shopee@2020')
        self.login_button.click()
        self.assertTrue( self.driver.find_element_by_name('findFlights').is_displayed())

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()