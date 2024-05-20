tasks=[]

def add_task():
    task=input("Enter a new task:")
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("List of tasks:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")

def delete_task():
    if len(tasks)==0:
        print("No tasks to delete")
    else:
        print("Tasks:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")
        choice=int(input("Enter the task number to delete:"))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully")
        else:
            print("Invalid task number")

def main():

    while True:
        print("1.Add task")
        print("2.View task")
        print("3.Delete task")
        print("4.Quit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            delete_task()
        elif choice==4:
            print("Thank you for using the To-Do-List Application")
            break
        else:
            print("Invalid choice. Please try again.")

main()






