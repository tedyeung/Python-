
files = ["try_cats.txt", "try_dogs.txt"]

for file in files:
    with open(file) as file_obj:
        file_read = file_obj.read()
        print(file_read)