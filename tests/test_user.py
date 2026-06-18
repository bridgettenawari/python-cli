import pytest
from models.user import User
from models.project import Project

def test_add_project_to_user():
    User.id = 1
    user = User("Alice", "alice@example.com")
    project = Project("Test Project", "Description", "2026-06-20")
    user.add_project(project)

    # Asserting what you want to be there
    assert user.projects[0].title == "Test Project"
    assert user.projects[0].description == "Description"
    assert user.projects[0].due_date == "2026-06-20"
    assert str(user) == f"1. Alice, alice@example.com"
