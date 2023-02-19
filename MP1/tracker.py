from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    task["lastActivity"] = datetime.now()
    # set the name, description, and due date (all must be provided)
    if name and description and due:
        task['name'] = name
        task['description'] = description
        # due date must match one of the formats mentioned in str_to_datetime()
        task['due'] = str_to_datetime(due)
        # add the new task to the tasks list
        tasks.append(task)
    # output a message confirming the new task was added or if the addition was rejected due to missing data
        print('New task was added.')
    else:
        print('New task rejected due to missing data.')
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/13/23
    Summary: Used if loop to check if info was provided and if it was, set name, description, and due date. if it wasnt, print rejection message
    '''

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Invalid Index entered.")
        #exit the function in way bc if the index is wrong, it's pointless to continue with the function
        return

    task = tasks[index]
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    name = input(f"What's the name of this task? ({task['name']}) \n").strip()
    desc = input(f"What's a brief descriptions of this task? ({task['description']}) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) ({task['due']}) \n").strip()
    update_task(index, name=name, description=desc, due=due)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/15/23
    Summary: Used if loop to check for index bounds and replaced the todos with existing value of each property 
    '''
    
    

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Invalid Index entered.")
        #exit the function in way bc if the index is wrong, it's pointless to continue with the function
        return
    task = tasks[index]
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    if name:
        task['name'] = name
    if description: 
        task['description'] = description
    # due date must match one of the formats mentioned in str_to_datetime()
    if due:
        task['due'] = str_to_datetime(due)
    # update lastActivity with the current datetime value
    task["lastActivity"] = datetime.now()
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    if name or description or due:
        print("Task was updated")
    else:
        print("Task was not updated")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Used if loop to check for index bounds and used if statements to check if info was provided and if it was, updated it and if not, left it alone
    '''

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Invalid Index entered.")
        #exit the function in way bc if the index is wrong, it's pointless to continue with the function
        return
 
    task = tasks[index]
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    if not task['done']:
        task['done'] = datetime.now()
    else:
        print(f"Task {task['name']} is already completed.")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Used if loop to check for index bounds and used if statements to check if task wasnt done and if it wasnt, set it to current time else, print its done
    '''

    

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Invalid Index entered.")
        #exit the function in way bc if the index is wrong, it's pointless to continue with the function
        return

    task = tasks[index]
    # utilize the given print statement when a task is found
    #task = {}
    if task:
        print(f"""
            [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
            Description: {task['description']} \n 
            Last Activity: {task['lastActivity']} \n
            Due: {task['due']}\n
            Completed: {task['done'] if task['done'] else '-'} \n
            """.replace('  ', ' '))
    else:
        print("Task not found.")
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Used if loop to check for index bounds and used if statements to check if task exists and if so print given statement and if not print it nonexistent
    '''

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Invalid Index entered.")
        #exit the function in way bc if the index is wrong, it's pointless to continue with the function
        return
    task = tasks[index]
    # delete/remove task from list by index
    tasks.pop(index)
    # message should show if it was successful or not
    if task not in tasks:
        print("Task successfully removed")
    else:
        print("Task not successfully deleted")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Used if loop to check for index bounds and used pop function to delete remove task at specified index and used if statement to check if it was deleted
    '''
    

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    _tasks = []
    for task in tasks:
        if not task['done']:
            _tasks.append(task)
    # pass that list into list_tasks()
    list_tasks(_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Used for loop to loop thru each task and if task isn't marked done, then itll be added to a list which will be passed thru a function that will
    display the tasks that are incomplete. 
    '''

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    _tasks = []
    for task in tasks:
        if not task['done'] and (datetime.now() > task["due"]):
            _tasks.append(task) 
    # pass that list into list_tasks()
    list_tasks(_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Used for loop to loop thru each task and if task isn't marked done and the current date is after the due date, then itll be added to a list 
    which will be passed thru a function that will display the tasks that are incomplete. 
    '''
    

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("Invalid Index entered.")
        #exit the function in way bc if the index is wrong, it's pointless to continue with the function
        return

    task = tasks[index]
    # get the days, hours, minutes, seconds between the due date and now
    diff = str_to_datetime(task['due']) - datetime.now()
    #check for task overdue
    #if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    if diff.total_seconds() < 0:
        overdue = True
        diff = abs(diff)
        # display the remaining time via print in a clear format showing days, hours, minutes, seconds
        print(f"Your task is overdue by {diff.days} days, {diff.seconds // 3600} hours, {(diff.seconds//60) % 60} minutes, and {diff.seconds % 60} seconds overdue.")
    else:
        overdue = False
        print(f"Your task is due in {diff.days} days, {diff.seconds // 3600} hours, {(diff.seconds//60) % 60} minutes, and {diff.seconds % 60} seconds overdue.")
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID: mm2836
    Date: 2/17/23
    Summary: Found the difference between the due date and the current date. If the time in seconds (after difference is converted to seconds) is
    less than the zero, the amt of time passed after the due date in days, hours, minutes, seconds will be displayed (after taking absolute value so results 
    will be positive). If it's not overdue, the time remaining will be displayed. 
    '''

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()