import os

current_directory = (os.path.basename(os.getcwd()))


def create_repository():
    try:
        os.system(f'echo # {current_directory} >> README.md')
        os.system("git init .")
        os.system("git add .")
        os.system('git commit -m "Initial Commit"')
        os.system("hub create")
        os.system("git push origin master")
    except:
        print("Oops..Something Went Wrong")


def push_to_repository(commitArg):
    try:
        os.system("git add .")
        os.system(f'git commit -m "{commitArg}"')
        os.system("git push origin master")
    except:
        os.system("git status")


# create_repository()
push_to_repository("Fixed readme")
