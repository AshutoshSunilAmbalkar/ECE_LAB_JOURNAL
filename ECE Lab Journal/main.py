
import menu
import inventory_manager
def main() :
    while True :
        menu.show_menu()
        choice = menu.take_input()
        if choice == '1':
            name = input("Enter component : ")
            qty = input("Enter quantity: ")
            inventory_manager.add_item(name, qty)
        elif choice == '2':
            inventory_manager.show_items()
        elif choice == '3':
            name = input("Enter component to update: ")
            qty = input("Enter the new quantity: ")
            inventory_manager.update_item(name, qty)
        elif choice == '4':
            name = input("Enter component to delete: ")
            inventory_manager.delete_item(name)
        elif choice == '5':
            print("Saving and exiting")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()