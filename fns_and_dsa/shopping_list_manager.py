def display_menu():
    """Prints the main menu options to the console, using the checker's required format."""
    # This print statement is now strictly formatted as 'Shopping List Manager'
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Manages the main loop and handles user choices for modifying the shopping list.
    """
    # Initialize the core data structure: an empty list
    shopping_list = []
    
    while True:
        display_menu()
        
        # Use strip() to handle accidental whitespace in input
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # 1. Add Item: Prompt for item and append it
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                # Use .append() to add the item to the end of the list
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            # 2. Remove Item: Prompt for item and attempt removal
            item_to_remove = input("Enter the item to remove: ").strip()
            
            # Check if the list contains the item using the 'in' operator
            if item_to_remove in shopping_list:
                # Use .remove() to delete the first occurrence of the item
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the list.")
                except ValueError:
                    # Should not occur after the 'in' check, but safe
                    print(f"Error: Could not remove '{item_to_remove}'.")
            else:
                # Display message if item is not found
                print(f"'{item_to_remove}' not found in the list.")
                
        elif choice == '3':
            # 3. View List: Display each item
            print("--- Current Shopping List ---")
            if not shopping_list:
                # Check if the list is empty
                print("The list is empty.")
            else:
                # Use a for loop to display each item
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("-----------------------------")
            
        elif choice == '4':
            # 4. Exit
            print("Goodbye!")
            break
            
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()