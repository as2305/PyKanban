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
print("Wecome to PyKanban!")
while True:
  choice = input("\nWhat would you like to do? \n 1) New Task \n 2) View Board \n 3) Move Task \n \n >>> ")
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
  elif choice == "3":
    #Find where the task is.
    found = []
    update_choice = input("\n Enter task to move: ")
    if update_choice in kanban["To-do"]:
      found.append("To-do")
    if update_choice in kanban["Doing"]:
      found.append("Doing")
    if update_choice in kanban["Done"]:
      found.append("Done")
    print(found)
    #if task doesn't exist
    if len(found) == 0:
      print("Not found!")
      break
    where_choice = input("Where would you like to move it? \n 1) To-do \n 2) Doing \n 3) Done \n >>> ")
    #Removing the element first
    kanban[found[0]].remove(update_choice)
    #reassigning it to target board
    choices = {1:"To-do", 2:"Doing", 3:"Done"}
    kanban[choices[int(where_choice)]].append(update_choice)
    file_path.write_text(json.dumps(kanban, indent = 4))
    
