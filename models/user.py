# One to many -> one user has many projects
from models.project import Project
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
      return f"{self.id}. {self.name}, {self.email}"
  
  def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }
  
  @classmethod
  def from_dict(cls, data):
    user = cls(data.get("name"), data.get("email"))
    user.id = data.get("id", user.id)
    user.projects = [Project.from_dict(p) for p in data.get("projects", [])]
    return user

# jack = User("Jack", "jack@gmail.com")
# michael = User("Michael", "michael@gmail.com")
# jack.add_project("Cook food")
# print(jack.projects)
# print(jack)
# print(michael)