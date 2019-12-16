from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Edited_Group_1", header="Edited_Logo_1", footer="Edited_Comment_1"))