#import libraries
import json
from pathlib import Path
import sys

#colour code for warning
RED = '\033[31m'
RESET = '\033[0m'

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
print("Wecome to PyKanban!")
print(f"{RED}NOTE: Do not enter duplicate tasks.{RESET}")
while True:
  choice = input("\nWhat would you like to do? \n 1) New Task \n 2) View Board \n 3) Move Task \n 4) Remove Task \n 5) Exit \n \n >>> ")
  #Takes input and assigns it to kanban
  if choice == "1":
    task_input = input("\nPlease enter the task: ")
    kanban["To-do"].append(task_input)
    file_path.write_text(json.dumps(kanban, indent = 4))
  #Displays Kanban Board
  elif choice == "2":
    counter_todo = 1
    counter_doing = 1
    counter_done = 1
    print("\n------- KANBAN BOARD -------")
    print("\n--- To-do ---")
    if not kanban["To-do"]:
      print("--Empty--")
    for i in kanban["To-do"]:
      print(f"{counter_todo} --- {i}")
      counter_todo += 1
    print("\n--- Doing ---")
    if not kanban["Doing"]:
      print("--Empty--")
    for i in kanban["Doing"]:
      print(f"{counter_doing} --- {i}")
      counter_doing += 1
    print("\n--- Done ---")
    if not kanban["Done"]:
      print("--Empty--")
    for i in kanban["Done"]:
      print(f"{counter_done} --- {i}")
      counter_done += 1
  elif choice == "3":
    #Find where the task is.
    found = []
    update_choice = input("\n Enter task to move: ")
    if update_choice in kanban["To-do"]:
      found.append("To-do")
    elif update_choice in kanban["Doing"]:
      found.append("Doing")
    elif update_choice in kanban["Done"]:
      found.append("Done")
    #if task doesn't exist
    if len(found) == 0:
      print("Not found!")
      continue
    where_choice = input("Where would you like to move it? \n 1) To-do \n 2) Doing \n 3) Done \n >>> ")
    if where_choice not in ["1", "2", "3"]:
      print("Wrong choice!")
      continue
    #Removing the element first
    kanban[found[0]].remove(update_choice)
    #reassigning it to target board
    choices = {"1":"To-do", "2":"Doing", "3":"Done"}
    kanban[choices[where_choice]].append(update_choice)
    file_path.write_text(json.dumps(kanban, indent = 4))
  elif choice == "4":
    #Delete Task function
    remove_task = input("Which task would you like to delete?: ")
    found = []
    if remove_task in kanban["To-do"]:
      found.append("To-do")
    elif remove_task in kanban["Doing"]:
      found.append("Doing")
    elif remove_task in kanban["Done"]:
      found.append("Done")
    if len(found) == 0:
      print("Not found!")
      continue
    kanban[found[0]].remove(remove_task)
    file_path.write_text(json.dumps(kanban, indent = 4))
  elif choice == "5":
    sys.exit()
    

