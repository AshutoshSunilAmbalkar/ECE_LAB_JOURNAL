import os

PROJECT_NAME= "inventory.txt"

def main():
    while True:
        print("\n***** ECE LAB INVENTORY *****")
        print("1] Do you want to add a new equipment ?")
        print("2] Show all equipments present in lab")
        print("3] Exit")
        choice = input("Pick an option (1, 2, or 3): ")
        if choice == '1':
            equipment_name = input("What is the component?: ")
            amount = input("Quantity: ")
            with open(PROJECT_NAME, "a") as f:
                f.write(equipment_name + " : " + amount + "\n")
            print("Equipment was entered")
        elif choice == '2':
            print("\n***** Your Equipments *****")
            if os.path.exists(PROJECT_NAME):
                with open(PROJECT_NAME, "r") as f:
                    content = f.read()
                    if content.strip() == "":
                        print("No equipments saved yet.")
                    else:
                        print(content)
            else:
                print("No equipments saved yet.")
                
        elif choice == '3':
            print("Saving and exiting the program")
            break
            
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()