import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import save_data, load_data
from rich.console import Console
console = Console()
users = []

# Loading data
# Since loaded data was converted from json text to a dictionary, access it using variable["key"]
# Loop through the raw_data to find data with the key users then loop through the user data to find data with the key projects and loop through the project data to find data with the key tasks
raw_data = load_data()
users = raw_data["users"]

def add_user(args):
  # args saves the data typed in the terminal in an object allowing you to use it to access certain attributes using dot notation
  user = User(name=args.name, email=args.email)
  users.append(user)
  # Convert objects(classes) to dictionaries bc JSON only understands simple dat atypes like dictionaries and strings and numbers
  save_data({"users": users})
  console.print(f"[green]User added successfully[/green]")
 
def display_users(args):
  # If theres no users print message else loop through each user and display it on the terminal
  if not users:
      console.print("[red]No users found[/red]")
  else:
      for user in users:
          console.print(f"[cyan]{user}[/cyan]")

def add_project(args):
  # Loop through each user to check if the user's name exists if its the same create a project
  # since user was already defined using the User class use it to access the add project function and pass in the project as a parameter so that it is appended to the list of projects for the user
  for user in users:
    if user.name == args.user:
      project = Project(title=args.title, description=args.description, due_date=args.due_date)
      user.add_project(project)
      save_data({"users": users})
      console.print(f"[green]Project added[/green] {project} to user {user.name}")
      return
  console.print(f"[red]Project not added to {args.user}[/red]")


def display_projects(args):
  for user in users:
    if user.name == args.user:
      for project in user.projects:
        print(project)

def add_task(args):
  for user in users:
    if user.name == args.user:
      for project in user.projects:
        if project.title == args.project:
          task = Task(title=args.title, assigned_to=args.assigned_to)
          project.add_task(task)
          save_data({"users": users})
          console.print(f"[green]Task added[/green] {task} to project {project.title}")
          return
  console.print(f"[red]Task not added to {args.project}[/red]")


def display_tasks(args):
  for user in users:
    if user.name == args.user:
      for project in user.projects:
        if project.title == args.project:
          for task in project.tasks:
            print(task)

      

def main():
  console.print("[magenta]ᥫ᭡.ִֶָ𓂃Welcome to my CLIᥫ᭡.ִֶָ𓂃[/magenta]\n")
  console.print("[magenta] Run CLI using python3 main.py (command-name) ((--args 'value') if present)")

  parser = argparse.ArgumentParser(description="My Project Manager") # Sets up the CLI
  subparsers = parser.add_subparsers() # Allows us to define multiple commands

  # ADD USERS
  parser_add_user = subparsers.add_parser("add-user", help="Add a new user")
  parser_add_user.add_argument("--name", required=True, help="User's name")
  parser_add_user.add_argument("--email", required=True, help="User's email")
  parser_add_user.set_defaults(func=add_user)

  # DISPLAY USERS
  parser_display_users = subparsers.add_parser("display-users", help="Displays all users")
  parser_display_users.set_defaults(func=display_users)

  # ADD USER'S PROJECTS
  parser_add_project = subparsers.add_parser("add-project", help="Add a new project")
  parser_add_project.add_argument("--user", required=True, help="Name of the user who owns the project")
  parser_add_project.add_argument("--title", required=True, help="Project title")
  parser_add_project.add_argument("--description", required=True, help="Project description")
  parser_add_project.add_argument("--due_date", required=True, help="Project due date")
  parser_add_project.set_defaults(func=add_project)

  # DISPLAY USER'S PROJECTS
  parser_display_project = subparsers.add_parser("display-projects", help="Display a user's projects")
  parser_display_project.add_argument("--user", required=True, help="Name of user who owns the project")
  parser_display_project.set_defaults(func=display_projects)

  # ADD PROJECT'S TASKS
  parser_add_task = subparsers.add_parser("add-task", help="Add a new task")
  parser_add_task.add_argument("--user", required=True, help="Name of user who owns the project")
  parser_add_task.add_argument("--project", required=True, help="Name of project")
  parser_add_task.add_argument("--title", required=True, help="Title of the task")
  parser_add_task.add_argument("--assigned-to", required=False, default="Nobody", help="Who has this task been assigned to?")
  parser_add_task.set_defaults(func=add_task)

  # DISPLAY PROJECT'S TASKS
  parser_display_task = subparsers.add_parser("display-task", help="Displays a project's tasks")
  parser_display_task.add_argument("--user", required=True, help="User who owns the project")
  parser_display_task.add_argument("--project", required=True, help="Name of project")
  parser_display_task.set_defaults(func=display_tasks)

  args = parser.parse_args() # Takes what you typed in the terminal and parses \ converts it to become an object
  if hasattr(args, "func"): # Checks if it has a property called func e.g. func = add_task
      args.func(args) # If the func is present python runs it
  else:
      parser.print_help() # If not it prints all the helps we defined

if __name__ == "__main__":
  main()