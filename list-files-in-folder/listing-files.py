import os
def listing_files_in_folder(folder):
    try:
        file=os.listdir(folder)
        print(f"listing the files in folder: {folder}")
        for files in file:
            print(files)
            #continue
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("No permission to file")
    
def main():
    folders=input("Provide the list of  folders with space: ").split()

    for folder in folders:
        listing_files_in_folder(folder)

main()


    

