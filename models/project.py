# One to many -> one project has many tasks
class Project:
  id = 1 # ID starts from one
  def __init__(self, title, description, due_date):
    self.id = Project.id 
    Project.id += 1
    self.title = title
    self.description = description
    self.due_date = due_date
    self.tasks = [] # Stores each project's tasks


  def add_task(self, task):
    self.tasks.append(task)

  # Ensures the data returns as a string instead of a object reference
  def __str__(self):
    return f"{self.id}. {self.title.capitalize()} - {self.description} [{self.due_date}]"
  
  def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks]
        }
  
project1 = Project("Prepare supper", "Ugali, Sukuma, Fish.", "20/06/2026")
project2 = Project("Wash clothes", "Wash all my clothes.", "28/05/2026")
project1.add_task("Cook food")
project1.add_task("Fry meat")
print(project1.tasks)
print(project1)
print(project2)