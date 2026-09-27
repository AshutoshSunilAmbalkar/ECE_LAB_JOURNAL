
def show_menu():
    print("\n***** ECE LAB INVENTORY *****")
    print("1] Do you want to add a new equipment ?")
    print("2] Show all equipments")
    print("3] Update equipment quantity")
    print("4] Delete an equipment")
    print("5] Exit")

def take_input():
    choice = input("Pick an option (1, 2, 3, 4, or 5): ")
    return choice