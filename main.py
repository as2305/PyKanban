#import json and path libraries
import json
from pathlib import Path

#define the file path
file_path = Path("kanban.json")

#define JSON Structure
kanban_structure = {
  "To-do": [],
  "Doing": [],
  "Done": []
}

#check if the file exists, if not, create a new one and assign the core JSON stucture
if not file_path.is_file():
    file_path.write_text(json.dumps(kanban_structure, indent = 4))

#initiate the main program and take user choice
while True:
  choice = input("\nWelcome to PyKanban! What would you like to do? \n 1) New Task \n 2) View Board \n >>>")
  #Takes input and assigns it to kanban_structure
  if choice == "1":
    task_input = input("\nPlease enter the task: ")
    kanban_structure["To-do"].append(task_input)
  #Displays Kanban Board
  elif choice == "2":
    counter = 1
    for i in kanban_structure["To-do"]:
      print(f"{counter} --- {i}")
      counter += 1
