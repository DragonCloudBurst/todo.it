import typer
import random

app = typer.Typer()

# wipe all saved tasks from data.txt
# backup will not be deleted
@app.command()
def wipe():
    print("Proceeding with this action will delete all of your save data.")
    choice = input("Are you sure you want to proceed? (y/n)")
    if choice == "y" or choice == "Y" or choice == "yes":
        with open("data.txt", "w") as save_data:
            save_data.write("")
            print("Save data deleted.")
    else:
        print("Command cancelled.")

# open the main menu to display all tasks
@app.command()
def menu():
    task_file = open("data.txt", "r")
    print("  ┌───────┐")
    print(" ─┘       └─────────────────────────────────")
    print("  > hello! here are your current tasks.")
    print("")

    with open ("data.txt", "r") as data:
        for line in data:
            print(f"  {line}")

# display all completed tasks
@app.command()
def log():
    completed_file = open("completed.txt", "r")
    print("Here are your completed tasks:")
    for line in completed_file:
        print(line)

@app.command()
def write(task: str):
    task_id = random.randint(0, 999)

    task_file = open ("data.txt", "r")
    task_file_read = task_file.readlines()
    task_file.close()

    # ensures duplicate task ids cannot be added to the list
    if str(task_id) in task_file_read:
        task_id += 1

    # write the specified task to the list along with a random number id
    task_file = open ("data.txt", "a")
    task_file.write(f"(id {task_id}): {task}\n")
    task_file.close()

    print("Task logged.")

# use this to wipe a task from the list
# without marking it as complete
@app.command()
def delete(task_id: int):
    data = open("data.txt", "r")
    read_data = data.readlines()
    data.close()
    
    task_text = ""
        
    for line in read_data:
        if f"(id {task_id})" in line:
            task_text = line

    data_write = open("data.txt", "w")
    # here the program will delete only one line based on the task id you gave it
    data_write.write(task_text)
    data_write.close()

    print("Task deleted.")

# use this to mark a task as complete
# and save its data to completed_tasks
@app.command()
def complete(task_id: int):
    data = open("data.txt", "r")
    read_data = data.readlines()
    data.close()

    tasks_complete = open("completed.txt", "a")

    data_write = open("data.txt", "w")
    # here the program will delete only one line based on the task id you gave it
    for number, line in enumerate(read_data):
        if f"(id {task_id})" not in line:
            data_write.write(line)
        if f"(id {task_id})" in line:
            tasks_complete.write(line)
    data_write.close()
    tasks_complete.close()
   
    print("Task completed.")

# save a backup copy of the current task data
# erases the current backup and creates a new one
@app.command()
def backup():
    backup = open("backup.txt", "w")
    backup.write("")
    backup.close()
    backup = open("backup.txt", "a")
    with open ("data.txt", "r") as save_data:
        for line in save_data:
            backup.write(line)

    print("Data has been backed up.")
    
if __name__ == "__main__":
    app()
    
