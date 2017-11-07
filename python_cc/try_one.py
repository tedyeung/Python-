
files = ["try_cats.txt", "try_dogs.txt", "birds.txt"]

for file in files:
    try:
        with open(file) as file_obj:
            file_read = file_obj.read()
            print(file_read)
    except:
        print ("\nOne file is missing!!!")
        