import typer

app = typer.Typer()
# for whatever reason the tasks list is not being saved to and read from T-T

# this comment made from WSL
# testing to ensure that pushing works

@app.command()
def load():
    with open("data.txt", "r") as save_data:
        for line in save_data.readlines():
            tasks.append(line)

@app.command()
def wipe():
    print("Proceeding with this action will delete all of your save data.")
    choice = input("Are you sure you want to proceed? (y/n)")
    if choice == "y" or choice == "Y":
        with open("data.txt", "w") as save_data:
            save_data.write("")
    else:
        print("Command cancelled.")

@app.command()
def menu():
    task_file = open("data.txt", "r")
    print(f"hello! here are your current tasks.")

    with open ("data.txt", "r") as data:
        for line in data:
            print(line)

@app.command()
def write(task: str):
    task_file = open ("data.txt", "a")
    task_file.write(f"- {task}")
    task_file.close()

if __name__ == "__main__":
    global tasks
    app()
    
