# One to many -> one user has many projects
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.users = []

    
