# One to many -> one user has many projects
class User:
  id = 0 # ID counter runs every time a User() is called
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.projects = [] # Stores each user's projects
    User.id += 1

    def add_project(self, project):
      self.projects.append(project)

    # Ensures the data returns as a string instead of a object reference
    def __str__(self):
      return f"Name: {self.name}, Email: {self.email} "
