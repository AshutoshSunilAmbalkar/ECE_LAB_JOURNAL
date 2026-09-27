
import os
import config
def read_file():
    # If the file is not there, create an empty one
    if not os.path.exists(config.PROJECT_NAME):
        file = open(config.PROJECT_NAME, "w")
        file.close()
    data = {}
    file = open(config.PROJECT_NAME, "r")
    for line in file:
        if ":" in line:
            parts = line.split(":")
            name = parts[0].strip()
            quantity = parts[1].strip()
            data[name] = quantity

    file.close()

    return data
def write_file(data):
    file = open(config.PROJECT_NAME, "w")

    for name in data:
        file.write(name + " : " + str(data[name]) + "\n")

    file.close()