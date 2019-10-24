# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact


class AddContact(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.new_contact_creation(wd, Contact(firstname="first_name", middlename="middle_name", lastname="last_name",
                                  nickname="nickname", title="title", company="company", adress="address",
                                  telephone_home="telephone_home", telephone_mobile="telephone_mobile",
                                  telephone_work="telephone_work", telephone_fax="telephone_fax", mail1="e-mail_1",
                                  mail2="e-mail_2", mail3="e-mail_3", homepage="homepage", bday="2", bmonth="February",
                                  byear="1980", aday="1", amonth="April", ayear="2000",
                                  secondary_address="Secondary_Address",
                                  secondary_phone="Secondary_Phone", secondary_notes="Secondary_Notes"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.new_contact_creation(wd, Contact(firstname="", middlename="", lastname="",
                                  nickname="", title="", company="", adress="",
                                  telephone_home="", telephone_mobile="",
                                  telephone_work="", telephone_fax="", mail1="",
                                  mail2="", mail3="", homepage="", bday="", bmonth="",
                                  byear="", aday="", amonth="", ayear="",
                                  secondary_address="",
                                  secondary_phone="", secondary_notes=""))
        self.return_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def new_contact_creation(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.adress)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("home").send_keys(Keys.UP)
        wd.find_element_by_name("home").send_keys(Keys.TAB)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.telephone_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.mail2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.mail3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[4]").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[4]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[36]").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # wd.find_element_by_xpath("//input[@name='photo']").click()
        # wd.find_element_by_xpath("//input[@name='photo']").clear()
        # wd.find_element_by_xpath("//input[@name='photo']").send_keys(jpg)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
