# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="Group_1", header="Logo_1", footer="Comment_1"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


if __name__ == "__main__":
    unittest.main()
