import json
import os

def option_menu():
    menu = ["1 - Add Website, Username and Password",
            "2 - View",
            "3 - Search",
            "4 - Delete",
            "5 - Update",
            "6 - Close"]
    print("\n".join(menu))

def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def manager_pass(menu_act):
    os.system('cls')
    data = load_data()

    if menu_act == '1':
        website = input("Enter name of website: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        new_entry = {'email': email, 'password': password}
        
        if website in data: 
            data[website].append(new_entry) 
        else:
            data[website] = [new_entry]

        write_data(data)
        print("Successfully Added!")

    elif menu_act == '2':
        for website, website_data in data.items():
            print(f"Website: {website}")
            for entry in website_data:
                print(f"    Email: {entry['email']}")
                print(f"    Password: {entry['password']}")

    elif menu_act == '3':
        website = input("Enter website to search: ")
        if website in data:
            print("Website found!")
            for i, entry in enumerate(data[website], start=1):
                print(f"    {i} Email: {entry['email']}")
                print(f"      Password: {entry['password']}")
        else:
            print("No website found!")

    elif menu_act == '4':
        website = input("Enter website to delete: ")
        if website in data:
            del data[website]
            write_data(data)
            print("Successfully Removed!")
        else:
            print("Website not found!")

    elif menu_act == '5':
        website = input("Enter website to update: ")
        if website in data:
            updated = input(" 'EMAIL' or 'PASSWORD': ").lower()
            new_info = input(f"Enter your new {updated}: ")
            for entry in data[website]:
                entry[updated] = new_info
            write_data(data)
            print("Successfully updated!")
        else:
            print("No website found!")

    elif menu_act == '6':
        exit()

running = True

while running:
    print("=======>PASSWORD MANAGER<=======")
    option_menu()
    user_input = input("Enter a number: ")
    manager_pass(user_input)
