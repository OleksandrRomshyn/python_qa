from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Pre_created_group"))
    app.group.modify_first_group(Group(name="Edited_Group_1", header="Edited_Logo_1", footer="Edited_Comment_1"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Pre_created_group"))
    app.group.modify_first_group(Group(name="Edited_Group_2"))
