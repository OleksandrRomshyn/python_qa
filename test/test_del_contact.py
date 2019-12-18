from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == "0":
        app.contact.create(Contact(firstname="Pre_created_contact"))
    app.contact.delete_first_contact()