# One to many -> one user has many projects
class User:
  id = 1 
  def __init__(self, name, email):
    self.id = User.id
    User.id += 1
    self.name = name
    self.email = email
    self.projects = [] # Stores each user's projects

  def add_project(self, project):
      self.projects.append(project)

    # Ensures the data returns as a string instead of a object reference
  def __str__(self):
      return f"{self.id}. {self.name}, {self.email} "

# jack = User("Jack", "jack@gmail.com")
# michael = User("Michael", "michael@gmail.com")
# jack.add_project("Cook food")
# print(jack.projects)
# print(jack)
# print(michael)