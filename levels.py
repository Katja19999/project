import csv
import os


def load_level(path, file):
    level = []
    try:
        with open(os.path.join(*path, file), mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                level.append([int(cell) for cell in row])
    except FileNotFoundError or FileExistsError:
        print(f"FILE {file} CANNOT BE FOUND OR DOESNT EXIST.")
    return level
