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


#Main Code Starts