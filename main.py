from pathlib import Path
import os

def createfile():
    try:
        name = input("Please tell your file name :- ")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("What you want to write :- ")
                fs.write(data)
            print("File created successfully")
        else:
            print("Error file name already exists")
    except Exception as err:
        print(f"An error occured as {err}")
def readfile():
    try:
        name = input ("Please tell your file name :- ")
        path = Path(name)
        if path.exists():
            with open(path, "r") as fs:
                content = fs.read()
                print(f" Your file content is \n {content}")
        else:
            print("Error no such file exists")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        name = input("Please tekk your file name :- ")
        path = Path(name)
        if path.exists():
            print("Operations")
            print("1. Renaming the file name :- ")
            print("2. Appending the file  content")
            print("3. Overwrriting the file")

            choice = int(input("Enter your option"))
            if choice == 1:
                new_name = input("Tell your new file name:- ")
                new_path = Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print("Renamed successfully")
                else:
                    print("File already exists")
            elif choice == 2:
                with open(path, 'a') as fs :
                    data = input ("What do you want to append:- ")
                    fs.write("\n" + data)
                    print("Successfully overwrite:-")
            elif choice == 3:
                with open(path, "w")as fs :
                    data = input ("What do you want to append:- ")
                    fs.write("\n" + data)
                    print("Successfully overwritten")
    except Exception as err:
        print(f"An error occured as {err}")
        
def deletfile():
    try:
        name = input("Please tell your file name :- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print(f"File {name} deleted successfuly")
        else:
            print(f"Error no such {name} file existes")
    except Exception as err:
        print(f"An error occured as {err}")






print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

a = int(input("\nTell your response :- "))
if a == 1:
    createfile()
if a == 2:
    readfile()
if a == 3:
    updatefile()
if a ==4 :
    deletfile()