#import json and path libraries
import json
from pathlib import Path

#define the file path
file_path = Path("kanban.json")

#define JSON Structure
kanban = {
  "To-do": [],
  "Doing": [],
  "Done": []
}

#check if the file exists, if not, create a new one and assign the core JSON stucture
if not file_path.is_file():
    file_path.write_text(json.dumps(kanban, indent = 4))

kanban = json.loads(file_path.read_text())
#initiate the main program and take user choice
while True:
  choice = input("\nWelcome to PyKanban! What would you like to do? \n 1) New Task \n 2) View Board \n 3) Move Task \n \n >>>")
  #Takes input and assigns it to kanban
  if choice == "1":
    task_input = input("\nPlease enter the task: ")
    kanban["To-do"].append(task_input)
    file_path.write_text(json.dumps(kanban, indent = 4))
  #Displays Kanban Board
  elif choice == "2":
    counter = 1
    print("\n------- KANBAN BOARD -------")
    print("\n--- To-do ---")
    if not kanban["To-do"]:
      print("--Empty--")
    for i in kanban["To-do"]:
      print(f"{counter} --- {i}")
      counter += 1
    print("\n--- Doing ---")
    if not kanban["Doing"]:
      print("--Empty--")
    for i in kanban["Doing"]:
      print(f"{counter} --- {i}")
      counter += 1
    print("\n--- Done ---")
    if not kanban["Done"]:
      print("--Empty--")
    for i in kanban["Done"]:
      print(f"{counter} --- {i}")
      counter += 1