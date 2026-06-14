from project_class import Project
class Task(Project):
  def __init__(self, title, status, assigned_to):
    self.title = title
    self.status = status
    self.assigned_to = assigned_to
    self.tasks = []

  