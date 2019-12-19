from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        self.fill_contact_fields(contact)
        # Submit
        wd.find_element_by_xpath("//input[21]").click()
        self.app.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_homepage()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_homepage()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.filled_text_field_verification_contact("firstname", contact.firstname)
        self.filled_text_field_verification_contact("middlename", contact.middlename)
        self.filled_text_field_verification_contact("lastname", contact.lastname)
        self.filled_text_field_verification_contact("nickname", contact.nickname)
        self.filled_text_field_verification_contact("title", contact.title)
        self.filled_text_field_verification_contact("company", contact.company)
        self.filled_text_field_verification_contact("address", contact.adress)
        self.filled_text_field_verification_contact("home", contact.telephone_home)
        self.filled_text_field_verification_contact("mobile", contact.telephone_mobile)
        self.filled_text_field_verification_contact("work", contact.telephone_work)
        self.filled_text_field_verification_contact("fax", contact.telephone_fax)
        self.filled_text_field_verification_contact("email", contact.mail1)
        self.filled_text_field_verification_contact("email2", contact.mail2)
        self.filled_text_field_verification_contact("email3", contact.mail3)
        self.filled_text_field_verification_contact("homepage", contact.homepage)
        self.filled_text_field_verification_contact("address2", contact.secondary_address)
        self.filled_text_field_verification_contact("phone2", contact.secondary_phone)
        self.filled_text_field_verification_contact("notes", contact.secondary_notes)
        self.filled_image_field_verification_contact(contact.image)
        self.filled_text_field_verification_contact("byear", contact.byear)
        self.filled_text_field_verification_contact("ayear", contact.ayear)
        self.filled_additional_field_verification_contact("bday", contact.bday)
        self.filled_additional_field_verification_contact("bmonth", contact.bmonth)
        self.filled_additional_field_verification_contact("aday", contact.aday)
        self.filled_additional_field_verification_contact("amonth", contact.amonth)

    def filled_image_field_verification_contact(self, image_path):
        wd = self.app.wd
        if image_path is not None:
            wd.find_element_by_xpath("//input[@name='photo']").send_keys(image_path)

    def filled_text_field_verification_contact(self, field_name, input_data):
        wd = self.app.wd
        if input_data is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(input_data)

    def filled_additional_field_verification_contact(self, field_name, input_data):
        wd = self.app.wd
        if input_data is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(input_data)

    def count(self):
        wd = self.app.wd
        wd.app.open_home_page()
        return wd.find_element_by_css_selector("#search_count").text
