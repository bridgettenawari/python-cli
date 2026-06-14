
class Task:
  def __init__(self, title, status="Incomplete", assigned_to="Nobody"):
    self._title = title
    self._status = status
    self._assigned_to = assigned_to

# Property and setter can only take one other argument apart from self so you have to put each attribute in a different property and setter function
# Use a self_.attribute to prevent the attribute from running forever (recursion) and also prevent it from being accessed directly when assigning value to out attributes

  @property
  def title(self):
    return self._title
  
  @title.setter
  def title(self, value):
    if value == "":
      raise ValueError("Title cannot be empty.")
    self._title = value
  
  @property
  def status(self):
    return self._status
  
  @status.setter
  def status(self, value):
    allowed_status = ["Incomplete", "Complete"]
    if value not in allowed_status:
      raise ValueError("Invalid Status")
    self._status = value
  
  @property
  def assigned_to(self):
    return self._assigned_to
  
  @assigned_to.setter
  def assigned_to(self, value):
    self._assigned_to = value

  # Ensures the data returns as a string instead of a object reference
  def __str__(self):
    return f"The task {self.title} has been assigned to {self.assigned_to}, status: [{self.status}]"
  