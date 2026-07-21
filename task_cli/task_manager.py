import copy
from time import strftime, gmtime

def add(description: str, task_dict:dict) -> dict:
    if not isinstance(description, str):
        raise ValueError(" add command requires a string type descrition")

    if not isinstance(task_dict, dict):
        raise ValueError("The task dictionary was not passed")
        
    inner_dict = copy.deepcopy(task_dict)
    keys = sorted(list(inner_dict.keys()))
    key = int(keys[-1]) + 1 if keys else 1
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    inner_dict[key] = {"description": description, "status": "todo", "createdAt": now, "updatedAt": now}
    print(f"Task created successfully at ID: {key}")
    return inner_dict

def update(id: int, description: str, task_dict: dict) -> dict:
    if not isinstance(id, int):
        raise ValueError(" update command requires a integer type id")

    if not isinstance(description, str):
        raise ValueError(" update command requires a string type descrition")

    if not isinstance(task_dict, dict):
        raise ValueError("The task dictionary was not passed")
        
    inner_dict = copy.deepcopy(task_dict)
    if str(id) not in inner_dict:
        raise ValueError("ID of the task does not exist")

    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    inner_dict[str(id)]["description"] = description
    inner_dict[str(id)]["updatedAt"] =  now
    return inner_dict

def delete(id: int, task_dict: dict) -> dict:
    if not isinstance(id, int):
        raise ValueError(" delete command requires a integer type id")

    if not isinstance(task_dict, dict):
        raise ValueError("The task dictionary was not passed")
        
    inner_dict = copy.deepcopy(task_dict)

    if str(id) not in inner_dict:
        raise ValueError("ID of the task does not exist")
    
    del inner_dict[str(id)]
    return inner_dict
def mark_in_progress(id: int, task_dict: dict) -> dict:
    if not isinstance(id, int):
        raise ValueError(" mark in progress command requires a integer type id")

    if not isinstance(task_dict, dict):
        raise ValueError("The task dictionary was not passed")
        
    inner_dict = copy.deepcopy(task_dict)

    if str(id) not in inner_dict:
        raise ValueError("ID of the task does not exist")
    
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    inner_dict[str(id)]["status"] = "in-progress"
    inner_dict[str(id)]["updatedAt"] =  now

    return inner_dict
def mark_done(id: int, task_dict: dict) -> dict:
    if not isinstance(id, int):
        raise ValueError(" mark-done command requires a integer type id")

    if not isinstance(task_dict, dict):
        raise ValueError("The task dictionary was not passed")
        
    inner_dict = copy.deepcopy(task_dict)

    if str(id) not in inner_dict:
        raise ValueError("ID of the task does not exist")
    
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    inner_dict[str(id)]["status"] = "done"
    inner_dict[str(id)]["updatedAt"] =  now

    return inner_dict

def list_tasks(status: str, task_dict: dict) -> dict:
    if not isinstance(status, str):
        raise ValueError("list command cannot take non string values")

    if status not in ["all", "todo", "in-progress", "done"]:
        raise ValueError("Status code does not exist")
    
    if not isinstance(task_dict, dict):
        raise ValueError("The task dictionary was not passed")
     
    if status == "all":
        for key, val in task_dict.items():
            print(f"{key}: {val}")

    else:
        for key, val in task_dict.items():
            if val["status"] == status:
                print(f"{key}: {val}")

    return task_dict
