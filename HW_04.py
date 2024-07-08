import pdb

contacts = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts.keys():
            contacts[name] = phone
            return "Contact added."
        else:
            print('Contact with this name already exists. Please try "change" command')
    except ValueError:
        print('Not enough data to create contact')

def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return 'Contact updated.'
    except KeyError:
        print('There is no such name in contacts. Try another name')

def show_contact(args, contacts):
    try:
        name = args[0]
        return contacts[name]
    except KeyError:
        print('There is no such name in contacts. Try another name')

def all(args, contacts):
        return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
