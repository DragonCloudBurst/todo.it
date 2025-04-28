import typer
import random

app = typer.Typer()

@app.command()
def wipe():
    print("Proceeding with this action will delete all of your save data.")
    choice = input("Are you sure you want to proceed? (y/n)")
    if choice == "y" or choice == "Y":
        with open("data.txt", "w") as save_data:
            save_data.write("")
            print("Sava data deleted.")
    else:
        print("Command cancelled.")

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

# i have just realized that this will currently delete a task with the same string in it
# for example delete 1 will also delete a task numbered 11
@app.command()
def write(task: str):
    task_id = random.randint(0, 999)

    task_file = open ("data.txt", "r")
    task_file_read = task_file.readlines()
    task_file.close()

    if str(task_id) in task_file_read:
        task_id += 1

    task_file = open ("data.txt", "a")
    task_file.write(f"(id {task_id}): {task}\n")
    task_file.close()

    print("Task logged.")

@app.command()
def delete(task_id: int):
    data = open("data.txt", "r")
    read_data = data.readlines()
    data.close()

    data_write = open("data.txt", "w")
    # here the program will delete only one line based on the task id you gave it
    for number, line in enumerate(read_data):
        if f"(id {task_id})" not in line:
            data_write.write(line)
    data_write.close()

        
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
    
