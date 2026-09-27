
import file_operations
def add_item(name, quantity):
    data = file_operations.read_file()
    data[name] = quantity
    file_operations.write_file(data)
    print("Equipment added successfully!")
def show_items():
    data = file_operations.read_file()
    print("\n***** Your Equipments *****")
    if len(data) == 0:
        print("No equipments saved yet.")
    else:
        for key in data:
            print(key + " : " + data[key])
def update_item(name, new_qty):
    data = file_operations.read_file()
    if name in data:
        data[name] = new_qty
        file_operations.write_file(data)
        print("Updated " + name + " to " + new_qty)
    else:
        print("Item not found! Add it first.")
def delete_item(name):
    data = file_operations.read_file()
    if name in data:
        del data[name]
        file_operations.write_file(data)
        print("Deleted " + name + " from lab.")
    else:
        print("Item not found!")