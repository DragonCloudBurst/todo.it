import typer

app = typer.Typer()
# for whatever reason the tasks list is not being saved to and read from T-T
tasks = []

@app.command()
def menu():
    task_file = open("data.txt", "a")
    print(f"hello! here are your current tasks.")
    taskCount = 0
    for task in tasks:
        task_file.write(f"({taskCount}.) - {task}\n")
        print(f"{task}")
        taskCount += 1
    task_file.close()
    task_file_read = open("data.txt", "r")
    print(task_file_read.read())
    

@app.command()
def addtask(desc: str):
    tasks.append(desc)
    print(f"task added: {desc}")

if __name__ == "__main__":
    app()
    