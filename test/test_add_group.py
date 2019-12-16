# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group_1", header="Logo_1", footer="Comment_1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
