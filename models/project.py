# One to many -> one project has many tasks
class Project:
  def __init__(self, title, description, due_date):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.tasks = [] # Stores each project's tasks

  def add_task(self, task):
    self.tasks.append(task)

  # Ensures the data returns as a string instead of a object reference
  def __str__(self):
    return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}"