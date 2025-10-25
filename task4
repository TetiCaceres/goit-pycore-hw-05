# Splits input into command and arguments
def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args



# Decorator to handle user input errors (ValueError, KeyError, IndexError)
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # Raised when wrong number of arguments is provided
            return "Give me name and phone please."
        except KeyError:
            # Raised when contact not found
            return f"Contact not found."

        except IndexError:
            # Raised when name is missing
            return "Enter correct user name."
    return inner

# Check if phone is digits only, optionally starting with '+'
def is_valid_phone(phone):
    return phone.isdigit() or (phone.startswith("+") and phone[1:].isdigit())

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if not is_valid_phone(phone):
        return "Invalid phone number. Use only digits, optionally starting with +."
    contacts[name] = phone
    return f"Contact {name} added."

#Change an existing contact's phone number
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if not is_valid_phone(new_phone):
        return "Invalid phone number. Use only digits, optionally starting with +."
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        raise KeyError
    
  
#Show the phone number of a given contact 
@input_error  
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    
    name = args[0]
    phone = contacts.get(name)
    if phone :
        return f"{name}: {phone}"
    else:
        raise KeyError

#Show all contacts in the dictionary.
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{i+1}. {name}: {phone}" for i, (name, phone) in enumerate(contacts.items()))

help_messages = {
    "add": "add <name> <phone> — add a new contact",
    "change": "change <name> <new_phone> — change existing contact's phone",
    "phone": "phone <name> — show phone number of a contact",
    "all": "all — show all contacts",
    "hello": "hello — greet the bot",
    "exit": "exit — quit the bot"
}

#Handles user input and executes commands
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Available commands: add, change, phone, all, hello, exit")


    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            
            # Exit the bot
            if command in ["close", "exit"]:
                print("Good bye!")
                break

            # Simple greeting
            elif command == "hello":
                print("How can I help you?") 

            # Add new contact      
            elif command == "add":
                if not args:
                    print("Format: add <name> <phone>")
                    continue
                print(add_contact(args, contacts))

            # Change contact phone
            elif command == "change":
                if not args:
                    print("Format: change <name> <new_phone>")
                    continue
                print(change_contact(args, contacts))
            
            # Show contact phone
            elif command == "phone":
                if not args:
                   print("Format: phone <name>")
                   continue
                print(show_phone(args, contacts))

            # Show all contacts
            elif command == "all":
                print(show_all(contacts))

            # Ignore empty input
            elif command == "":
                # Empty input, ignore
                continue
            
            # Handle unknown commands
            else:
                # Show full help when unknown command is entered
                print("Invalid command. Available commands:")
                for msg in help_messages.values():
                    print("  ", msg)
        
        except Exception as e:
            # Catch any unexpected errors to prevent crash
            print(f"Unexpected error: {e}")
           


if __name__ == "__main__":
    main()
