# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first_name", middlename="middle_name", lastname="last_name",
                       nickname="nickname", title="title", company="company", adress="address",
                       telephone_home="telephone_home", telephone_mobile="telephone_mobile",
                       telephone_work="telephone_work", telephone_fax="telephone_fax",
                       mail1="e-mail_1",
                       mail2="e-mail_2", mail3="e-mail_3", homepage="homepage", bday="2",
                       bmonth="February",
                       byear="1980", aday="1", amonth="April", ayear="2000",
                       secondary_address="Secondary_Address",
                       secondary_phone="Secondary_Phone", secondary_notes="Secondary_Notes",
                       image="C:\\Users\\11\\Desktop\\panda.jpg"))
    app.session.logout()

