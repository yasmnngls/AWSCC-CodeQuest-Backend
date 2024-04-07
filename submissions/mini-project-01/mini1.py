def menu():
    return """\nOptions:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit"""

def add_item(shopping_list):
    item = input("Enter the item you want to add: ").capitalize()
    shopping_list.append(item)
    print(f"{item} has been added to your Shopping list.\n")

def view_list(shopping_list):
    print("Your Shopping list:")
    for num, item in enumerate(shopping_list, start=1):
        print(f"\t{num}. {item}")
    print()

def remove_item(shopping_list):
    item = input("Enter the item you want to remove: ").capitalize()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your Shopping list.\n")
    else:
        print(f"{item} is not in your Shopping list.\n")

def main():
    shopping_list = []
    action = 0
    while action != 4:
        print(menu())
        action = int(input("Enter the number of your choice: "))
        if action == 1:
            add_item(shopping_list)
        elif action == 2:
            view_list(shopping_list)
        elif action == 3:
            remove_item(shopping_list)
        elif action == 4:
            print("Thank you for using our Shopping List!\n")
        else:
            print("Invalid\n")

if __name__ == "__main__":
    main()