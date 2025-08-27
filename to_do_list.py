def menu():
    print("\n----TO-DO LIST MENU---")
    print("1.Add Task")
    print("2.View Task")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit")

def add(tasks):
    task=input("Enter the task:")
    tasks.append(task)
    print("Task added successfully!")

def view(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")

def update(tasks):
    view(tasks)
    if tasks:
        try:
            index=int(input("Enter the number to update:"))-1
            if(0<=index < len(tasks)):
                new=input("Enter the new task: ")
                tasks[index]=new
                print("Task updated successfully")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def delete(tasks):
    view(tasks)
    if tasks:
        try:
            index = int(input("Enter number to delete:"))-1
            if (0<=index < len(tasks)):
                removed = tasks.pop(index)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks=[]
    while True:
        menu()
        choice=input("Enter your choice (1-5): ")
        
        if choice == "1":
            add(tasks)
        elif choice == "2":
            view(tasks)
        elif choice == "3":
            update(tasks)
        elif choice == "4":
            delete(tasks)
        elif choice == "5":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()