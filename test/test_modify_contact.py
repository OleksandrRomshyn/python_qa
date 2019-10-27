from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="edited_first_name", middlename="edited_middle_name", lastname="edited_last_name",
                                             nickname="edited_nickname", title="edited_title", company="edited_company", adress="edited_address",
                                             telephone_home="edited_telephone_home", telephone_mobile="edited_telephone_mobile",
                                             telephone_work="edited_telephone_work", telephone_fax="edited_telephone_fax",
                                             mail1="edited_e-mail_1",
                                             mail2="edited_e-mail_2", mail3="edited_e-mail_3", homepage="edited_homepage", bday="22",
                                             bmonth="March", byear="1990", aday="21", amonth="May", ayear="2010",
                                             secondary_address="edited_Secondary_Address",
                                             secondary_phone="edited_Secondary_Phone", secondary_notes="edited_Secondary_Notes",
                                             image="C:\\Users\\11\\Desktop\\edited_panda.jpg"))
    app.session.logout()
