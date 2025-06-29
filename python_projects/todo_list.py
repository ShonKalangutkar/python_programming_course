todo_list = []
completed_list = []

def add_item():
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f"{item} has been added to the to do list")
    
def remove_item():
    index = input("Enter the index of the item to remove")
    if index.isdigit() and 1 <= int(index) <= len(todo_list):
        removed_item = todo_list.pop(int(index)-1)
        print(f"{removed_item} has been removed from the list")
    else:
        print("Invalid Index. Please try again")

def display_list(lst, list_name):
    print(f"\n {list_name} :")
    for index, item in enumerate(lst, start=1):
        print(str(index)+"."+item)
    print()

def mark_item_completed():
    index = input("Enter the index of the item to mark as completed: ")
    if index.isdigit() and 1 <= int(index) <= len(todo_list): 
        completed_item = todo_list.pop(int(index)-1)
        completed_list.append(completed_item)
        print(f"{completed_item} has been marked as completed")
    else:
        print("Invalid Index. Please try again")

def main():
    while True:
        print("To Do list")
        print("1. Add Item")
        print("2. remove Item")
        print("3. marked Item as completed")
        print("4. Display to do list")
        print("5. display completed list")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            mark_item_completed()
        elif choice == 4:
            display_list(todo_list, "To Do List")
        elif choice == 5:
            display_list(completed_list, "Completed list")
        elif choice == 6:
            break
        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    main()