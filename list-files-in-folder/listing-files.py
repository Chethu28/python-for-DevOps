import os
def listing_files_in_folder(folder):
    try:
        file=os.listdir(folder)
        print(f"listing the files in folder: {folder}")
        for files in file:
            print(files)
            #continue
    except FileNotFoundError:
         print(f"Error: Folder '{folder}' not found.")
    except PermissionError:
        print(f"Error: No permission to access files in '{folder}'.")
    
def main():
    folders=input("Provide the list of  folders with space: ").split()

    for folder in folders:
        listing_files_in_folder(folder)

if __name__ == "__main__":
    main()

    

