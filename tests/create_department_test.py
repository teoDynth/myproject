"""Module with CreateDepartmentTest unittest Test Case class."""
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())


class CreateDepartmentTest(unittest.TestCase):
    """A Test Case class for creating a department item in the database. Creates and then deletes a department item."""
    def setUp(self):
        from main import my_app
        self.app = my_app.test_client()
        self.app.testing = True
        self.driver = browser

    def test_new_department_creation(self):
        driver = self.driver
        page_url = 'http://192.168.0.118:5000/new-department'
        driver.get(page_url)
        form = driver.find_element(By.XPATH, '//*[@id="name"]')
        form.send_keys('Test department')
        submit = driver.find_element(By.XPATH, '//*[@id="submit"]')
        submit.click()
        departments = self.app.get('/')
        self.assertIn('Test department', str(departments.data))

    def tearDown(self):
        driver = self.driver
        department_to_delete = driver.find_element(By.LINK_TEXT, 'Test department')
        department_to_delete.click()
        delete_button = driver.find_element(By.XPATH, '/html/body/a[2]/button')
        delete_button.click()
        self.driver.close()
