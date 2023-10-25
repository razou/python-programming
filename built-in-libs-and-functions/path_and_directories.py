import os


def os_walk(dir_path: str):
    python_files = []
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith(".py"):
                python_files.append(f)
                file_paths.append(os.path.join(root, f))
                
    print("len(python_files): ", len(python_files))
    print(python_files[:5])
    print("*"*10)
    print("len(file_paths): ", len(file_paths))
    print(file_paths[:10])

            


def os_walk_get_started(dir_path: str):
    """_summary_
Ref: https://pythoner.name/en/walk
   
"The walk() function returns a generator object from which to get tuples. 

Each tuple has three items:

=> Address of the current directory as a string.
 => List of subdirectories names of the first level nesting in this directory. 
If there are no subdirectories, the list will be empty.
=> List of file names of the first level nesting in the given directory. 
If there are no files, the list will be empty"

    Args:
        dir_path (str): _description_
    """
    g = os.walk(dir_path)
    print('type of g: ', type(g))
    
    print("************ tuples **************")
    for t in os.walk(dir_path):
        print(t)
        break
    
    print("********* tree ***********")
    root, dirs, files = next(g)
    print("root: ", root)
    print("dirs: ", dirs)
    print("files: ", files)
    
if __name__ == '__main__':
#    dir_path = "."
# os_walk_get_started(dir_path=dir_path)
# os_walk(dir_path) 
    my_file = "../REAME.md"
    print(os.path.basename(my_file))
    
