# One to many -> one project has many tasks
from user_class import User
class Project(User):
  def __init__(self, title, description, due_date):
    self.title = title
    self.description = description
    self.due_date = due_date

  